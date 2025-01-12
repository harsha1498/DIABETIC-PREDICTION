@echo off
echo Creating virtual environment...
call python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing Django...
call pip install django



echo Installing dependencies from requirements.txt...
call pip install -r requirements.txt
