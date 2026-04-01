# Python 기반 이미지
FROM python:3.10-slim

# 작업 폴더
WORKDIR /app

# 파일 복사
COPY . /app

# 패키지 설치
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy

# 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]