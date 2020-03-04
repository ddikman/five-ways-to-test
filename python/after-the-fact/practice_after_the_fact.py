def calculate_total(articles):
  sum = 0
  total = 0
  for article in articles:
    sum = sum + article
    total = total + article
    if sum < 0:
      sum = 0

  if sum < 0:
      sum = 0

  return sum

class InvalidNumberError(Exception):
  pass
