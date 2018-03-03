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
        ptosadd_coll = model.BaseModel.get_model("ptosadd.PtosaddModel").get_coll()
        query_params= report_util.change_time(time_desc,start_time,end_time)
        ptos = ptos_coll.find(query_params).sort("add_time", -1)
        ptos_data=utils.dump(ptos)#注意此处需要先将查询出来的类型转换成json类型
        report_china_name = "problemstosolution"#windows上面目前路径有汉字的下载不好使
        namelist = [u'序号','反馈单号','反馈人','反馈标题','指定人','分类','发起时间','期待解决时间','问题描述','图片地址','解答_时间','解答_正文','解答_图片地址','结果评价']
        fieldlist = []
        export_bus_list =[]
        for bus in ptos_data:
            export_bus_list.append({
                "ptos_order":bus["_id"],
                "ptos_author":bus["add_user_name"],
                "ptos_title":bus["title"],
                "to_name":bus["to_name"],
                "ptos_type":bus["category"],
                "add_time":bus["add_time"],
                "expect_time":bus["except_time"],
                "ptos_remark":bus["context"],
                "images":bus["images"],
            })
            ptosadd_data=ptosadd_coll.find_one({"ptos_id":bus["_id"]})

            if ptosadd_data:
                export_bus_list.append({
                    "answer_time": ptosadd_data["add_time"],
                    "answer_text": ptosadd_data["context"],
                    "answer_images": str(ptosadd_data["images"]),
                })
                export_bus_list.append({
                    "answer_result": bus["result"],
                })
            else:
                pass
        if len(export_bus_list)>0:
            fieldlist=['ptos_order','ptos_author','ptos_title','to_name','ptos_type','add_time','expect_time','ptos_remark','images','answer_time','answer_text','answer_images','answer_result']

        result = report_util.export_excel(report_china_name=[report_china_name],namelist=[namelist],result=[export_bus_list],fieldlist=[fieldlist])
        data = ptos_data
        return result,data

    def inforshare_report(self,time_desc,start_time,end_time):
        inforgather = model.BaseModel.get_model("inforshare.InforshareModel").get_coll()
        query_params = report_util.change_time(time_desc, start_time, end_time)
        inforgather = inforgather.find(query_params).sort("add_time", -1)
        inforgather_data=utils.dump(inforgather)#注意此处需要先将查询出来的类型转换成json类型
        report_china_name = "inforshare"#windows上面目前路径有汉字的下载不好使
        namelist = [u'序号','信息单号','发布人','发布时间','类别','标题','正文','文件名','文件地址','图片地址']
        fieldlist = []
        export_bus_list =[]
        for gather in inforgather_data:
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
        data = inforgather_data
        return result,data

    def inforguide_report(self,time_desc,start_time,end_time):
        inforguide = model.BaseModel.get_model("inforguide.InforguideModel").get_coll()
        query_params = report_util.change_time(time_desc, start_time, end_time)
        inforguide = inforguide.find(query_params).sort("add_time", -1)
        inforguide_data=utils.dump(inforguide)#注意此处需要先将查询出来的类型转换成json类型
        report_china_name = "inforguide"#windows上面目前路径有汉字的下载不好使
        namelist = [u'序号','单号','搜集人','标题','分类','内容','添加时间','最后修改时间','图片地址']
        fieldlist = []
        export_bus_list =[]
        for guide in inforguide_data:
            export_bus_list.append({
                "guide_order":guide["_id"],
                "add_user_name":guide["add_user_name"],
                "guide_title":guide["guide_title"],
                "guide_type":guide["guide_type"],
                "guide_text":guide["guide_text"],
                "add_time":guide["add_time"],
                "last_updated_time":guide["last_updated_time"],
                "images":str(guide["images"]) ,
            })
        if len(export_bus_list)>0:
            fieldlist=['guide_order','add_user_name','guide_title','guide_type','guide_text','add_time','last_updated_time','images']

        result = report_util.export_excel(report_china_name=[report_china_name],namelist=[namelist],result=[export_bus_list],fieldlist=[fieldlist])
        data = inforguide_data
        return result,data

    def notice_report(self,time_desc,start_time,end_time):
        notice = model.BaseModel.get_model("notice.NoticeModel").get_coll()
        query_params = report_util.change_time(time_desc, start_time, end_time)
        notice = notice.find(query_params).sort("add_time", -1)
        notice_data=utils.dump(notice)#注意此处需要先将查询出来的类型转换成json类型
        report_china_name = "notice"#windows上面目前路径有汉字的下载不好使
        namelist = [u'序号','单号','发布人','标题','内容','发布时间','最后修改时间']
        fieldlist = []
        export_bus_list =[]
        for notice in notice_data:
            export_bus_list.append({
                "notice_order":notice["_id"],
                "add_user_name":notice["add_user_name"],
                "notice_title":notice["notice_title"],
                "notice_text":notice["notice_text"],
                "add_time":notice["add_time"],
                "last_updated_time":notice["last_updated_time"],
            })
        if len(export_bus_list)>0:
            fieldlist=['notice_order','add_user_name','notice_title','notice_text','add_time','last_updated_time']

        result = report_util.export_excel(report_china_name=[report_china_name],namelist=[namelist],result=[export_bus_list],fieldlist=[fieldlist])
        data = notice_data
        return result,data






