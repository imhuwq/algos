# algos

A python3 code base of home brew algorithms and data structures.

## 1. Project Structure
```shell
.
├── data_structure            # the module including all data structure
├── htmlcov                   # test coverage report
├── .pre-commit-config.yaml   # config file of git pre-commit hook
├── README.md                 # the project readme file
|── requirements_dev.txt      # python package requirements for local dev
├── tests                     # the test codes
└── test.sh                   # trigger pytest
```

## 2. How to Setup
- 2.1 install python requirements
```shell
pip install -r requirements_dev.txt
```

- 2.2 install pre-commit hook
```shell
pre-commit install
```

This will install `pytest-check` hook which triggers pytest to run all test codes under `tests` directory.  
You can also run the tests manually with the shell script `./test.sh`. 
