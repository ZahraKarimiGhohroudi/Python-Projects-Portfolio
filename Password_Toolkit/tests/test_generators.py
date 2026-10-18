import string
import pytest


from password_toolkit import (
    MemorablePasswordGenerator,
    PinCodeGenerator,
    RandomPasswordGenerator,
)


# -----test for Random Password----
def test_random_password_length():
    assert len(RandomPasswordGenerator(length=15).generate()) == 15


def test_random_password_length_stays_the_same_across_calls():
    gen = RandomPasswordGenerator(length=12)
    assert len(gen.generate()) == 12
    assert len(gen.generate()) == 12


def test_random_password_letters_only():
    pwd = RandomPasswordGenerator(
        length=12, include_numbers=False, include_symbols=False
    ).generate()
    assert pwd.isalpha()


def test_random_password_include_numbers():
    pwd = RandomPasswordGenerator(
        length=12, include_numbers=True, include_symbols=False
    ).generate()
    assert pwd.isalnum()


def test_random_password_always_has_required_groups():
    gen = RandomPasswordGenerator(length=10, include_numbers=True, include_symbols=True)
    for _ in range(100):
        pwd = gen.generate()
        assert any(c in string.ascii_lowercase for c in pwd)
        assert any(c in string.ascii_uppercase for c in pwd)
        assert any(c in string.digits for c in pwd)
        assert any(c in string.punctuation for c in pwd)


def test_random_password_short_length_is_changed_to_8():
    gen = RandomPasswordGenerator(length=2, include_numbers=True, include_symbols=True)
    assert gen.length == 8


# ---test for Memorable Password----


def test_memorable_custom_vocabulary():
    gen = MemorablePasswordGenerator(num_of_words=2, vocabulary=["only"])
    assert gen.generate() == "only-only"


def test_memorable_word_count_and_separator():
    gen = MemorablePasswordGenerator(
        num_of_words=3, separator="*", vocabulary=["alpha", "beta"]
    )
    assert len(gen.generate().split("*")) == 3


def test_memorable_capitalization():
    gen = MemorablePasswordGenerator(
        num_of_words=4, separator="-", capitalization=True, vocabulary=["river"]
    )
    assert gen.generate() == "River-River-River-River"


def test_memorable_short_word_count_is_changed_to_2():
    gen = MemorablePasswordGenerator(num_of_words=1, vocabulary=["a"])
    assert len(gen.generate().split("-")) == 2


def test_memorable_rejects_empty_vocabulary():
    with pytest.raises(ValueError):
        MemorablePasswordGenerator(vocabulary=[])


# ---- test for Pin Code ----


def test_pin_is_digits_only():
    for _ in range(100):
        pin = PinCodeGenerator(length=6).generate()
        assert len(pin) == 6
        assert pin.isdigit()


def test_pin_short_length_is_changed_to_4():
    assert len(PinCodeGenerator(length=2).generate()) == 4
