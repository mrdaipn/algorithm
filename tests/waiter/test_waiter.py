from problems.primes.primes import Primes
from problems.waiter.waiter import Waiter


class TestWaiter:

    def test_waiter_with_2_3_4_5_6_7_and_q_3_should_return_2_4_6_3_5_7(self):
        waiter = Waiter(prime_producer=Primes())
        assert [2, 4, 6, 3, 5, 7] == waiter([2, 3, 4, 5, 6, 7], 3)
