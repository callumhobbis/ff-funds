import re
from dataclasses import dataclass

from unidecode import unidecode


@dataclass(frozen=True)  # frozen so it can be used as dict key
class Company:
    """Class storing information about a company."""

    name: str  # as found on Sustainalytics


EXPANDED_ABVS = {
    "LTD": "LIMITED",
    "CORP": "CORPORATION",
    "CO": "COMPANY",
    "INC": "INCORPORATED",
    "LLC": "LIMITED LIABILITY COMPANY",
    "PLC": "PUBLIC LIMITED COMPANY",
}


def normalise_name(comp: str) -> str:
    """Normalise company name for use in comparisons."""
    comp = comp.replace(".", "")  # normalise acronyms & abbreviations
    comp = comp.replace(",", " ")  # commas always separate words
    comp = comp.upper()

    # expand abbreviations
    for abv, full in EXPANDED_ABVS.items():
        comp = re.sub(rf"\b{abv}\b", full, comp)

    comp = comp.replace("&", "AND")

    return unidecode(comp)  # some funds may not respect accents


def identify_company(
    query: str, known: list[str], *, strict: bool = False
) -> str | None:
    """Identify company name in list.

    Returns the known company name if found, otherwise returns None.
    """
    query = normalise_name(query)

    # If we have an exact match (up to normalisation), it's easy.
    for comp in known:
        if query == normalise_name(comp):
            return comp

    # Check if removing suffixes like 'Ltd' gives an exact match.
    for comp in known:
        comp_stem = normalise_name(comp)
        query_stem = query
        for full in EXPANDED_ABVS.values():
            # a leading space because we assume these are at the end
            comp_stem = comp_stem.replace(f" {full}", "")
            query_stem = query_stem.replace(f" {full}", "")
        if query_stem == comp_stem:
            return comp

    if strict:
        return None

    # If nothing else works, but we can find it inside another
    # company name, go with that company.
    for comp in known:
        normed = normalise_name(comp)
        if query in normed or normed in query:
            return comp
    return None
