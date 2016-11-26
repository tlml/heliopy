import heliopy.data.wind as wind
import heliopy.data.mms as mms
from datetime import datetime
import urllib


def test_wind():
    """
    Tests for imporitng wind data.

    Currently only try to download a single day's data for each product.
    """
    starttime = datetime(2010, 1, 1, 0, 0, 0)
    endtime = datetime(2010, 1, 1, 23, 59, 59)

    wind.mfi_h0(starttime, endtime)
    wind.threedp_pm(starttime, endtime)


def test_mms():
    """
    Tests for importing mms data.

    Try and import a single days' worth of data for each data product.
    """
    starttime = datetime(2016, 1, 1, 0, 0, 0)
    endtime = datetime(2016, 1, 1, 1, 0, 0)

    for i in range(1, 5):
        mms.fgm_survey(str(i), starttime, endtime)

if __name__ == '__main__':
    test_mms()