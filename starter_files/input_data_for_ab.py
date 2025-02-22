import json

data = {
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
}
input_data = json.dumps(data)

with open("data.json", "w") as _f:
    _f.write(input_data)