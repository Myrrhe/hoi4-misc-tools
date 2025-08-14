# -*- coding: utf-8 -*-
"""Used to parse arguments."""

import logging
import sys
from typing import Any, Optional

from cli import Argument

_logger: logging.Logger = logging.getLogger(__name__)


class CommandParser:
    """Used to parse arguments."""

    def __init__(self) -> None:
        self.arguments: list[Argument] = []

    def add_argument(
        self,
        signature: str,
        actions: Optional[str] = None,
        _type: Optional[type] = None,
        default: Optional[Any] = None,
        choices: Optional[list[Any]] = None,
        _help: Optional[str] = None,
    ) -> None:
        """Add one argument."""
        self.arguments.append(
            Argument(signature, actions, _type, default, choices, _help)
        )

    def parse_args(self, args: list[str]) -> dict[str, Any]:
        """Parse command-line arguments into a dictionary."""
        parsed_args = {}
        remaining_args = {
            arg.split("=", 1)[0]: {
                "val": arg.split("=", 1)[1] if "=" in arg else None,
                "is_flag": "=" not in arg,
            }
            for arg in args
        }

        for arg in self.arguments:
            if arg.signature in remaining_args:
                value = remaining_args[arg.signature]["val"]
                if remaining_args[arg.signature]["is_flag"]:
                    value = True
                # Convert to correct type
                if arg.type is not None:
                    try:
                        value = arg.type(value)
                        if arg.choices and value not in arg.choices:
                            raise ValueError(
                                f"Invalid choice: {value}. Allowed: {arg.choices}"
                            )
                    except ValueError as e:
                        _logger.critical(
                            "Error parsing {%s}: {%s}", arg.signature, e
                        )
                        sys.exit(1)
                parsed_args[arg.signature] = value
                remaining_args.pop(arg.signature)
            else:
                # If not provided, set default
                parsed_args[arg.signature] = arg.default

        return parsed_args
