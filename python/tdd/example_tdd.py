def is_prime(number):
  if number < 0:
    raise InvalidNumberError
  elif number < 2:
      return False

  divisor = 2
  for i in range(divisor, number):
    if (number % i) == 0:
        return False

  return True

class InvalidNumberError(Exception):
  pass
