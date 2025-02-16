"""Autograding script"""

import os


def test_01():
    """Test the homework."""
    assert os.path.exists("files/output/metrics.json")
