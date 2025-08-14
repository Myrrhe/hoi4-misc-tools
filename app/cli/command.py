# -*- coding: utf-8 -*-
"""Command class."""

from abc import ABC, abstractmethod
from typing import Any

from cli import CommandParser


class Command(ABC):
    """Command class."""

    signature: str = "base_command"

    description: str = "Base command description"

    def add_arguments(self, parser: CommandParser) -> None:
        """Add arguments to the command."""

    @abstractmethod
    def handle(self, *args: Any, **options) -> None:
        """Run the command."""
