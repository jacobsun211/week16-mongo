from fastapi import FastAPI
from app import dal
import uvicorn


app = FastAPI()


@app.get("/health")
def health_check():
    return {'status': 'not ok'}

@app.get('/employees/engineering/high-salary')
def get_engineering_high_salary():
    return dal.get_engineering_high_salary_employees()

@app.get('/employees/by-age-and-role')
def get_by_age_and_role():
    return dal.get_employees_by_age_and_role()


@app.get('/employees/top-seniority')
def get_top_seniority_employees_without_hr():
    return dal.get_top_seniority_employees_excluding_hr()


@app.get('/employees/age-or-seniority')
def get_employees_by_age_or_seniority():
    return dal.get_employees_by_age_or_seniority()


@app.get('/employees/managers/excluding-departments')
def get_managers_without_departments():
    return dal.get_managers_excluding_departments()


@app.get('/employees/by-lastname-and-age')
def get_by_lastname_and_age():
    return dal.get_employees_by_lastname_and_age()



