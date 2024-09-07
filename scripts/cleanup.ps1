# __pycache__ディレクトリを削除
Remove-Item -Recurse -Force __pycache__

# migrationsディレクトリを削除
Remove-Item -Recurse -Force migrations

# 実行完了メッセージ
Write-Host "Cleanup completed: __pycache__ and migrations have been removed."
