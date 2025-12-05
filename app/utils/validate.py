# app/utils/checks.py
import re
from datetime import date

from app.core.logger import logger

SQL_KEYWORDS = [
    "SELECT",
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "CREATE",
    "TRUNCATE",
    "EXEC",
    "UNION",
]

BLACKLIST_CHARS = ["<", ">", "'", '"', ";", "--"]


def check_string(value: str) -> str:
    value = value.strip()

    # 禁止文字チェック
    if any(bad in value for bad in BLACKLIST_CHARS):
        logger.error(f"Invalid character found in input: {value}")
        raise ValueError(f"Invalid character found in input: {value}")

    # SQLキーワードチェック
    upper_value = value.upper()
    if any(keyword in upper_value for keyword in SQL_KEYWORDS):
        logger.error(f"Potential SQL injection detected: {value}")
        raise ValueError(f"Potential SQL injection detected: {value}")

    return value


def validate_string(value: str) -> str:
    """文字列をチェック"""
    return check_string(value)


def validate_string_list(value: list[str]) -> list[str]:
    """文字列リストをチェック"""
    return [check_string(v) for v in value]


def validate_email(value: str) -> str:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    if not re.match(pattern, value):
        logger.warning(f"Invalid email format: {value}")
        raise ValueError("Invalid email format")
    return value


def validate_password(value: str) -> str:
    if not any(c.isdigit() for c in value):
        logger.warning("Password must contain at least one digit")
        raise ValueError("Password must contain at least one digit")
    if not any(c.isalpha() for c in value):
        logger.warning("Password must contain at least one letter")
        raise ValueError("Password must contain at least one letter")
    return value


def validate_birthday(value: date) -> date:
    if value >= date.today():
        logger.warning("Birthday must be in the past")
        raise ValueError("Birthday must be in the past")
    return value
