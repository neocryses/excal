#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `cli` module of `excal` package."""

import re

# import pytest
from click.testing import CliRunner

from excal import cli


def test_command_line_help():
    """Test help option"""
    runner = CliRunner()
    pattern = re.compile(r"--help\s+Show this message and exit.")
    result = runner.invoke(cli.main, ['--help'])
    assert result.exit_code == 0
    assert pattern.search(result.output) is not None
