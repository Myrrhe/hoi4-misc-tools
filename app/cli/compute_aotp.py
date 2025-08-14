# -*- coding: utf-8 -*-
"""Compute Ahead Of Time penalty."""

import logging

from cli import Command, CommandParser

_logger: logging.Logger = logging.getLogger(__name__)


class ComputeAOTP(Command):
    """Compute Ahead Of Time penalty."""

    signature: str = "compute_aotp"

    description: str = "Compute Ahead Of Time penalty"

    def add_arguments(self, parser: CommandParser) -> None:
        """Add arguments to the command."""
        parser.add_argument(
            "--nb_days",
            _type=int,
            default=100,
            _help="Base number of days to complete",
        )
        parser.add_argument(
            "--bonus",
            _type=int,
            default=0,
            _help="Percentage bonus",
        )
        parser.add_argument(
            "--aot",
            _type=float,
            default=1.0,
            _help="AOT",
        )

    def handle(self, *args, **options) -> None:
        """Run the command."""
        res_perc: float = 0.0
        time: int = 0
        # Base Cost
        base: float = float(options["--nb_days"])
        # Research Speed Bonus
        bonus: float = float(options["--bonus"]) / 100.0
        # Ahead-of-time penalty (not years ahead)
        aot: float = float(options["--aot"])
        base /= 1 + bonus
        while res_perc < 1:
            res_perc += 1/base/(1+aot)
            aot -= 2/365
            aot = max(aot, 0)
            time += 1
        # Prints total time needed
        _logger.info(time)
