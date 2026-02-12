# Tech Stack Decision

## Backend Language: Python

### 선택 이유
- FastAPI를 활용한 빠른 API 개발
- 비동기 처리 및 성능 확보 용이
- 게임 로직 구현에 적합한 가독성
- 추후 운영/자동화/DevOps 스크립트와 연계 용이

## Web Framework: FastAPI
- 자동 Swagger 문서 제공
- 간결한 코드 구조
- 실제 서비스 운영에 적합

## Database
- SQLite (초기)
- PostgreSQL (운영 단계 전환 예정)

## Infra / DevOps (Planned)
- Docker
- GitHub Actions (CI)
- Cloud Server (AWS or Fly.io)

## Why Not Others?
- Node.js: 개인 숙련도 및 운영 자동화 측면에서 Python이 더 적합
- Java/Spring: 개인 프로젝트 규모 대비 과도한 구조