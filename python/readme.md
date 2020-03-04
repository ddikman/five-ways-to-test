# five-ways-to-test python

The project contains four folders for describing different testing methods. Under `exercises` below, you'll find details on how to approach each of these.

## running tests

The project uses [pipenv](https://docs.python-guide.org/dev/virtualenvs/) to manage dependencies required, so before anything else:

```shell script
pipenv install
```

Run tests by:

```shell script
pipenv run pytest --cov-report=html --cov=tdd --cov=learning --cov=coverage --cov=after-the-fact
```

Or, to have the runner continously re-run all tests:

```shell script
pipenv run pytest-watch
```

## exercises

Each project shows a method, so follow these instructions to try it out.

### tdd

For TDD we:

1. Write the test
2. Make it pass (by writing as little code as possible)
3. Refactor to make it clean

This practice starts in [test_tdd.py](tdd/test_tdd.py) as we are starting with the test, so open that file and check the instructions there.

### learning

The learning tests are about using a test suite to drive your development, allowing you to run the code without having to run your entire app. In this example I'm using an open book api and for practice you can use the [Chuck Norris joke API](http://www.icndb.com/api/).

Have a look at the [test_learning.py](learning/test_learning.py) for how I step by step figure out how the API works. Then have a go for yourself in [practice_learning.py](learning/practice_learning.py) using [test_practice_learning.py](learning/test_practice_learning.py) as runner.

### coverage

In this example, I have put together what might be the worst email validator ever. It has a bug you'll need to fix (crashes on null values) and probably it can do with some refactoring.

But first, add in coverage! Add in tests to cover all the lines of code and do so trying to figure out what kind of test cases the code supports. Once you have that in place, you can add a test to show the issue and fix it.

### after-the-fact

In the `after-the-fact` exercise we're doing something similar like in the coverage example but with the difference that we know `what` we want to do but the `why` might not be right. So instead of coverage, we focus on getting tests for the behaviour and then adjust the functionality to match behaviour.

Start in the [after-the-fact/test_practice_after_the_fact.py] and implement tests based on expected behaviour and then fix the existing code to match.

## troublshooting

The project is written using [VSCode](https://code.visualstudio.com/).

1. Make sure you open the `python` project and not the root folder, otherwise VSCode might not find the pipenv file
2. Select your [environment](https://code.visualstudio.com/docs/python/environments)
3. Troubleshoot [linting setup](https://donjayamanne.github.io/pythonVSCodeDocs/docs/troubleshooting_linting/).

Also, without creating a virtual environment, vscode will default to the global installation of python. To adress this, run:

```shell script
python -m venv .venv
```

Read more in [environments for vscode](https://code.visualstudio.com/docs/python/environments).
