# -*- coding:utf-8 -*-
from urllib import request
import re
from bs4 import BeautifulSoup

def get_weather(city_code):
    url = "http://www.weather.com.cn/weather/"+city_code+".shtml"
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    content_html = soup.find("ul",{"class":"t clearfix"})
    detail_day = content_html.findAll("h1")
    detail_wea = content_html.findAll("p",{"class":"wea"})

    tem_pretty = content_html.findAll("p",{"class":"tem"})
    detail_tem_pretty=[]
    for i in tem_pretty:
        try:
            detail_tem_pretty.append([i.find("span").text,i.find("i").text])
        except:
            detail_tem_pretty.append([i.find("i").text])
    detail_wins=content_html.findAll("i")
    weather=[]
    for i in range(0,3):
        weather.append([detail_day[i].text,detail_wea[i].text,detail_tem_pretty[i],detail_wins[2*i+1].text])
        #返回的分别是日期、天气、气温、风力
    print(weather)
    return weather


def get_lifeindex(city_code):
    url = "http://www.weather.com.cn/weather/"+city_code+".shtml"
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    content_html = soup.find("div",{"class":"hide show"})
    shzs = content_html.findAll("li")
    life_index=[]
    for i in shzs:
        life_index.append([i.find("em").text,i.find("span").text,i.find("p").text])
    return life_index

# get_weather("101010100")




