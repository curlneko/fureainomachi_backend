from unittest.mock import MagicMock, patch

import pytest
from fastapi import HTTPException

from app.core.response import ResponseModel, success_response
from app.models.posts_model import Post
from app.routers.posts_router import create_post, get_posts
from app.schemas.posts_schema import PostCreate, PostGet


def test_get_posts_success() -> None:
    mock_db = MagicMock()

    # テストデータ（SQLAlchemyモデル）
    mock_post1 = Post(id=1, title="Post 1", content="Content 1", author_id=1)
    mock_post2 = Post(id=2, title="Post 2", content="Content 2", author_id=2)

    # serviceを一時置き換える
    with patch(
        "app.routers.posts_router.get_posts_service",
        return_value=[mock_post1, mock_post2],
    ) as mock_service:
        result = get_posts(db=mock_db)

    assert result == success_response(
        [
            PostGet.model_validate(mock_post1),
            PostGet.model_validate(mock_post2),
        ]
    )

    mock_service.assert_called_once_with(mock_db)


def test_create_post_success() -> None:
    mock_db = MagicMock()
    mock_post_create = PostCreate(title="Hello", content="World", author_id=1)
    mock_post = Post(id=1, title="Hello", content="World", author_id=1)

    with patch(
        "app.routers.posts_router.create_post_service", return_value=mock_post
    ) as mock_service:
        result = create_post(post=mock_post_create, db=mock_db)

    assert result == success_response(PostGet.model_validate(mock_post))
    mock_service.assert_called_once_with(mock_db, mock_post_create)
