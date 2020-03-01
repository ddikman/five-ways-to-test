# Instructions
# ------------
# The tests in here are already passing as an example.
# To try this yourself, comment the import of `example_tdd` and replace with the `practice_tdd`
# Then comment out all tests except for the first, run it and see it fail
# Then implement some functionality to pass it and one by one uncomment and make the other tests pass

# from practice_tdd import is_prime
from example_tdd import is_prime, InvalidNumberError

from pytest import raises
from random import randint
import timeit

def test_one_is_not_a_prime():
  assert is_prime(1) == False

def test_no_even_number_is_a_prime():
  even_number = randint(7, 20) * 2
  assert is_prime(even_number) == False

def test_zero_is_not_a_prime():
  assert is_prime(0) == False

def test_first_seven_primes():
  first_seven_primes = [2, 3, 5, 7, 11, 13, 17]
  for prime in first_seven_primes:
    assert is_prime(prime) == True

def test_throws_error_on_negative_numbers():
  with raises(InvalidNumberError):
    is_prime(-1)

def test_can_calculate_high_prime_number():
  prime_number_200 = 1223
  assert is_prime(prime_number_200) == True
