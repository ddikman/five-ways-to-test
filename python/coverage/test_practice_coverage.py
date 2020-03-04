from pratice_coverage import is_valid_company_email

# like below, add coverage for all lines in the code

company_domain = 'company.com'
def test_invalid_if_not_company_domain():
  assert is_valid_company_email('bob.jones@another.com') == False

def test_your_test():
  pass

# when all above tests are added, you can add in this test as well and fix the functionality, knowing you have not broken anything

# def test_is_not_valid_when_null():
#   assert is_valid_company_email(None) == False
