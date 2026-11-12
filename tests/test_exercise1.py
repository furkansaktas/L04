import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even_docstring():
    assert is_even(4) is True
    assert is_even(3) is False
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-3) is False


# bug report 2
def test_r2_double():
    assert double(5) == 10
