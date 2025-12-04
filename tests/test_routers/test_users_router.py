from datetime import date
from unittest.mock import MagicMock, patch

import pytest

from app.enums.country import Country
from app.enums.gender import Gender
from app.enums.language import Language
from app.models.users_model import User
from app.routers.users_router import create_user
from app.schemas.users_schema import UserCreate, UserGet


def test_create_user_success() -> None:
    mock_db = MagicMock()
    mock_user_create = UserCreate(
        name="Alex",
        email="alex@example.com",
        password="securepassword123",
        current_country=Country.JA,
        birth_country=Country.TW,
        gender=Gender.FEMALE,
        spoken_language=[Language.JA, Language.EN],
        learning_language=[Language.ZH],
        birthday=date(1995, 1, 1),
    )

    mock_user = User(
        id=1,
        name="Alex",
        email="alex@example.com",
        password="securepassword123",
        current_country=Country.JA,
        birth_country=Country.TW,
        gender=Gender.FEMALE,
        spoken_language=[Language.JA, Language.EN],
        learning_language=[Language.ZH],
        birthday=date(1995, 1, 1),
    )

    with patch(
        "app.routers.users_router.create_user_service", return_value=mock_user
    ) as mock_service:
        result = create_user(input=mock_user_create, db=mock_db)

    assert result == UserGet.model_validate(mock_user)
    mock_service.assert_called_once_with(mock_db, mock_user_create)
