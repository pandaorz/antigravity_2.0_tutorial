#!/usr/bin/env bash

# ==========================================================================
# Antigravity v2 - Linux 自動化備份安全腳本 (Secure & Idempotent)
# ==========================================================================
# 特色：
# 1. 嚴格錯誤中斷機制 (set -euo pipefail)
# 2. 排他鎖 (Lock File) 機制，防範重複執行衝突
# 3. 參數防呆與路徑驗證
# 4. 冪等性設計 (Idempotent mkdir/rsync)
# 5. 自動清理 7 天前過期備份
# ==========================================================================

# 1. 啟用嚴格模式
set -euo pipefail
IFS=$'\n\t'

# 2. 定義腳本全域變數與鎖檔案
LOCK_FILE="/tmp/antigravity_backup.lock"
BACKUP_DAYS_TO_KEEP=7

# 3. 錯誤處理回撥函式
cleanup() {
    # 釋放排他鎖
    if [ -f "$LOCK_FILE" ]; then
        rm -f "$LOCK_FILE"
        echo "[INFO] 鎖檔案已順利釋放。"
    fi
}
trap cleanup EXIT ERR SIGINT SIGTERM

# 4. 防止重複執行 (Locking)
# 嘗試開啟檔案描述符 99 指向鎖檔案，並使用 flock 進行非阻塞性排他鎖定
exec 99>"$LOCK_FILE"
if ! flock -n 99; then
    echo "[WARNING] 備份任務已在背景執行中！請勿重複啟動。" >&2
    exit 1
fi

# 5. 參數防呆檢查
if [ "$#" -ne 2 ]; then
    echo "❌ 參數錯誤！" >&2
    echo "💡 使用說明: $0 <來源目錄> <備份目標目錄>" >&2
    exit 2
fi

SOURCE_DIR="$1"
TARGET_DIR="$2"

echo "=========================================="
echo "⚡ Antigravity 安全備份引擎啟動"
echo "=========================================="
echo "來源目錄: $SOURCE_DIR"
echo "目標目錄: $TARGET_DIR"

# 6. 路徑安全性驗證
if [ ! -d "$SOURCE_DIR" ]; then
    echo "❌ [錯誤] 來源目錄 '$SOURCE_DIR' 不存在！備份終止。" >&2
    exit 3
fi

# 7. 冪等性建立目標目錄
# mkdir -p 本身具備冪等性，若目錄已存在不會噴錯
if [ ! -d "$TARGET_DIR" ]; then
    echo "[INFO] 目標目錄不存在，正在建立..."
    mkdir -p "$TARGET_DIR"
fi

# 8. 執行備份 (以 tar 封裝並加入 timestamp)
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILENAME="backup_${TIMESTAMP}.tar.gz"
BACKUP_FULLPATH="${TARGET_DIR}/${BACKUP_FILENAME}"

echo "[RUN] 正在封裝壓縮備份檔案..."
# 排除隱藏系統檔，將來源目錄打包
tar --exclude='lost+found' -czf "$BACKUP_FULLPATH" -C "$SOURCE_DIR" .

echo "✅ [成功] 備份已安全完成！檔名: $BACKUP_FILENAME"
echo "檔案大小: $(du -sh "$BACKUP_FULLPATH" | cut -f1)"

# 9. 舊檔案定期清理 (Retention Policy)
echo "[RUN] 正在搜尋並清理超過 $BACKUP_DAYS_TO_KEEP 天的舊備份檔..."
# find 搭配 -maxdepth 與 -mtime 清理，並防止誤刪其他檔案
find "$TARGET_DIR" -maxdepth 1 -name "backup_*.tar.gz" -type f -mtime +"$BACKUP_DAYS_TO_KEEP" -exec rm -f {} \;
echo "✅ 舊備份清理完成。"
echo "=========================================="
