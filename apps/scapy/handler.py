#-*- coding:utf-8 -*-
from ZhihuiSMB.apps.base.handler import APIHandler,MultiStandardHandler
from ZhihuiSMB.apps.scapy.libs import *

class GetBaoWuNewsHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private=False
    def get(self):
        news = get_pretty_news()
        self.result["data"]=news
        self.finish(self.result)

class GetBaoWuPriceHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private = False

    def get(self):
        data = get_shareprice()
        company = get_pricedata()
        table = get_pricetable(data, company)
        self.result["data"]=table
        self.finish(self.result)

class GetShouGangeHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private = False

    def get(self):
        news=get_detail_shougang_news()
        self.result["data"]=news
        self.finish(self.result)

class GetWeatherXuanhuaHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private = False
    def get(self):
        weather_xuanhua  = get_weather()
        self.result["data"]=weather_xuanhua
        self.finish(self.result)

class GetCctvNewsHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private = False
    def get(self):
        cctv_mainnews  = get_cctv_mainnews()
        self.result["data"]=cctv_mainnews
        self.finish(self.result)

class GetYangshengHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private = False
    def get(self):
        yangsheng_news  = get_yangsheng_news()
        self.result["data"]=yangsheng_news
        self.finish(self.result)

class GetJianfeiHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private = False
    def get(self):
        jianfei_news  = get_jianfei_news()
        self.result["data"]=jianfei_news
        self.finish(self.result)

class GetChufangHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    def get(self):
        chufang_news  = get_chufang_news()
        self.result["data"]=chufang_news
        self.finish(self.result)

class GetDetailNewsHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private = False
    def get(self):
        url=self.get_argument("url")
        result = get_detail_news(url)
        # self.result["data"]={"text_news":result[0],"img_news":result[1]}
        self.result["data"]=result
        self.finish(self.result)

class GetnuaaXyxjHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private=False
    def get(self):
        self.result["data"] = get_nuaa_xyxj()
        self.finish(self.result)

class GetnuaaXwzpHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private=False
    def get(self):
        self.result["data"] = get_nuaa_xwzp()
        self.finish(self.result)

class GetnuaaZphHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private = False
    def get(self):
        self.result["data"] = get_nuaa_zph()
        self.finish(self.result)

class GetNjWeatherHandler(MultiStandardHandler):
    _model = "scapy.ScapyModel"
    enable_methods = ["get"]
    private = False
    def get(self):
        self.result["data"] = get_nanjing_weather()
        self.finish(self.result)




handlers=[
    (r"/baowu/news",GetBaoWuNewsHandler),
    (r"/baowu/price",GetBaoWuPriceHandler),
    (r"/shougang/news",GetShouGangeHandler),
    (r"/weather",GetWeatherXuanhuaHandler),
    (r"/cctv_news",GetCctvNewsHandler),
    (r"/yangsheng_news",GetYangshengHandler),
    (r"/jianfei_news",GetJianfeiHandler),
    (r"/chufang_news",GetChufangHandler),
    (r"/detail_news",GetDetailNewsHandler),
    (r"/nuaa_xyxj",GetnuaaXyxjHandler),
    (r"/nuaa_xwzp",GetnuaaXwzpHandler),
    (r"/nuaa_zph",GetnuaaZphHandler),
    (r"/njweather",GetNjWeatherHandler),
]