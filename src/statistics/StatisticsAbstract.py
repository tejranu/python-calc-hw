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
    def mode(self):
        pass

    @abstractmethod
    def pop_standard_deviation(self):
        pass

    @abstractmethod
    def variance_pop_proportion(self):
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
    def p_value(self):
        pass

    @abstractmethod
    def proportion(self):
        pass

    @abstractmethod
    def sample_mean(self):
        pass

    @abstractmethod
    def sample_standard_deviation(self):
        pass

    @abstractmethod
    def variance_sample_proportion(self):
        pass





