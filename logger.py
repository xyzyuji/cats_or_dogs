import logging

print("logger.pyが読み込まれました")

def get_logger():
    print("===================================================")
    logger = logging.getLogger("cats_or_dogs_logger")
    logger.setLevel(logging.INFO)

    # すでにハンドラが追加されていないか確認（重複防止）
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.propagate = False  # 二重ログ防止（必要に応じて）
    print("===================================================")
    return logger