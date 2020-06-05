# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg


def function_a():
    raise RuntimeError("This function should fail")


def function_b():
    raise RuntimeError("This function should fail")


def function_c():
    common_function()


def function_d():
    common_function()


def common_function():
    raise RuntimeError("This function should fail")


def deep_error():
    deeper_error()


def deeper_error():
    deepest_error()


def deepest_error():
    common_function()
