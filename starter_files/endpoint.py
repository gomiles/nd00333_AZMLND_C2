import requests
import json
import os


scoring_uri = 'http://e418e45f-0527-4a31-988a-ba09a9f283e1.westeurope.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = os.getenv('APIKEY')

# Two sets of data to score, so we get two results back
data = [{
    "Inputs": {
        "data": [
            {
                "age": 0,
                "marital": 0,
                "default": 0,
                "housing": 0,
                "loan": 0,
                "month": 0,
                "day_of_week": 0,
                "duration": 0,
                "campaign": 0,
                "pdays": 0,
                "previous": 0,
                "poutcome": 0,
                "emp.var.rate": 0,
                "cons.price.idx": 0,
                "cons.conf.idx": 0,
                "euribor3m": 0,
                "nr.employed": 0,
                "job_admin.": 0,
                "job_blue-collar": 0,
                "job_entrepreneur": 0,
                "job_housemaid": 0,
                "job_management": 0,
                "job_retired": 0,
                "job_self-employed": 0,
                "job_services": 0,
                "job_student": 0,
                "job_technician": 0,
                "job_unemployed": 0,
                "job_unknown": 0,
                "contact_cellular": 0,
                "contact_telephone": 0,
                "education_basic.4y": 0,
                "education_basic.6y": 0,
                "education_basic.9y": 0,
                "education_high.school": 0,
                "education_illiterate": 0,
                "education_professional.course": 0,
                "education_university.degree": 0,
                "education_unknown": 0
            }
        ]
    },
    "GlobalParameters": {
        "method": "predict"
    }
}, {
    "Inputs": {
        "data": [
            {
                "age": 0,
                "marital": 0,
                "default": 0,
                "housing": 0,
                "loan": 0,
                "month": 0,
                "day_of_week": 0,
                "duration": 1000,
                "campaign": 0,
                "pdays": 0,
                "previous": 0,
                "poutcome": 0,
                "emp.var.rate": 0,
                "cons.price.idx": 0,
                "cons.conf.idx": 0,
                "euribor3m": 0,
                "nr.employed": 0,
                "job_admin.": 0,
                "job_blue-collar": 0,
                "job_entrepreneur": 0,
                "job_housemaid": 0,
                "job_management": 0,
                "job_retired": 0,
                "job_self-employed": 0,
                "job_services": 0,
                "job_student": 0,
                "job_technician": 0,
                "job_unemployed": 0,
                "job_unknown": 0,
                "contact_cellular": 0,
                "contact_telephone": 0,
                "education_basic.4y": 0,
                "education_basic.6y": 0,
                "education_basic.9y": 0,
                "education_high.school": 0,
                "education_illiterate": 0,
                "education_professional.course": 0,
                "education_university.degree": 0,
                "education_unknown": 0
            }
        ]
    },
    "GlobalParameters": {
        "method": "predict"
    }
}]
# Convert to JSON string
input_data = [json.dumps(data_point) for data_point in data]

# Set the content type
headers = {'Content-Type': 'application/json'}
# Add authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
for input_point in input_data:
    print("Sending request")
    resp = requests.post(scoring_uri, input_point, headers=headers)
    print(resp)
    print(resp.json())
    print("")

