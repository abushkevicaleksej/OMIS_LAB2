class DefaultMetrics:
    def __init__(self, type_of_metrics: str, metrics_info: str):
        self.__type_of_metrics = type_of_metrics
        self.__metrics_info = metrics_info

    def set_metrics_type(self, new_metrics):
        self.__type_of_metrics = new_metrics

    def show_info(self):
        return self.__metrics_info

