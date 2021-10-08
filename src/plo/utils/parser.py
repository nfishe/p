from argparse import ArgumentParser, _SubParsersAction
from typing import Any, Callable, List, Optional

__all__ = ("parser", "command", "argument")

parser = ArgumentParser()
subparsers = None


def command(args: Optional[List] = None, parent: Optional[_SubParsersAction] = None):
    """Add command to subparser."""
    if parent is None:
        global subparsers
        if subparsers is None:
            subparsers = parser.add_subparsers(dest="command")
        parent = subparsers

    def decorator(func: Callable) -> Callable:
        parser = parent.add_parser(
            func.__name__,
        )

        if args:
            if not isinstance(args, list):
                raise AssertionError("Arguments must be a list")

            for arg in args:
                parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)
        return func

    return decorator


def argument(*name_or_flags: str, **kwargs: Any):
    return ([*name_or_flags], kwargs)
