# -*- coding:utf-8 -*-
from ZhihuiSMB.apps.base.handler import MultiStandardHandler,TokenHandler
from ZhihuiSMB.libs.oauthlib import get_provider
import ZhihuiSMB.libs.utils as utils

class PcPtosReportHandler(MultiStandardHandler,TokenHandler):
    _model = "report.ReportModel"
    enable_methods = ["get"]

    def get(self):
        time_desc = self.get_argument("time_desc", "all")
        start_time = self.get_argument("start_time",None)
        end_time = self.get_argument("end_time",None)

        result = self.model.ptos_report(time_desc,start_time,end_time)[0]
        data = self.model.ptos_report(time_desc,start_time,end_time)[1]
        file_names = result["filename"]
        file_paths = result["file_path"]
        # self.result["data"]={"download_path":result["download_path"],"file_name":file_names,"file_path":file_paths,"report_data":data}
        # self.finish(self.result)

        #以下注释内容可以直接在浏览器下载该文件
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename=' + file_names[0])
        with open(file_paths[0], 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                self.write(data)
        self.finish(self.result)

class PcInforshareReportHandler(MultiStandardHandler,TokenHandler):
    _model = "report.ReportModel"
    enable_methods = ["get"]

    def get(self):
        time_desc = self.get_argument("time_desc", "all")
        start_time = self.get_argument("start_time", None)
        end_time = self.get_argument("end_time", None)
        result = self.model.inforshare_report(time_desc,start_time,end_time)[0]
        data = self.model.inforshare_report(time_desc, start_time, end_time)[1]
        file_names = result["filename"]
        file_paths = result["file_path"]
        # self.result["data"]={"download_path":result["download_path"],"file_name":file_names,"file_path":file_paths,"report_data":data}
        # self.finish(self.result)
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', 'attachment; filename=' + file_names[0])
        with open(file_paths[0], 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                self.write(data)
        self.finish(self.result)

handlers = [
    (r"/pc/ptos",PcPtosReportHandler,get_provider("report_admin")),
    (r"/pc/inforshare",PcInforshareReportHandler,get_provider("report_admin")),
]