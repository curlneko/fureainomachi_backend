from unittest.mock import MagicMock

from app.models.posts_model import Post
from app.schemas.posts_schema import PostCreate
from app.services.posts_service import create_post_service, get_posts_service


def test_get_posts_service():
    # モックのDBセッションを作成
    mock_db = MagicMock()

    # テストデータ（SQLAlchemyモデル）
    mock_post1 = Post(id=1, title="Post 1", content="Content 1", author_id=1)
    mock_post2 = Post(id=2, title="Post 2", content="Content 2", author_id=2)

    # db.query(Post).all() が返す値を設定
    mock_db.query.return_value.all.return_value = [mock_post1, mock_post2]

    # サービス関数を呼び出し
    results = get_posts_service(mock_db)

    # 返り値の確認
    assert results == [mock_post1, mock_post2]

    # query が1回呼ばれたことを確認
    mock_db.query.assert_called_once()


def test_create_post_service():
    # モックのDBセッションを作成
    mock_db = MagicMock()
    mock_db.add = MagicMock()
    mock_db.commit = MagicMock()
    mock_db.refresh = MagicMock()

    # テストデータ（Pydanticモデル）
    new_post_data = PostCreate(title="Hello", content="World", author_id=1)

    # サービス関数を呼び出し
    result = create_post_service(mock_db, new_post_data)

    # db.add/db.commit/db.refresh が呼ばれたことを確認
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

    # 返り値の属性確認
    assert result.title == new_post_data.title
    assert result.content == new_post_data.content
