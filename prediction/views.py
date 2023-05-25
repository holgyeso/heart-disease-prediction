from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import pandas as pd
from prediction.forms import HeartDiseaseForm
from django.contrib import messages

# helper functions
def get_data_size() -> tuple:
    return settings.DF.shape


def normalize_data(data_dict:dict, ord_enc, one_enc, std_scaler) -> pd.DataFrame:

    # make df from data
    df = pd.DataFrame(data_dict, index=[0])

    # apply categorical encoder; it should be the first because it generates additional columns
    df_norm = pd.DataFrame(one_enc.transform(df[one_enc.feature_names_in_]).toarray(), columns=one_enc.get_feature_names_out())

    # apply ordinal encoder
    df_norm[ord_enc.get_feature_names_out()] = ord_enc.transform(df[ord_enc.feature_names_in_])

    # apply standard scaling
    df_norm[std_scaler.get_feature_names_out()] = std_scaler.transform(df[std_scaler.feature_names_in_])

    df_norm.rename(columns={"Race_American Indian\/Alaskan Native": "Race_American Indian/Alaskan Native"}, inplace=True)

    return df_norm

def make_prediction(df: pd.DataFrame, model) -> bool:

    if model.predict(df[model.feature_names_in_])[0] == 1:
        return True
    return False

# view functions
def user_form(request):

    form = HeartDiseaseForm()

    if request.method == "POST":
        # construct data dict; that will be used to form a df like the one that it was given to the scalers/encoders

        data_dict = {}

        for f in settings.ORD_ENC.feature_names_in_:
            data_dict[f] = request.POST.get(f.lower())

        for f in settings.ONE_ENC.feature_names_in_:
            data_dict[f] = request.POST.get(f.lower())
        
        for f in settings.STD_SCL.feature_names_in_:
            data_dict[f] = float(request.POST.get(f.lower(), "0"))

        # calculate BMI from weight and height
        data_dict["BMI"] = float(request.POST.get("weight")) / (float(request.POST.get("height"))**2)


        df = normalize_data(data_dict=data_dict, 
                            ord_enc=settings.ORD_ENC, 
                            one_enc=settings.ONE_ENC,
                            std_scaler=settings.STD_SCL)
        
        pred = make_prediction(df,model=settings.MODEL)
        
        context = {
            "form_input": dict(sorted(data_dict.items())),
            "prediction": pred
        }

        return render(request, "prediction/form_results.html", context=context)

    context = {
        "form": form
    }

    context["row_nr"], context["col_nr"] = get_data_size()

    return render(request, "prediction/form_input.html", context=context)
