from django.shortcuts import render

import pandas as pd
from django.http import JsonResponse
from .models import MonthlyConsumption
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
import json

from .models import User

some_salt = 'some_salt'


def energy(request):
    allValues = list(MonthlyConsumption.objects.all().values())

    graphVals = {}
    for val in allValues:
        
        graphVals[val["field"]]= {
                "labels": [x for x in val.keys() if x not in ["id", "field"]],
                "data": [val[x] for x in val.keys() if x not in ["id", "field"]],
                "graphLabel": [val[x] for x in val.keys() if x in ["field"]][0]
            }
        graphVals

    return JsonResponse({"vals": graphVals})


@csrf_exempt
def login(request):
    data = json.loads(request.body)
    password = data['password']
    email = data['email']

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({"message": "User not found", "status":500})

    if check_password(password, user.password):
        return JsonResponse({"message": "User logged in"})
    else:
        return JsonResponse({"message": "Incorrect password", "status":500})


@csrf_exempt
def register(request):
    data = json.loads(request.body)
    email = data.get('email')
    raw_password = data.get('password')

    # Hash the password
    hashed_password = make_password(raw_password, salt="my_salt")

    # Create a new user with hashed password
    try:
        user = User.objects.create(
            email=email, password=hashed_password, preferences={})
    except Exception as e:
        return JsonResponse({"message": "User already exists", "status": 500})
    return JsonResponse({"message": "User registered"})


@csrf_exempt
def upload_excel(request):
    if request.method == 'POST':
        # Read the Excel file using pandas
        df = pd.read_csv(
            "vara/Factory environmental test data.csv", index_col=False)

        # Iterate over rows and save data to the database
        for index, row in df.iterrows():
            print(row)
            MonthlyConsumption.objects.create(
                field=row["Unnamed: 0"],
                jan=row["Jan 2023"],
                feb=row["Feb 2023"],
                march=row["March 2023"],
                april=row["April 2023"],
                may=row["May 2023"],
                june=row["June 2023"],
                july=row["July 2023"],
                august=row["August 2023"],
                sept=row["September 2023"],
                oct=row["October 2023"],
                nov=row["November 2023"],
                dec=row["December 2023"]
            )

        return JsonResponse({'message': 'Data uploaded successfully'})
    else:
        return JsonResponse({'error': 'Please provide a file'}, status=400)
