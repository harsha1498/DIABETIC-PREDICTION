#<a class" id="Admin" href="{% url 'Admin' %}">admin<i for="Admin" class="fa-sharp-duotone fa-light fa-ranking-star"></i></a>
from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.views.decorators.csrf import csrf_protect
from .form import DiabetesPredictionForm
from django.contrib import messages
from user.forms import UserLoginForm
from .models import Upload_csv_file

import pandas as pd
import numpy as np
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create your views here.
def about(request):
    return render(request,"about.html")

# def admin_view(request):
#     return

def predict(request):
    result1 = None
    form = DiabetesPredictionForm()  # Initialize the form at the beginning
    existing_file = Upload_csv_file.objects.first() 
    file_path = existing_file.file.path
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DiabetesPredictionForm(request.POST)  # Instantiate the form with POST data
            if form.is_valid():  # Check if the form is valid
                # Get cleaned data
                val1 = form.cleaned_data['pregnancies']
                val2 = form.cleaned_data['glucose']
                val3 = form.cleaned_data['blood_pressure']
                val4 = form.cleaned_data['skin_thickness']
                val5 = form.cleaned_data['insulin']
                val6 = form.cleaned_data['bmi']
                val7 = form.cleaned_data['dpf']  # DPF from form
                val8 = form.cleaned_data['age']

                # Load the dataset
                data = pd.read_csv(file_path)
                x = data.drop("Outcome", axis=1)
                y = data["Outcome"]

                # Train the model
                x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
                model = LogisticRegression(solver='liblinear', max_iter=200)
                model.fit(x_train, y_train)

                # Create a DataFrame for input values with consistent feature names
                input_data = pd.DataFrame([[val1, val2, val3, val4, val5, val6, val7, val8]],
                                          columns=["Pregnancies", "Glucose", "BloodPressure", 
                                                   "SkinThickness", "Insulin", "BMI", 
                                                   "DiabetesPedigreeFunction", "Age"])

                # Make predictions
                prediction = model.predict(input_data)

                # Interpret the prediction
                result1 = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"
            else:
                # Handle form errors
                for key, error_list in form.errors.items():
                    for error in error_list:
                        messages.error(request, error) 

    else:
        # If the user is not authenticated
        if request.method == 'POST':
            messages.warning(request, "You should login first to display <b>Results</b>.")
            return redirect("login")  # Redirect to the login page

    return render(request, "home.html", {'form': form, 'result1': result1})