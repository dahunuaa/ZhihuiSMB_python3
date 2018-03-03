# -*- coding:utf-8 -*-
from ZhihuiSMB.apps.base.handler import MultiStandardHandler
from ZhihuiSMB.apps.weather.lib import *

class Citycode2Mongo(MultiStandardHandler):
    _model = "weather.WeatherModel"
    enable_methods = ["get"]
    def get(self):
        weather_list = []
        with open('C:/Users/Administrator/Desktop/车联网/weather_city_code.txt') as f:
            for line in f.readlines():
                weather_list.append(line.strip().split("="))
        final_weather_list = []
        for i in weather_list:
            if len(i) > 1:
                final_weather_list.append(i)

        self.model.city2mongo(final_weather_list)

class GetCityWeather(MultiStandardHandler):
    _model = "weather.WeatherModel"
    enable_methods = ["get"]

    def get(self):
        cityname = self.get_argument("city")
        city = self.model.getcodefromname(cityname)
        city_code=city["code"]
        self.result["data"]=get_weather(city_code)
        self.finish(self.result)

class GetLifeIndex(MultiStandardHandler):
    _model = "weather.WeatherModel"
    enable_methods = ["get"]
    def get(self):
        cityname=self.get_argument("city")
        city = self.model.getcodefromname(cityname)
        city_code = city["code"]
        self.result["data"] = get_lifeindex(city_code)
        self.finish(self.result)

handlers =[
    (r"/city2mongo",Citycode2Mongo),
    (r"/get_weather",GetCityWeather),
    (r"/get_lifeindex",GetLifeIndex),
]