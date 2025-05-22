from django import forms

class HeartForm(forms.Form):
    age = forms.IntegerField()
    sex = forms.IntegerField()
    chest_pain_type = forms.IntegerField()
    resting_bp_s = forms.IntegerField()
    cholesterol = forms.IntegerField()
    fasting_blood_sugar = forms.IntegerField()
    resting_ecg = forms.IntegerField()
    max_heart_rate = forms.IntegerField()
    exercise_angina = forms.IntegerField()
    oldpeak = forms.FloatField()
    ST_slope = forms.IntegerField()
