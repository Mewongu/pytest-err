# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg
from example_test_suite.common import (
    function_a,
    function_b,
    function_c,
    function_d,
    deep_error,
)


def test_function_a():
    function_a()


def test_function_b():
    function_b()


def test_function_c():
    function_c()


def test_function_d():
    function_d()


def test_deep_error():
    deep_error()
