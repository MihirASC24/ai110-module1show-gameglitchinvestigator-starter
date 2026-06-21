import pytest

from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the previous hint bug ---
# Previously, the secret was sometimes passed in as a string (e.g. "50").
# Comparing an int guess against a string secret produced wrong hints:
# "Too Low" when it should be "Too High" and vice versa. check_guess now
# coerces both operands to int, so the hint must be correct regardless of
# whether secret is an int or a numeric string.

@pytest.mark.parametrize("secret", [50, "50"])
def test_string_secret_win(secret):
    outcome, _ = check_guess(50, secret)
    assert outcome == "Win"


@pytest.mark.parametrize("secret", [50, "50"])
def test_string_secret_too_high(secret):
    # Guess above the secret must report "Too High", not "Too Low"
    outcome, _ = check_guess(60, secret)
    assert outcome == "Too High"


@pytest.mark.parametrize("secret", [50, "50"])
def test_string_secret_too_low(secret):
    # Guess below the secret must report "Too Low", not "Too High"
    outcome, _ = check_guess(40, secret)
    assert outcome == "Too Low"


def test_string_guess_matches_int_secret():
    # Symmetric case: a numeric-string guess against an int secret
    outcome, _ = check_guess("40", 50)
    assert outcome == "Too Low"
