import os
import sqlite3
import subprocess

import pytest

import homework
from homework import *


# bug report 1
def test_r1_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32


# bug report 2
def test_r2_get_grade():
    assert get_grade(90) == "A"


# bug report 3
def test_r3_find_max():
    assert find_max([-5, -10, -3]) == -3


# bug report 4
def test_r4_is_leap_year():
    assert is_leap_year(2000) == True


# bug report 5
def test_r5_binary_search_single_element():
    assert binary_search([5], 5) == 0
