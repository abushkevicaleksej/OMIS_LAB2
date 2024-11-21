from model.Report import Report


class SimplyReportHistory:
    def __init__(self, number: int, reports: [Report]):
        self.__num_of_chosen_metrics = number
        self.__reports = reports

    def get_num_of_chosen_metrics(self):
        return self.__num_of_chosen_metrics

    def get_numbers_of_reports(self):
        number_list = []
        for report in self.__reports:
            number_list.append(self.__reports[report].get_num_of_report())
        return number_list



