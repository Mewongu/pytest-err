# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg
import ast
from pathlib import Path


def get_calling_function_name(file, line):
    if isinstance(file, str):
        file = Path(file)

    fn_scopes = function_scopes_for_module(file)
    return fn_scopes[line]


def function_scopes_for_module(file: Path):
    function_definitions = get_function_definitions(ast.parse(file.read_text()))

    function_scopes = IntervalKeeper()
    for fn_def in function_definitions:
        *_, last_statement = fn_def.body
        function_scopes[fn_def.lineno : last_statement.lineno] = fn_def.name

    return function_scopes


def get_function_definitions(node):
    function_definitions = list()
    if isinstance(node, ast.Module):
        for child in node.body:
            function_definitions.extend(get_function_definitions(child))
        return function_definitions
    elif isinstance(node, ast.FunctionDef):
        function_definitions.append(node)
        for child in node.body:
            function_definitions.extend(get_function_definitions(child))
        return function_definitions
    elif isinstance(node, ast.ClassDef):
        for child in node.body:
            function_definitions.extend(get_function_definitions(child))
        return function_definitions
    return []


class IntervalKeeper:
    def __init__(self):
        self.intervals = dict()

    def __setitem__(self, key, value):
        self.intervals[key.start, key.stop] = value

    def __getitem__(self, item):
        if isinstance(item, int):
            items = sorted(
                self.intervals.items(),
                key=lambda x: (x[0][0], x[0][1] - x[0][0], x[0][1], x[1]),
            )
            for interval, value in items:
                if interval[0] <= item <= interval[1]:
                    return value

        elif isinstance(item, slice):
            return self.intervals[item.start, item.stop]
