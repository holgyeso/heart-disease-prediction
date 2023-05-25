from django import forms


class HeartDiseaseForm(forms.Form):

    height = forms.DecimalField(label="Height (m)",
                                min_value=0,
                                step_size=0.01)

    weight = forms.DecimalField(label="Weight (kg)",
                                min_value=0,
                                step_size=0.01)

    sex = forms.CharField(label='Sex',
                          widget=forms.Select(choices=[('Female', 'Female'), ('Male', 'Male')]))

    agecategory = forms.CharField(label='Age',
                          widget=forms.Select(choices=[
                              ('18-24', '18-24'),
                              ('25-29', '25-29'),
                              ('30-34', '30-34'),
                              ('35-39', '35-39'),
                              ('40-44', '40-44'),
                              ('45-49', '45-49'),
                              ('50-54', '50-54'),
                              ('55-59', '55-59'),
                              ('60-64', '60-64'),
                              ('65-69', '65-69'),
                              ('70-74', '70-74'),
                              ('75-79', '75-79'),
                              ('80 or older', '80 or older'),
                          ]))

    race = forms.CharField(label='Race',
                           widget=forms.Select(choices=[
                               ('White', 'White'),
                               ('Black', 'Black'),
                               ('Asian', 'Asian'),
                               ('American Indian/Alaskan Native',
                                'American Indian/Alaskan Native'),
                               ('Hispanic', 'Hispanic'),
                               ('Other', 'Other')
                           ]))

    smoking = forms.CharField(label='Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]',
                              widget=forms.Select(choices=[('No', 'No'), ('Yes', 'Yes')]))

    alcoholdrinking = forms.CharField(label='Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week',
                                      widget=forms.Select(choices=[('No', 'No'), ('Yes', 'Yes')]))

    diabetic = forms.CharField(label='(Ever told) (you had) diabetes?',
                               widget=forms.Select(choices=[
                                   ('No', 'No'), 
                                   ('No, borderline diabetes', 'No, borderline diabetes'),
                                   ('Yes', 'Yes'),
                                   ('Yes (during pregnancy)', 'Yes (during pregnancy)')
                                   ]))

    stroke = forms.CharField(label='(Ever told) (you had) a stroke?',
                             widget=forms.Select(choices=[('No', 'No'), ('Yes', 'Yes')]))

    
    asthma = forms.CharField(label='(Ever told) (you had) asthma?',
                            widget=forms.Select(choices=[('No', 'No'), ('Yes', 'Yes')]))
    
    kidneydisease = forms.CharField(label='Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?',
                            widget=forms.Select(choices=[('No', 'No'), ('Yes', 'Yes')]))
    
    skincancer = forms.CharField(label='(Ever told) (you had) skin cancer?',
                        widget=forms.Select(choices=[('No', 'No'), ('Yes', 'Yes')]))

    physicalactivity = forms.CharField(label="Did you do any physical activity or exercise during the past 30 days other than your regular job?",
                                       widget=forms.Select(choices=[('No', 'No'), ('Yes', 'Yes')]))

    diffwalking = forms.CharField(label='Do you have serious difficulty walking or climbing stairs?',
                                  widget=forms.Select(choices=[('No', 'No'), ('Yes', 'Yes')]))

    physicalhealth = forms.IntegerField(label="For how many days during the past 30 days was your physical health not good? (0-30 days)",
                                        min_value=0,
                                        max_value=30,
                                        step_size=1)

    mentalhealth = forms.IntegerField(label="For how many days during the past 30 days was your mental health not good? (0-30 days)",
                                      min_value=0,
                                      max_value=30,
                                      step_size=1)
    
    sleeptime = forms.IntegerField(label="On average, how many hours of sleep do you get in a 24-hour period?",
                                    min_value=1,
                                    max_value=24,
                                    step_size=1)

    genhealth = forms.CharField(label='Would you say that in general your health is...',
                           widget=forms.Select(choices=[
                               ('Poor', 'Poor'),
                               ('Fair', 'Fair'),
                               ('Good', 'Good'),
                               ('Very good', 'Very good'),
                               ('Excellent', 'Excellent')
                           ]))

    