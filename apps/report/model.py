# -*- coding:utf-8 -*-
import ZhihuiSMB.apps.base.model as model
from ZhihuiSMB.libs.datatypelib import *
import ZhihuiSMB.report as report_util#引入这个就报404
import ZhihuiSMB.libs.utils as utils

class ReportModel(model.StandCURDModel):
    _coll_name = "report"
    _columns = []

    def ptos_report(self,time_desc,start_time,end_time):
        ptos_coll = model.BaseModel.get_model("ptos.PtosModel").get_coll()
        comment_coll = model.BaseModel.get_model("comment.CommentHandler").get_coll()
        query_params= report_util.change_time(time_desc,start_time,end_time)
        ptos = ptos_coll.find(query_params).sort("add_time", -1)
        ptos_data=utils.dump(ptos)#注意此处需要先将查询出来的类型转换成json类型
        report_china_name = "FAQs"#windows上面目前路径有汉字的下载不好使
        namelist = [u'order','FAQ id','editor','title','category','add_time','content','images','finish_time','answer_result','result','answer','agree_amounts']
        fieldlist = []
        export_bus_list =[]
        for bus in ptos_data:
            export_bus_list.append({
                "ptos_order":bus["_id"],
                "ptos_author":bus["add_user_name"],
                "ptos_title":bus["title"],
                "category":bus["category"],
                "add_time":bus["add_time"],
                "content": bus["context"],
                "images":str(bus["images"]),
                "finish_time": bus["last_updated_time"],
                "answer_result": bus["result"],
            })
            comment_data=utils.dump(comment_coll.aggregate([
                                                {"$match": {"text_id":bus["_id"]}},
                                                # {"$group":{"_id":bus["_id"], }},

                                               {"$sort":{"like_amounts":-1},}
                                               ]))
            if comment_data:
                export_bus_list.append({
                    "answer": comment_data[0]['text'],
                    "agree_amounts": comment_data[0]['like_amounts'],
                })
            else:
                export_bus_list.append({
                    "answer": "",
                    "agree_amounts": "",
                })
        if len(export_bus_list)>0:
            fieldlist=['ptos_order','ptos_author','ptos_title','category','add_time','content','images','finish_time','answer_result','result',"answer","agree_amounts"]


        result = report_util.export_excel(report_china_name=[report_china_name],namelist=[namelist],result=[export_bus_list],fieldlist=[fieldlist])
        data = ptos_data
        return result,data

    def inforshare_report(self,time_desc,start_time,end_time):
        inforshare = model.BaseModel.get_model("inforshare.InforshareModel").get_coll()
        query_params = report_util.change_time(time_desc, start_time, end_time)
        inforshare = inforshare.find(query_params).sort("add_time", -1)
        inforshare_data=utils.dump(inforshare)#注意此处需要先将查询出来的类型转换成json类型
        report_china_name = "inforshare"#windows上面目前路径有汉字的下载不好使
        namelist = [u'infor_order','infor_id','editor','add_time','category','title','content','filename','file link','images link']
        fieldlist = []
        export_bus_list =[]
        for gather in inforshare_data:
            export_bus_list.append({
                "gather_order":gather["_id"],
                "add_user_name":gather["add_user_name"],
                "gather_title":gather["add_time"],
                "gather_address":gather["infor_type"],
                "gather_area":gather["infor_title"],
                "gather_oilfield":gather["infor_text"],
                "gather_text":gather["filename"],
                "add_time":gather["filepath"],
                "images":str(gather["images"]),
            })
        if len(export_bus_list)>0:
            fieldlist=['gather_order','add_user_name','gather_title','gather_address','gather_area','gather_oilfield','gather_text','add_time','images']

        result = report_util.export_excel(report_china_name=[report_china_name],namelist=[namelist],result=[export_bus_list],fieldlist=[fieldlist])
        data = inforshare_data
        return result,data









