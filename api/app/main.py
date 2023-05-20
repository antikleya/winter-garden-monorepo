from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/test")
async def get_users():
    return {"cringe": "autism"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
# alembic upgrade head &&
