from __future__ import annotations

from dataclasses import dataclass

from fffunds.company import Company  # noqa: TCH001


@dataclass
class Fund:
    """Class storing information about a fund."""

    name: str
    holdings: dict[Company, float]  # maps a Company to its fund amount
