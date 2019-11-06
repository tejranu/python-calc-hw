from src.statistics.StatisticsAbstract import StatisticsAbstract


class Statistics(StatisticsAbstract):

    result = 0

    def population_mean(self, number_list):
        # population mean formula:
        number_list = list(number_list)
        sum_value = 0

        for x in number_list:
            sum_value = sum(number_list)

        # take the sum of the items and then divide it by the number of items
        number_count = len(number_list)

        pop_mean = sum_value / number_count
        # then return that value
        return pop_mean

    def median(self, number_list):
        pass

    def mode(self):
        pass

    def pop_standard_deviation(self):
        pass

    def variance_pop_proportion(self):
        pass

    def zscore(self):
        pass

    def standardized_score(self):
        pass

    def population_corre_coefficient(self):
        pass

    def confidence_interval(self):
        pass

    def population_variance(self):
        pass

    def p_value(self):
        pass

    def proportion(self):
        pass

    def sample_mean(self):
        pass

    def sample_standard_deviation(self):
        pass

    def variance_sample_proportion(self):
        pass




