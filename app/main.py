from fastapi import FastAPI, Request, Response
from pymongo import MongoClient

import json
import os
import requests


app = FastAPI()

mongo_user = os.getenv("MONGO_USER")
mongo_pass = os.getenv("MONGO_PASS")
mongo_host = os.getenv("MONGO_HOST")
mongo_port = os.getenv("MONGO_PORT")
mongo_db = os.getenv("MONGO_DB")
appid = os.getenv("APPID")
cnt_days= os.getenv("CNT_DAYS")

client = MongoClient(f"mongodb://{mongo_user}:{mongo_pass}@{mongo_host}:{mongo_port}/{mongo_db}?authSource=admin")
db = client[mongo_db]

@app.get("/")
def read_root():
    return {"Status": "Online"}

@app.get("/city/{city_name}")
def read_root(city_name: str, request: Request):
    try:
        geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={appid}'
        geolocation = requests.get(geo_url).json()
        forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={geolocation[0]["lat"]}&lon={geolocation[0]["lon"]}&cnt={cnt_days}&appid={appid}'
        response = requests.get(forecast_url).json()
        db["external_data"].insert_one({"data": response})
        return response
    except:
        return Response(content=json.dumps({"Error": "Please, inform a valid city name."}), status_code=400)