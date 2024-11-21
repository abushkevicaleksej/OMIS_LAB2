from model.Report import Report
from model.Admin import Admin
from model.Metrics import Metrics

class CreateReportManager:
    def __init__(self, admin: Admin, report: Report):
        self.__admin = admin
        self.__report = report

    def start_report_processing(self, admin: Admin, report: Report):
        pass

    def finish_report_processing(self) -> Report:
        pass

    def add_metrics(self, metrics: [Metrics]):
        pass

