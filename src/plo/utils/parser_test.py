from argparse import ArgumentParser

import pytest

from .parser import argument, command


@pytest.fixture
def parser():
    return ArgumentParser()


def test_command(parser):
    parent = parser.add_subparsers()
    @command(args=[], parent=parent)
    def test():
        None

    assert not test()


def test_command_arguments(parser):
    parent = parser.add_subparsers(dest="command")

    @command(args=[argument("foo")], parent=parent)
    def test():
        None

    assert test.__name__ in parent.choices
