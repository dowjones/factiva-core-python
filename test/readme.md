# Test notes for the factiva-core Python package
General notes that describe the context the package is expected to be tested, and other considerations.

## Runtime
The environment is conditioned by the main dependencies: requests and pandas. As per the Pandas documentation, the preference is to use [Python version 3.7.1](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html#python-version-support) and above, and requests work with almost any version of Python.

The code has been writen using features like f-string which are available since Python 3.6, thus, that's the minimum supported version. As per Pandas guidelines, Python 3.7.1 or above is preferred.

## Pandas dependency
Although the big majority of actions can be performed using the requests library, dealing with some responses can be easier using Pandas. Additionally, in the near future the response of new endpoints, and even new version are expected to return a more structured response. The package factiva-pipelines also uses Pandas as the main data manipulation tool.

## Environment Variables
Before starting the test, set the following enviroment variables with values like this:
```
FACTIVA_USERKEY='abcd1234abcd1234abcd1234abcd1234'
FACTIVA_CLIENT_EMAIL='dummy-account@djproject.iam.gserviceaccount.com'
```
