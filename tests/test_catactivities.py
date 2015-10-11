import pytest
import six
import time

from catinabox import catactivities

if six.PY2:
    import mock
else:
    from unittest import mock


@mock.patch.object(time, "sleep", autospec=True)
def test__cat_nap__satisfying_nap(sleep):
    catactivities.cat_nap(350)
    sleep.assert_called_with(350)


@mock.patch.object(time, "sleep", autospec=True)
def test__cat_nap__not_satisfying(sleep):
    with pytest.raises(catactivities.NapWillNotBeSatisfying):
        catactivities.cat_nap(5)
    assert sleep.call_count == 0
