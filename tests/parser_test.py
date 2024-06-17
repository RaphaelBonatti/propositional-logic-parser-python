from modules.parser import wff_from_str


def test_simple_wff_to_string():
    wff_str = "A"

    s = wff_from_str(wff_str).toString()

    assert s == "A"


def test_compound_wff_to_string():
    wff_str = "(~ A & B ) "

    s = wff_from_str(wff_str).toString()

    assert s == "(¬A ∧ B)"


def test_complex_compound_wff_to_string():
    wff_str = "(~ (( ~A & (B1 | B2) )<=>C ) => D  )"

    s = wff_from_str(wff_str).toString()

    assert s == "(¬((¬A ∧ (B1 ∨ B2)) ↔ C) → D)"
