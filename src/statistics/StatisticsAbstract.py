from abc import ABC, abstractmethod
# abstract class to contain all methods to be implemented


class StatisticsAbstract(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def population_mean(self, number_list):
        pass

    @abstractmethod
    def median(self, number_list):
        pass

    @abstractmethod
    def mode(self, number_list):
        pass

    @abstractmethod
    def pop_standard_deviation(self, number_list):
        pass

    @abstractmethod
    def variance_pop_proportion(self, number_list):
        pass

    @abstractmethod
    def zscore(self):
        pass

    @abstractmethod
    def standardized_score(self):
        pass

    @abstractmethod
    def population_corre_coefficient(self):
        pass

    @abstractmethod
    def confidence_interval(self):
        pass

    @abstractmethod
    def population_variance(self):
        pass

    @abstractmethod
    def p_value(self, number_list):
        pass

    @abstractmethod
    def proportion(self, number_list):
        pass

    @abstractmethod
    def sample_mean(self, number_list):
        pass

    @abstractmethod
    def sample_standard_deviation(self, number_list):
        pass

    @abstractmethod
    def variance_sample_proportion(self, number_list):
        pass

