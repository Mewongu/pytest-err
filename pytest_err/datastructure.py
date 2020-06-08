# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg
from enum import Enum

from pytest_err.util import get_calling_function_name


class Indent(Enum):
    EMPTY = "  "
    LAST = "└─"
    CONTINUATION = "│ "
    BRANCH = "├─"


class Node:
    def __init__(self, file, line_no):
        self.file = file
        self.line_no = line_no
        self.callers = dict()
        self.visits = 0

    def add_caller(self, *call_stack):
        top, *rest = call_stack
        if top not in self.callers:
            self.callers[top] = Node(*top)
        if top in self.callers:
            self.callers[top].visits += 1
        if rest:
            self.callers[top].add_caller(*rest)

    def __str__(self, indents=[], last=False):
        if indents:
            indent_str = f"\n[{self.visits}]  " + "".join(i.value for i in indents)
        else:
            indent_str = f"[{self.visits}]  "

        rs = ""
        rs += f"{indent_str}{get_calling_function_name(self.file, self.line_no)}:{self.line_no}"
        if self.callers:
            if len(self.callers) > 1:
                *most, last = self.callers.values()
            else:
                most = []
                last = list(self.callers.values())[0]
            for caller in most:
                rs += caller.__str__(update_indents(indents) + [Indent.BRANCH])
            rs += last.__str__(update_indents(indents) + [Indent.LAST])

        return rs


indent_replacement = {Indent.LAST: Indent.EMPTY, Indent.BRANCH: Indent.CONTINUATION}


def update_indents(indents):
    return [indent_replacement.get(x, x) for x in indents]
