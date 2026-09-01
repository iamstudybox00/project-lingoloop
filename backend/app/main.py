from fastapi import FastAPI

app = FastAPI(
    title="Lingoloop API",
    description="AI 영어 학습 애플리케이션 API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Hello Lingoloop"}