# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg

import pytest
from _pytest._code.code import ReprFileLocation, ReprEntry
from _pytest.reports import TestReport
from _pytest.terminal import TerminalReporter

from pytest_err.datastructure import Node

ENABLED = False
FAULT_NODES = Node(None, None)


def pytest_addoption(parser):
    group = parser.getgroup("error reporting", "reporting", after="general")
    group.addoption(
        "--error-analysis",
        default=False,
        action="store_true",
        help="Should an analysis of common error causes be performed?",
    )


@pytest.mark.trylast
def pytest_configure(config):
    global ENABLED
    ENABLED = config.getoption("error_analysis")

    # TODO: Create handler for saving info


def pytest_runtest_logreport(report: TestReport):
    """Check result and post result"""

    if not ENABLED:
        return

    if (report.when, report.outcome) in (("setup", "failed"), ("call", "failed")):
        stack = list()

        exc_chain_repr = report.longrepr
        repr_traceback = exc_chain_repr.reprtraceback
        repr_crash = exc_chain_repr.reprcrash  # type: ReprCrash
        reprentries = repr_traceback.reprentries
        for entry in reprentries:  # type: ReprEntry
            repr_file_loc = entry.reprfileloc  # type: ReprFileLocation
            stack.append((repr_file_loc.path, repr_file_loc.lineno))

        FAULT_NODES.add_caller(*reversed(stack))


def pytest_unconfigure(config):
    if ENABLED:
        standard_reporter = config.pluginmanager.getplugin(
            "terminalreporter"
        )  # type: TerminalReporter
        standard_reporter.write_sep("=", "Error Report")
        standard_reporter.write_line("[<#visits>]   <function>:<lineno> ")
        standard_reporter.write_sep("-", "-")
        for fault in FAULT_NODES.callers.values():
            standard_reporter.write_line(str(fault))
