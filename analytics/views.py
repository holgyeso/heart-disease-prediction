import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import pandas as pd
from analytics.forms import InspectDataForm
from django.contrib import messages

# helper functions

def get_dtypes(df: pd.DataFrame) -> dict:
    dtypes_dict = df.dtypes.apply(lambda x: x.name).to_dict()
    return dict(sorted(dtypes_dict.items()))


def column_name_norm(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        col_lower = col[0].lower() + col[1:]
        cap_chars = re.findall(r'[A-Z]', col_lower)
        if len(cap_chars) == 1:  # knowing that columns are in camelCase form (only one capital char)
            df.rename(columns={col: col[:col.index(
                cap_chars[0])] + " " + col[col.index(cap_chars[0]):]}, inplace=True)
    return df


def n_head_rows(df: pd.DataFrame, n: int) -> dict:
    df = column_name_norm(df=df)
    return df.head(n).to_dict(orient='split')


def n_tail_rows(df: pd.DataFrame, n: int) -> dict:
    df = column_name_norm(df=df)
    return df.tail(n).to_dict(orient='split')


def col_stats(df: pd.DataFrame, include=None):
    stats_df = df.describe(include=include)
    missing = {}

    for c in stats_df.columns:
        missing[c] = len(df.loc[df[c].isna()])
    
    df = column_name_norm(df)

    stats_dict = pd.concat([stats_df, pd.DataFrame(missing, index=["missing"])]).to_dict(orient="split")

    for col in stats_dict["index"]:
        stats_dict["data"][stats_dict["index"].index(col)] = [col] + stats_dict["data"][stats_dict["index"].index(col)]


    return stats_dict


# view functions

def feature_details(request):

    context = {
        "dtypes": get_dtypes(settings.DF),
        "nr_cols": 2
    }

    return render(request, "analytics/features.html", context=context)


def first_n_rows(request):

    context = {}

    if request.method == "POST":

        if request.POST.get("order") == "first":
            context["data_dict"] = n_head_rows(
                df=settings.DF_LABELED, n=int(request.POST.get("nr")))
        else:
            context["data_dict"] = n_tail_rows(
                df=settings.DF_LABELED, n=int(request.POST.get("nr")))

        context["nr_cols"] = settings.DF_LABELED.shape[-1]

        form = InspectDataForm({
            "order": request.POST.get("order"),
            "nr": request.POST.get("nr")
        })

    else:
        form = InspectDataForm()

    context["form"] = form

    return render(request, "analytics/inspect.html", context=context)


def stats(request):
    context = {
        "nr_rows": settings.DF.shape[0],
        "nr_cols": settings.DF.shape[-1],
    }

    context["numerical"] = col_stats(df=settings.DF)
    context["numerical_col_nr"] = len(context["numerical"]["columns"]) + 1
    context["numerical_col_nr_display"] = context["numerical_col_nr"] - 1


    context["categorical"] = col_stats(df=settings.DF, include='object')
    context["categorical_col_nr"] = len(context["categorical"]["columns"]) + 1
    context["categorical_col_nr_display"] = context["categorical_col_nr"] - 1

    return render(request, "analytics/statistics.html", context=context)
