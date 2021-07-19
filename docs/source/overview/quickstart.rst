Quickstart
==========

The easiest way to start using `factiva-core` is by creating an instance of a User Key object.

.. code-block:: python

    from factiva.core import UserKey
    u = UserKey(key='abcd1234abcd1234abcd1234abcd1234', request_info=True)
    u

After its execution, the `UserKey` instance will contain details about the account settings and limits.
