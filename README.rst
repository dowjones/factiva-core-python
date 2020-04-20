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
    aku = APIKeyUser(api_key='abcd1234abcd1234abcd1234abcd1234', request_info=True)
    print(aku)

.. code-block::

    <class 'factiva.core.apikeyuser.APIKeyUser'>
      api_key = ****************************1234
      account_name = Demo Account
      account_type = account_with_limits
      active_products = Snapshots
      max_allowed_concurrent_extractions = 2
      max_allowed_extracted_documents = 100000
      max_allowed_extractions = 10
      total_downloaded_bytes = 12345678
      total_extracted_documents = 5500
      total_extractions = 2
      total_stream_subscriptions = 2
      total_stream_topics = 1
      remaining_documents = 94500
      remaining_extractions = 8

Loading Factiva Industry Hierarchy
----------------------------------
Loads the Industry hierarchy dataset which, among others, contain the Industry Factiva Code.

.. code-block:: python

    from factiva.core import dicts
    ih = dicts.industries_hierarchy()
    ih.head()

.. code-block::

    ind_fcode            name   parent
    0   indroot  *DJ Industries
    1        i0     Agriculture  indroot
    2    i01001         Farming       i0
    3    i03001     Aquaculture   i01001
    4  i0100144   Cocoa Growing   i01001
