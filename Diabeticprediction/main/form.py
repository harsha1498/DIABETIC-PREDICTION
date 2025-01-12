from django import forms
from .models import Upload_csv_file

class CSVUploadForm(forms.Form):
    model= Upload_csv_file
    fields = ['file']

class DiabetesPredictionForm(forms.Form):
    # Defining fields for the form with diabetic example values
    pregnancies = forms.IntegerField(
        label='Number of Pregnancies',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of pregnancies'}),
        min_value=0,  # Assuming pregnancies cannot be negative
        initial=2  # Example value for a typical individual
    )
    glucose = forms.FloatField(
        label='Glucose Level (mg/dL)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter glucose level'}),
        min_value=0.0,
        initial=150.0  # Example value indicating potential diabetes
    )
    blood_pressure = forms.FloatField(
        label='Blood Pressure (mm Hg)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter blood pressure'}),
        min_value=0.0,
        initial=130.0  # Example value reflecting elevated blood pressure
    )
    skin_thickness = forms.FloatField(
        label='Skin Thickness (mm)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter skin thickness'}),
        min_value=0.0,
        initial=30.0  # Example value for skin thickness in diabetic patients
    )
    insulin = forms.FloatField(
        label='Insulin Level (µU/mL)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter insulin level'}),
        min_value=0.0,
        initial=50.0  # Example value for insulin level in diabetic patients
    )
    bmi = forms.FloatField(
        label='BMI',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter BMI'}),
        min_value=10.0,  # Adjusted minimum value to reflect realistic ranges
        max_value=60.0,  # Added maximum value for higher BMI cases
        initial=32.0  # Example value indicating obesity
    )
    dpf = forms.FloatField(
        label='Diabetes Pedigree Function',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter diabetes pedigree function'}),
        min_value=0.0,
        max_value=2.5,  # Added maximum value
        initial=1.2  # Example value for higher genetic risk
    )
    age = forms.IntegerField(
        label='Age (years)',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
        min_value=0,  # Assuming age cannot be negative
        max_value=120,  # Added maximum value for realistic age range
        initial=45  # Example value for an adult likely to have diabetes
    )

    def clean(self):
        cleaned_data = super().clean()

        # Example: Check that insulin is reasonable
        insulin = cleaned_data.get('insulin')
        if insulin is not None and insulin < 0:
            self.add_error('insulin', 'Insulin level cannot be negative.')

        # Example: Validate glucose level
        glucose = cleaned_data.get('glucose')
        if glucose is not None and (glucose < 0 or glucose > 200):
            self.add_error('glucose', 'Glucose level must be between 0 and 200 mg/dL.')

        # Example: Validate blood pressure
        blood_pressure = cleaned_data.get('blood_pressure')
        if blood_pressure is not None and (blood_pressure < 0 or blood_pressure > 200):
            self.add_error('blood_pressure', 'Blood pressure must be between 0 and 200 mm Hg.')

        # Example: Validate skin thickness
        skin_thickness = cleaned_data.get('skin_thickness')
        if skin_thickness is not None and (skin_thickness < 0 or skin_thickness > 99):
            self.add_error('skin_thickness', 'Skin thickness must be between 0 and 99 mm.')

        # Example: Validate BMI
        bmi = cleaned_data.get('bmi')
        if bmi is not None and (bmi < 10 or bmi > 60):
            self.add_error('bmi', 'BMI must be between 10 and 60.')

        # Example: Validate diabetes pedigree function
        dpf = cleaned_data.get('dpf')
        if dpf is not None and (dpf < 0 or dpf > 2.5):
            self.add_error('dpf', 'Diabetes pedigree function must be between 0 and 2.5.')

        # Example: Validate age
        age = cleaned_data.get('age')
        if age is not None and (age < 0 or age > 120):
            self.add_error('age', 'Age must be between 0 and 120 years.')

        return cleaned_data