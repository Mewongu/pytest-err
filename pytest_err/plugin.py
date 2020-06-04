# SPDX-License-Identifer: MPL-2.0
# Copyright © 2020 Andreas Stenberg
import pytest

ENABLED = False


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


def pytest_runtest_logreport(report):
    """Check result and post result"""

    if not ENABLED:
        return

    # TODO: Log if error


def pytest_unconfigure(config):
    if ENABLED:
        # TODO: Dump to file
        pass
