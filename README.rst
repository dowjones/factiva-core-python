Dow Jones Factiva Core Python Library
#####################################

Python package with root definitions and dictionaries, to support other functional packages.

* **APIKeyUser**: Represents an API user defined as a user key only (no O-Auth).

Installation
============
To install this library, run the following commands. However, this library will be installed as a dependency of other Factiva or Dow Jones packages.

.. code-block::

    $ pip install factiva-core

Using Library services
======================
Create an API-Key user instance, and retrieve a summary of current allowances and use.

.. code-block::Python

    from factiva.core import APIKeyUser
    my_user = APIKeyUser(api_key='abc123abc123abc123abc123', get_info=True)
    if(my_user.remaining_snapshots > 0):
        # Code to capture a snapshot

