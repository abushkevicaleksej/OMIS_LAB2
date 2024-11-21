from model.ReportHistory import ReportHistory


class HistoryController:
    def __init__(self):
        self.history = []

    def add_history(self, history: ReportHistory):
        self.history.append(history)
        print("History added successfully.")

    def get_all_histories(self):
        return self.history

    def get_report_numbers(self):
        report_numbers = []
        for history in self.history:
            report_numbers.extend(history.get_numbers_of_reports())
        return report_numbers

    def get_time_marks(self):
        time_marks = []
        for history in self.history:
            if isinstance(history, ReportHistory):
                time_marks.extend(history.get_time_marks_of_creating())
        return time_marks

    def display_history_details(self):
        for i, history in enumerate(self.history):
            print(f"History {i + 1}:")
            print(f"  Number of chosen metrics: {history.get_num_of_chosen_metrics()}")
            print(f"  Report numbers: {history.get_numbers_of_reports()}")
            if isinstance(history, ReportHistory):
                print(f"  Time marks: {history.get_time_marks_of_creating()}")
            print()
