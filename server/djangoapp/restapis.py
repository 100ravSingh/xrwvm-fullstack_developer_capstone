# Uncomment the imports below before you add the function code
from django.http import JsonResponse
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

backend_url = os.getenv(
    'backend_url',
    default="https://humble-disco-4vq5x95w4q6hqrw7-3030.app.github.dev")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url', 
    default=
    "https://sentianalyzer.24c21jy4pklt.us-south.codeengine.appdomain.cloud")


def get_request(endpoint, **kwargs):
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        # If any error occurs
        print(f"Network exception occurred: {e}")


# Update the `get_dealerships` render list of dealerships all by default,
# particular state if state is passed


def get_dealerships(request, state="All"):
    if (state == "All"):
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/"+state
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})


def add_review(request):
    if (request.user.is_anonymous is False):
        data = json.loads(request.body)
        try:
            post_review(data)
            return JsonResponse({"status": 200})
        except Exception as e:
            print(f"error is : {e}")
            return JsonResponse({
                "status": 401,
                "message": "Error in posting review"
                })
    else:
        return JsonResponse({
            "status": 403,
            "message": "Unauthorized"
            })


def analyze_review_sentiments(text):
    try:
        request_url = sentiment_analyzer_url.rstrip("/") + "/analyze/" + text
        print("Calling sentiment analyzer:", request_url)

        response = requests.get(request_url, timeout=30)

        if response.status_code == 200:
            return response.json()
        else:
            print("Sentiment service error:", response.status_code)
            return None

    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        return None


def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Network exception occurred : {err}")
