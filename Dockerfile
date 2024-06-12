# Dockerfile
FROM python:3.10-slim

# 環境変数の設定
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリの設定
WORKDIR /app

# 依存関係のインストール
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# プロジェクトのコードをコピー
COPY . /app/



