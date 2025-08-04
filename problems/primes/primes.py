import math


class Primes:

    def generate_primes(self, number_of_primes):
        result = [2]
        current_prime = 2
        for _ in range(1, number_of_primes):
            next_prime = self.find_next_prime(current_prime)
            result.append(next_prime)
            current_prime = next_prime

        return result

    def find_next_prime(self, current_prime):
        if current_prime == 2:
            return 3

        next_candidate = current_prime + 2
        while True:
            if self.is_prime(next_candidate):
                return next_candidate
            else:
                next_candidate += 1

    def is_prime(self, number):
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False

        return True
