from typing import List


class Waiter:

    def __init__(self, prime_producer):
        self.prime_producer = prime_producer

    def __call__(self, array: List, q: int):
        result = []
        primes = self.prime_producer.generate_primes(q)

        i = 0
        for _ in range(q):
            a = []
            b = []

            while array:
                current_element = array.pop()
                if current_element % primes[i] == 0:
                    b.append(current_element)
                else:
                    a.append(current_element)

            while b:
                result.append(b.pop())

            array = a
            i += 1
        while a:
            result.append(a.pop())

        return result
