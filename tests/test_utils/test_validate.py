from datetime import date

import pytest

from app.utils.validate import (
    check_string,
    validate_birthday,
    validate_email,
    validate_password,
    validate_string,
    validate_string_list,
)


def test_check_string() -> None:
    assert validate_string("NormalString") == "NormalString"


def test_check_string_list() -> None:
    assert validate_string_list(["NormalString", "AnotherString"]) == [
        "NormalString",
        "AnotherString",
    ]


def test_check_string_with_sql_keyword() -> None:
    with pytest.raises(ValueError, match="Potential SQL injection detected"):
        check_string("DROP TABLE users")


def test_check_string_with_blacklist_char() -> None:
    with pytest.raises(ValueError, match="Invalid character found in input"):
        check_string("Invalid;String")


def test_check_email() -> None:
    assert validate_email("test@example.com") == "test@example.com"


def test_check_invalid_email() -> None:
    with pytest.raises(ValueError, match="Invalid email format"):
        validate_email("invalid-email")


def test_check_password() -> None:
    assert validate_password("Password1") == "Password1"


def test_check_invalid_password_no_digit() -> None:
    with pytest.raises(ValueError, match="Password must contain at least one digit"):
        validate_password("Password")


def test_check_invalid_password_no_letter() -> None:
    with pytest.raises(ValueError, match="Password must contain at least one letter"):
        validate_password("12345678")


def test_check_birthday() -> None:
    valid_birthday = date(1990, 1, 1)
    assert validate_birthday(valid_birthday) == valid_birthday


def test_check_future_birthday() -> None:
    future_birthday = date.today().replace(year=date.today().year + 1)
    with pytest.raises(ValueError, match="Birthday must be in the past"):
        validate_birthday(future_birthday)
