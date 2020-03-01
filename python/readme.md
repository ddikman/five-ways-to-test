# five-ways-to-test python

## setup

Uses [pipenv](https://docs.python-guide.org/dev/virtualenvs/) to manage dependencies required.

```shell script
pipenv install
```

## running tests

Each sub project (way of testing) contains three files:
- `practice_{project_name}.py` | contains the practice for you to implement
- `example_{project_name}.py` | contains an example implementation to help if you get stuck
- `test_{project_name}.py` | contains example tests for you to use or implement

You can run the tests by:

```shell script
pipenv run pytest --cov=. --cov-report html
```

Or, to have the runner continously re-run all tests:

```shell script
pipenv run pytest-watch
```

## exercises

Each project shows a method, so follow these instructions to try it out.

### tdd

For TDD we:

1. Write the test
2. Make it pass (by writing as little code as possible)
3. Refactor to make it clean

This practice starts in [test_tdd.py](tdd/test_tdd.py) as we are starting with the test, so open that file and check the instructions there.
