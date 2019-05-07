"""
Utility module which will hold generalized functions.
"""

import datetime as dt


def parse_date_string(date_string):
    """
    Parse date string into datetmie object.
    """
    if not date_string.isdigit():
        raise ValueError("input date must be numbers")

    length = len(date_string)
    if 0 < length <= 2:
        year = dt.date.today().strftime("%Y")
        if length == 1:
            convert_string = year + "0" + date_string
        elif length == 2:
            convert_string = year + date_string
    elif len(date_string) == 4:
        convert_string = "20" + date_string
    elif len(date_string) == 6:
        convert_string = date_string
    else:
        raise ValueError("input date must be one of the following form.\n"
                         "  M\n"
                         "  MM\n"
                         "  YYMM\n"
                         "  YYYYMM")

    date = dt.datetime.strptime(convert_string, '%Y%m').date()
    return date
