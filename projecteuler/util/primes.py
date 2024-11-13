import numpy as np
import math


def sieve(n: int) -> list[int]:
    nums = np.array(range(1, n + 1), dtype=np.bool_)

    for curr in range(2, math.floor(np.sqrt(n)) + 1):
        if nums[curr]:
            for factor in [
                curr**2 + curr * i for i in range(n + 1) if curr ** 2 + curr * i < n
            ]:

                nums[factor] = False

    return list(
        map(
            lambda x: x[0],
            filter(
                lambda x: x[1],
                map(lambda i: (i[0], i[1]), enumerate(nums)),
            ),
        )
    )[2:]


def factorize(n: int, primes: list[int]):
    factors = {}
    current = n

    for prime in primes:
        while current % prime == 0:
            current = int(current / prime)
            if factors.get(prime) is not None:
                factors[prime] += 1
            else:
                factors[prime] = 1

    return factors
