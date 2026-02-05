from fastapi import FastAPI
from app import dal
app = FastAPI()


@app.get("/health")
def health_check():
    return {'status': 'not ok'}

@app.get('/q1/customers-credit-limit-outliers')
def customers_credit_limit_outliers():
    return dal.get_engineering_high_salary_employees()


# python -m uvicorn app.main:app --reload