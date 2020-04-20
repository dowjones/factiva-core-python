Dow Jones Factiva Core Python Library
#####################################

Python package with root definitions and dictionaries, to support other functional packages.

* **APIKeyUser**: Represents an API user defined as a user key only (no O-Auth).
* **Dicts**: Module that contains mulitple dictionaries for data combination or better human-reading.

Installation
============
To install this library, run the following commands. However, this library will be installed as a dependency of other Factiva or Dow Jones packages.

.. code-block::

    $ pip install --upgrade factiva-core

Using Library services
======================
Quick examples that show how to use the included services.

Creating a User Instance and Getting its Status
-----------------------------------------------
Create an API-Key user instance, and retrieve a summary of current allowances and use.

.. code-block:: python

    from factiva.core import APIKeyUser
    my_user = APIKeyUser(api_key='abcd1234abcd1234abcd1234abcd1234', request_info=True)
    if(my_user.remaining_extractions > 0):
        # Code to capture a snapshot

Loading Factiva Industry Hierarchy
----------------------------------
Loads the Industry hierarchy dataset which, among others, contain the Industry Factiva Code.

.. code-block:: python

    from factiva.core import dicts
    ih = dicts.industries_hierarchy()
    ih.head()

