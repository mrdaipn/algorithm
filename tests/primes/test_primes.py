import pytest
from problems.primes.primes import Primes


class TestPrimes:

    @pytest.fixture()
    def primes(self):
        return Primes()

    def test_generate_1_prime_return_2(self, primes):
        assert [2] == primes.generate_primes(number_of_primes=1)

    def test_generate_2_primes_return_2_3(self, primes):
        assert [2, 3] == primes.generate_primes(number_of_primes=2)

    def test_generate_8_first_primes(self, primes):
        assert [2, 3, 5, 7, 11, 13, 17, 19] == primes.generate_primes(
            number_of_primes=8
        )
