import concurrent.futures
import math
import time

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def main_async():
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    stop_time = time.time()
    time_taken = stop_time - start_time
    print(time_taken)

def main():
    start_time = time.time()
    for number in PRIMES:
        print('%d is prime: %s' % (number, is_prime(number)))
    stop_time = time.time()
    time_taken = stop_time - start_time
    print(time_taken)

if __name__ == '__main__':
    main_async()
    main()