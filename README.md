# Diabetes Prediction Web Application

## Overview
A Django-based platform for assessing diabetes risk using machine learning (logistic regression). Users can log in, manage profiles, and receive personalized health insights based on key health metrics.

> **Note:** Predictions are for informational purposes only. Consult healthcare professionals for medical advice.

---

## Features
- **User Authentication:** Secure login, registration, and profile management.
- **Health Metric Input:** Users enter metrics like glucose level, blood pressure, etc.
- **Real-Time Predictions:** Instant diabetes risk assessment.
- **Clear Results:** Categorizes users as "Diabetic" or "Non-Diabetic."
- **Error Handling:** Alerts for invalid inputs.

---

## Installation
1. Ensure Python 3.x is installed.
2. Clone the repository:
   ```bash
   git clone <repository-link>
   cd <project-folder>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

## Usage
1. Start the server:
   ```bash
   python manage.py runserver
   ```
2. Access the application at `http://127.0.0.1:8000`.
3. Register, log in, and input health metrics for predictions.

---

## Future Improvements
- Enhanced user profiles for tracking health metrics.
- Data visualization for better insights.
- Mobile optimization for improved accessibility.

---

## Author
**Sri Harsha Jampani**  
Email: [jampaniharsha6105@gmail.com](mailto:jampaniharsha6105@gmail.com)




# Screenshots  

## Home
![Screenshot 2025-01-16 144608](https://github.com/user-attachments/assets/37574d8f-f3c1-4037-80f4-7c26637af813)

## Login
![Screenshot 2025-01-16 143703](https://github.com/user-attachments/assets/1aa54cf0-ac0a-45eb-9b53-5c07b4619cf7)

## Signup

![Screenshot 2025-01-16 144620](https://github.com/user-attachments/assets/f48c4db2-0bc5-4b35-9edb-589f35b95a98)

## Profile

![Screenshot 2025-01-16 151705](https://github.com/user-attachments/assets/63e9a653-ca33-446d-86ec-a224bf7172d4)





