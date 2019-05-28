"""
Utility module which will hold generalized functions.
"""

import datetime as dt

from . import exceptions as ex


def parse_date_string(date_string):
    """
    Parse date string into datetmie object.
    """
    if not date_string.isdigit():
        raise ValueError("input date must be numbers")

    length = len(date_string)
    convert_string = None

    if 0 < length <= 2:
        year = dt.date.today().strftime("%Y")
        if length == 1:
            if date_string != "0":
                convert_string = year + "0" + date_string
        elif length == 2:
            if 0 < int(date_string) <= 12:
                convert_string = year + date_string
    elif len(date_string) == 4:
        if 0 < int(date_string[2:]) <= 12:
            convert_string = "20" + date_string
    elif len(date_string) == 6:
        if 0 < int(date_string[4:]) <= 12:
            convert_string = date_string

    if convert_string is None:
        raise ex.ExcalValueError(
            "Input date must be one of the following form.\n"
            "  M\n"
            "  MM\n"
            "  YYMM\n"
            "  YYYYMM\n"
            "\nValue entered: {}".format(date_string))

    date = dt.datetime.strptime(convert_string, '%Y%m').date()
    return date
