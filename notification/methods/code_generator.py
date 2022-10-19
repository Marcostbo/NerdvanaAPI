from random import randint


class CodeGenerator:
    min_digits = 4
    max_digits = 8

    def generate_random_code(self, number_of_digits):
        if self.min_digits <= number_of_digits <= self.max_digits:
            return self._random_with_n_digits(n=number_of_digits)
        else:
            raise ValueError

    @staticmethod
    def _random_with_n_digits(n):
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        return randint(range_start, range_end)
