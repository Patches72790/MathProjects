from util.primes import sieve, factorize


def sum_square_difference(n):
    def sum_of_squares():
        return sum(i**2 for i in range(1, n + 1))

    def square_of_sum():
        return ((n * (n + 1)) / 2) ** 2

    a = sum_of_squares()
    b = square_of_sum()

    print(a, b)
    return square_of_sum() - sum_of_squares()


def largest_prime_factor(n: int, num_primes: int):
    primes = sieve(num_primes)
    return factorize(n, primes[2:])


def largest_palindrome_product():

    pass


def main():
    # print(sum_square_difference(100))
    # print(smallest_multiple(10))
    # print(largest_prime_factor(600851475143, 10000))

    primes = sieve(1000000)
    print(primes, len(primes))

    print(f"10001st prime = {primes[10000]}")


if __name__ == "__main__":
    main()
