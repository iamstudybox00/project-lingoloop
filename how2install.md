# 프로젝트 가상환경 처음 세팅

1. python 3.12.7 설치
2. cd backend 하여 백엔드로 Terminal 이동(PowerShell말고 CMD로)
3. python -m venv .venv 실행하여 CMD 앞쪽에 (.venv)가 떠있는지 확인
4. .venv\Scripts\activate 이동
5. pip install -r requirements.txt 해서 의존성 설치
6. pip install fastapi uvicorn로 uvicorn 깔기
7. uvicorn app.main:app --reload 해서 시작

# 이후 가상환경 들어가기
1. python -m venv .venv
2. uvicorn app.main:app --reload 입력하여 서버 실행

# Swagger(프론트엔드 없이 백엔드 API 테스트용)
- uvicorn app.main:app --reload 입력하여 서버 실행
- http://127.0.0.1:8000/docs 

# 프론트엔드 세팅
1. nodejs-bin==24.20.0
2. cd frontend 로 폴더이동
3. npm install 로 node_modules 설치
4. npm run dev 로 실행 기본 http://localhost:5173/