# -*- coding: utf-8 -*-
"""Used to store one argument."""

from typing import Any, Optional


class Argument:
    """Used to store one argument."""

    def __init__(
        self,
        signature: str,
        actions: Optional[str],
        _type: Optional[type],
        default: Optional[Any],
        choices: Optional[list[Any]],
        _help: Optional[str],
    ) -> None:
        self.signature = signature
        self.actions = actions
        self.type = _type
        self.default = default
        self.choices = choices
        self.help = _help

    def __str__(self) -> str:
        return self.help if self.help is not None else ""

    def __repr__(self) -> str:
        return self.help if self.help is not None else ""
