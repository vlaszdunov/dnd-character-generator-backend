from fastapi import FastAPI
import uvicorn
from core.config import settings

app = FastAPI()


@app.get("/")
async def a():
    return {"status": "OK"}


def main():
    uvicorn.run(
        "app.main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )


if __name__ == "__main__":
    main()
