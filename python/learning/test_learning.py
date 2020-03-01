from example_learning import example_parse_some_data, example_get_some_json, example_get_author, example_find_first_author

# first test, just to see what data we get
def test_print_output():
  response = example_parse_some_data()
  print(dir(response))
  # failing this test prints me properties of the class, showing me I have a 200 response with a `json` method
  # assert False

# second test, shows me content is in
def test_print_json():
  json = example_get_some_json()
  print(json)
  # uncommenting this will give me the full json printout
  # assert False

# third test, try to get author data out (getting closer to what I want to achieve)
# now starting to look more like TDD, I set the expectation first then modify the method
def test_get_author():
  author = example_get_author()
  assert author == "Robert C. Martin"

# forth test, now I know how to pull data out of it, I can parameterise and start building what I want
def test_returns_first_author_of_first_match():
  author = example_find_first_author("Clean code")
  assert author == "Robert C. Martin"
