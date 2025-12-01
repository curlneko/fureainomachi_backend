from unittest.mock import MagicMock, patch

import pytest
from app.routers.posts_router import get_posts, create_post

from app.models.posts_model import Post
from app.schemas.posts_schema import PostCreate


def test_get_posts_success():
    mock_db = MagicMock()

    # テストデータ（SQLAlchemyモデル）
    mock_post1 = Post(id=1, title="Post 1", content="Content 1", author_id=1)
    mock_post2 = Post(id=2, title="Post 2", content="Content 2", author_id=2)

    # serviceを一時置き換える
    with patch("app.routers.posts_router.get_posts_service", return_value=[mock_post1, mock_post2]) as mock_service:
        result = get_posts(db=mock_db)

    assert result == [mock_post1, mock_post2]

    mock_service.assert_called_once_with(mock_db)


def test_get_posts_not_found():
    mock_db = MagicMock()

    with patch("app.routers.posts_router.get_posts_service", return_value=[]) as mock_service:
        # 発生しなかった場合はテスト失敗、発生すればテスト成功
        with pytest.raises(Exception) as exc_info:
            get_posts(db=mock_db)

    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Posts not found"


def test_create_post_success():
    mock_db = MagicMock()
    mock_post_create = PostCreate(title="Hello", content="World", author_id=1)
    mock_post = Post(id=1, title="Hello", content="World", author_id=1)

    with patch("app.routers.posts_router.create_post_service", return_value=mock_post) as mock_service:
        result = create_post(post=mock_post_create, db=mock_db)

    assert result == mock_post
    mock_service.assert_called_once_with(mock_db, mock_post_create)
