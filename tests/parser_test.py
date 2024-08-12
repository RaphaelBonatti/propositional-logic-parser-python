from modules.parser import wff_from_str


def test_simple_wff_to_string():
    wff_str = "A"

    wff = wff_from_str(wff_str)

    assert str(wff) == "A"


def test_compound_wff_to_string():
    wff_str = "(~ A & B ) "

    wff = wff_from_str(wff_str)

    assert str(wff) == "(¬A ∧ B)"


def test_complex_compound_wff_to_string():
    wff_str = "(~ (( ~A & (B1 | B2) )<=>C ) => D  )"

    wff = wff_from_str(wff_str)

    assert str(wff) == "(¬((¬A ∧ (B1 ∨ B2)) ↔ C) → D)"
