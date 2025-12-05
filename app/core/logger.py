import json
import os
import sys

from loguru import logger

# デフォルトのログ設定を削除
logger.remove()

# コンソール出力の設定
logger.add(
    sys.stdout,
    colorize=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level}</level> | {message}"
    ),
)

# file出力の設定
# 1日ごとに新しいログファイルを作る（古いファイルはローテーションされる）
# 古いログファイルは 7日間保持、それ以降は自動削除
# JSON形式で出力
logger.add(
    "logs/log_{time:YYYY-MM-DD}.log",
    rotation="00:00",
    retention="7 days",
    serialize=True,
)
