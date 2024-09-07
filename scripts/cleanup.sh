#!/bin/bash

# __pycache__ディレクトリを削除
rm -rf __pycache__/

# migrationsディレクトリを削除
rm -rf migrations

# 実行完了メッセージ
echo "Cleanup completed: __pycache__ and migrations have been removed."