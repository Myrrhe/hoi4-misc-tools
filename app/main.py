# -*- coding: utf-8 -*-
"""Entry point."""

import logging
import os
import sys

from cli import CommandRegistry

_logger: logging.Logger = logging.getLogger(__name__)


def main(*_, **__) -> int | str | None:
    """Entry point."""
    os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    CommandRegistry.initialize()
    CommandRegistry.execute(sys.argv[1])
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:]))
