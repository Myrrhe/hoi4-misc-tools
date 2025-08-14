# -*- coding: utf-8 -*-
"""Manage the commands."""

import logging
import sys

from cli import Command, CommandParser

_logger: logging.Logger = logging.getLogger(__name__)


class CommandRegistry:
    """Registry to store and execute commands."""

    _commands: dict[str, type[Command]] = {}
    _initialized = False

    @classmethod
    def register(cls, command_cls: type[Command]) -> None:
        """Register a command class."""
        cls._commands[command_cls.signature] = command_cls

    @classmethod
    def initialize(cls) -> None:
        """Initialize registry only once."""
        if not cls._initialized:
            for command_cls in Command.__subclasses__():
                if hasattr(command_cls, "signature"):
                    cls.register(command_cls)
            cls._initialized = True

    @classmethod
    def execute(cls, signature: str) -> None:
        """Execute the command corresponding to the given signature."""
        command_cls = cls._commands.get(signature)
        if command_cls:
            command_parser = CommandParser()
            command = command_cls()
            command.add_arguments(command_parser)
            new_args = command_parser.parse_args(sys.argv[2:])
            command.handle(
                *sys.argv[2:],
                **new_args,
            )
        else:
            _logger.critical("Unknown command: {%s}", signature)
