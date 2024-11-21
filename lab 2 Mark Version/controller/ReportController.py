import datetime
from model.DefaultReport import DefaultReport
from model.Admin import Admin


class ReportController:
    def __init__(self):
        self.reports = []

    def add_report(self, report: DefaultReport):
        self.reports.append(report)
        print(f"Report {report.get_num_of_report()} added successfully.")

    def remove_report(self, report_num: int):
        for report in self.reports:
            if report.get_num_of_report() == report_num:
                self.reports.remove(report)
                print(f"Report {report_num} removed successfully.")
                return True
        print(f"Report {report_num} not found.")
        return False

    def get_report_by_number(self, report_num: int):
        for report in self.reports:
            if report.get_num_of_report() == report_num:
                return report
        print(f"Report {report_num} not found.")
        return None

    def update_report_admin(self, report_num: int, new_admin: Admin):
        report = self.get_report_by_number(report_num)
        if report:
            report.set_admin(new_admin)
            print(f"Admin updated for Report {report_num}.")
            return True
        return False

    def list_reports(self):
        return self.reports

    def display_report_details(self, report_num: int):
        report = self.get_report_by_number(report_num)
        if report:
            print(f"Report Number: {report.get_num_of_report()}")
            print(f"Admin: {report.get_admin()}")
            print(f"Metrics: {report.get_metrics()}")
            print(f"Creation Time: {report.get_creating_time()}")
            print(f"Creation Date: {report.get_creating_date()}")
        else:
            print(f"Report {report_num} not found.")

    def filter_reports_by_admin(self, admin: Admin):
        return [report for report in self.reports if report.get_admin() == admin]

    def filter_reports_by_date(self, date: datetime.date):
        return [report for report in self.reports if report.get_creating_date() == date]
