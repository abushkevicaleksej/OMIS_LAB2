from model.SimplyReportHistory import SimplyReportHistory


class ReportHistory(SimplyReportHistory):
    def get_time_marks_of_creating(self):
        time_list = []
        for report in self.__reports:
            time_list.append(self.__reports[report].get_creating_time())
        return time_list
