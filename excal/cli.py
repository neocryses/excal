# -*- coding: utf-8 -*-
"""Console script for excal."""
import datetime as dt
import sys

import click

from . import calendar as cl
from . import config as cf
from . import exceptions as ex
from . import util as ut

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("dates", nargs=-1, required=False)
@click.option("-c",
              "--config",
              "config_path",
              type=click.Path(exists=True),
              default=None,
              help="Specify the path to the config file to be used")
@click.option("-g",
              "--generate-config",
              "generate_flag",
              is_flag=True,
              help="Generate config file inside current directory")
def main(dates, config_path, generate_flag):
    """Utility tool to generate excel calendars."""

    try:
        workbooks = []

        if generate_flag:
            cf.generate_config_file()

        config = cf.load_config(config_path)

        if not dates:
            excal = cl.ExcelCalendar(dt.date.today().replace(day=1), config)
            workbooks.append(excal)
        else:
            for date in dates:
                excal = cl.ExcelCalendar(ut.parse_date_string(date), config)
                workbooks.append(excal)

        for workbook in workbooks:
            workbook.paint_calendar()

    except (ex.ExcalValueError, ex.ExcalFileExistsError) as error:
        click.echo("<Error> {}".format(error))
        sys.exit(1)
