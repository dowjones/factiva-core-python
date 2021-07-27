Dow Jones Factiva Core Python Library
#####################################
.. image:: https://github.com/dowjones/factiva-core-python/actions/workflows/master_test_publish.yml/badge.svg
.. image:: https://readthedocs.org/projects/factiva-core-python/badge/?version=latest :target: https://factiva-core-python.readthedocs.io/en/latest/?badge=latest :alt: Documentation Status

Python package with root definitions and dictionaries, to support other functional packages. Get more details in the `official documentation <https://factiva-core-python.readthedocs.io/>`_

* **UserKey**: Represents an API user defined as a user key only (no O-Auth). This class is used in the Snapshots & Streams services
* **Dicts**: Module that contains mulitple dictionaries for data combination or better human-reading.

Installation
============
To install this library, run the following commands. However, this library will be installed as a dependency of other Factiva or Dow Jones packages.

.. code-block::

    $ pip install --upgrade factiva-core

Using Library services
======================
Quick examples that show how to use the included services.

Creating a User Instance and Getting its statistics
---------------------------------------------------
Create `UserKey` instance and retrieve a summary of the account statistics.

.. code-block:: python

    from factiva.core import UserKey
    u = UserKey(key='abcd1234abcd1234abcd1234abcd1234', stats=True)
    print(u)

.. code-block::

    <class 'factiva.core.userkey.UserKey'>
    |-key = ****************************1234
    |-cloud_token = **Not Fetched**
    |-account_name = AccName1234
    |-account_type = account_with_contract_limits
    |-active_products = DNA
    |-max_allowed_concurrent_extractions = 5
    |-max_allowed_extracted_documents = 200,000
    |-max_allowed_extractions = 3
    |-currently_running_extractions = 0
    |-total_downloaded_bytes = 7,253,890
    |-total_extracted_documents = 2,515
    |-total_extractions = 1
    |-total_stream_instances = 4
    |-total_stream_subscriptions = 1
    |-enabled_company_identifiers = [{'id': 4, 'name': 'isin'}, {'id': 3, 'name': 'cusip'}, {'id': 1, 'name': 'sedol'}, {'id': 5, 'name': 'ticker_exchange'}]
    |-remaining_documents = 197,485
    |-remaining_extractions = 2


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
