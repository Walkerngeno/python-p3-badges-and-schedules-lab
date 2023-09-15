# conftest.py

import pytest

@pytest.hookimpl(tryfirst=True)
def pytest_itemcollected(item):
    # Modify the item._nodeid attribute as needed
    pref = "prefix"
    suf = "suffix"
    item._nodeid = ' '.join((pref, suf))
