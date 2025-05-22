# Create your views here.
import os
import joblib
import numpy as np
from django.shortcuts import render
from .forms import HeartForm
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, '..', 'heart_disease_model.pkl')
SCALER_PATH = os.path.join(settings.BASE_DIR, '..', 'scaler.pkl')

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_heart_disease(request):
    prediction = None
    if request.method == 'POST':
        form = HeartForm(request.POST)
        if form.is_valid():
            data = np.array([[
                form.cleaned_data['age'],
                form.cleaned_data['sex'],
                form.cleaned_data['chest_pain_type'],
                form.cleaned_data['resting_bp_s'],
                form.cleaned_data['cholesterol'],
                form.cleaned_data['fasting_blood_sugar'],
                form.cleaned_data['resting_ecg'],
                form.cleaned_data['max_heart_rate'],
                form.cleaned_data['exercise_angina'],
                form.cleaned_data['oldpeak'],
                form.cleaned_data['ST_slope'],
            ]])
            scaled_data = scaler.transform(data)
            prediction = model.predict(scaled_data)[0]
    else:
        form = HeartForm()
    return render(request, 'predictor/index.html', {'form': form, 'prediction': prediction})
