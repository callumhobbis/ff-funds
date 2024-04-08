import pandas as pd

from fffunds.company import identify_company, normalise_name


def test_normalise_upper() -> None:
    comp = "Google"
    assert normalise_name(comp) == "GOOGLE"


def test_normalise_full_stops() -> None:
    comp = "C.N.O.O.C."
    assert normalise_name(comp) == "CNOOC"


def test_normalise_commas() -> None:
    comp = "Stuff,Cool"
    assert normalise_name(comp) == "STUFF COOL"


def test_abbreviations() -> None:
    comp = "Something Ltd"
    assert normalise_name(comp) == "SOMETHING LIMITED"


def test_accents() -> None:
    comp = "Petróleos del Perú"
    assert normalise_name(comp) == "PETROLEOS DEL PERU"


def test_ampersand() -> None:
    comp = "Marks & Spencer"
    assert normalise_name(comp) == "MARKS AND SPENCER"


def test_all_ff_names_identified() -> None:
    ff = pd.read_csv("./tests/ff_names_matched.csv")
    ff_names = ff["company_name_sustainalytics"].to_list()
    ff_identified = ff["company_name_mbie"].apply(
        lambda x: identify_company(x, ff_names, strict=False)
    )
    assert (ff_identified == ff["company_name_sustainalytics"]).all()
