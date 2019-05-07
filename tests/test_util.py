#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for `util` module of `excal` package."""

import datetime

import pytest

from excal import util


def test_parse_date_string_len1():
    """Test string date parsing."""
    expected = datetime.date(2019, 4, 1)
    result = util.parse_date_string("4")
    assert result == expected


def test_parse_date_string_len2():
    """Test string date parsing."""
    expected = datetime.date(2019, 11, 1)
    result = util.parse_date_string("11")
    assert result == expected


def test_parse_date_string_len3():
    """Test string date parsing."""
    with pytest.raises(ValueError):
        util.parse_date_string("904")


def test_parse_date_string_len4():
    """Test string date parsing."""
    expected = datetime.date(2019, 4, 1)
    result = util.parse_date_string("1904")
    assert result == expected


def test_parse_date_string_len5():
    """Test string date parsing."""
    with pytest.raises(ValueError):
        util.parse_date_string("01904")


def test_parse_date_string_len6():
    """Test string date parsing."""
    expected = datetime.date(2019, 4, 1)
    result = util.parse_date_string("201904")
    assert result == expected
