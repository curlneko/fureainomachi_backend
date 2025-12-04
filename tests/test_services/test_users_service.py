from datetime import date
from unittest.mock import MagicMock

from app.enums.country import Country
from app.enums.gender import Gender
from app.enums.language import Language
from app.models.users_model import User
from app.schemas.users_schema import UserCreate, UserGet
from app.services.users_service import create_user_service


def test_create_user_service() -> None:
    # モックのDBセッションを作成
    mock_db = MagicMock()
    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    # テストデータ（Pydanticモデル）
    new_user_data = UserCreate(
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
    # サービス関数を呼び出し
    result = create_user_service(mock_db, new_user_data)

    # db.add/db.commit/db.refresh が呼ばれたことを確認
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

    # 返り値の属性確認
    assert result.name == new_user_data.name
    assert result.current_country == new_user_data.current_country
    assert result.birth_country == new_user_data.birth_country
    assert result.gender == new_user_data.gender
    assert result.spoken_language == new_user_data.spoken_language
    assert result.learning_language == new_user_data.learning_language
    assert result.birthday == new_user_data.birthday
