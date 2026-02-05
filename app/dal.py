from app.connection import collection
from pprint import pprint


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

    documents = collection.find(query, projection).limit(5)
    response = respone_builder(documents)
    return response
    


def get_employees_by_age_and_role():
    pass


# print(get_engineering_high_salary_employees())

