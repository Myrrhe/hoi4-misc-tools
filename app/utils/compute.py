# -*- coding: utf-8 -*-
"""Computation functions."""


def compute_payback_time(
    nb_infra: int,
    bonus: float,
    goods: float
) -> float:
    """Compute the time needed for a civilian factory to be profitable."""
    infra_bonus: float = 1.0 + (nb_infra / 5.0)
    time: float = 10800.0 / (5 * infra_bonus * bonus * goods)
    return time
