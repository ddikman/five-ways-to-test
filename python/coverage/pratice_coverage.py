# this is a stupid implementation but it illustrates some easy code
def is_valid_company_email(email):
  if not email.lower().endswith('@company.com'):
    return False

  username = email.split('@')[0]

  if username.count('.') != 1:
    return False

  names = username.split('.')
  firstName = names[0]
  lastName = names[1]
  for letter in firstName:
    if not letter.isalpha():
      return False

  for letter in lastName:
    if not letter.isalpha():
      return False

  return True
