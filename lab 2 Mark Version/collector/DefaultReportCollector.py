from model.Metrics import Metrics
from model.Report import Report

class DefaultReportCollector:
    def __init__(self):
        pass

    def collect_report(self, report: Report):
        pass

    def add_metrics(self, report: Report, metrics: [Metrics]):
        pass