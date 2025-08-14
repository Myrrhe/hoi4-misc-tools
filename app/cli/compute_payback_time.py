# -*- coding: utf-8 -*-
"""Compute Payback Time."""

import logging

from cli import Command, CommandParser

from utils.compute import compute_payback_time

_logger: logging.Logger = logging.getLogger(__name__)


class ComputePaybackTime(Command):
    """Compute Payback Time."""

    signature: str = "compute_payback_time"

    description: str = "Compute Payback Time"

    def add_arguments(self, parser: CommandParser) -> None:
        """Add arguments to the command."""
        parser.add_argument(
            "--nb_infra",
            _type=int,
            default=1,
            _help="Number of infrastructure",
        )
        parser.add_argument(
            "--bonus",
            _type=int,
            default=0,
            _help="Construction speed bonus",
        )
        parser.add_argument(
            "--goods",
            _type=float,
            default=0,
            _help="Consumer goods percentage",
        )

    def handle(self, *args, **options) -> None:
        """Run the command."""
        nb_infra: int = int(options["--nb_infra"])
        bonus: float = 1.0 + float(options["--bonus"]) / 100.0
        goods: float = 1.0 - float(options["--goods"]) / 100.0
        _logger.info(compute_payback_time(nb_infra, bonus, goods))
