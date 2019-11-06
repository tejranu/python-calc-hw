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

        self.result = sum_value / number_count
        # then return that value
        return self.result

    def median(self, number_list):
        # first sort the list
        number_list = list(number_list)
        number_list.sort()

        # take the list and get the value at the middle of the number list
        if len(number_list) % 2 is not 0:
            middle_val_index = int(len(number_list) / 2)

            middle_val = number_list[middle_val_index]

            self.result = middle_val
        else:
            # if the number count of the list is even, take the middle two numbers... add them and divide by 2
            middle_val_index = int(len(number_list) / 2)
            after_middle_index = middle_val_index + 1

            self.result = (float(number_list[middle_val_index]) + float(number_list[after_middle_index])) / 2

        return self.result

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




