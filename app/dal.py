from connection import collection
from pprint import pprint
# from app.connection import collection


def respone_builder(documents):
    response = []
    for document in documents:
        response.append(document)
    return response


def get_engineering_high_salary_employees():
    query = {'salary':{'$gt': 65000},
             'job_role.department': 'Engineering'}


    projection = {
        '_id': 0, 'employee_id': 1,'name': 1,'salary': 1
    }

    documents = collection.find(query, projection)
    response = respone_builder(documents)
    return response
    


def get_employees_by_age_and_role():
    query = {
        'age':{'$gte': 30, '$lte': 45},
        'job_role.title': {'$in': ['Specialist','Engineer']}
    }

    documents = collection.find(query)
    response = respone_builder(documents)
    return response


def get_top_seniority_employees_excluding_hr():
    query = {
        'job_role.department': {'$ne': 'HR'}
    }

    documents = collection.find(query).sort({"years_at_company": -1}).limit(7)
    response = respone_builder(documents)
    return response


def get_employees_by_age_or_seniority():
    query = {
        '$or' :[ 
            {'age': {'$gt': 50}},
        {'years_at_company':{'$lt': 3}}
        ]
    }

    projection = {
        '_id': 0, 'employee_id': 1,'name': 1,'age': 1,'years_at_company': 1
    }

    documents = collection.find(query, projection)
    response = respone_builder(documents)
    return response


print(get_employees_by_age_or_seniority())

