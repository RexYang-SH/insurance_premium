from src.model import Input
from fastapi import FastAPI
from src.infer import infer
import uvicorn

app = FastAPI(openapi_url="/api/v1/openapi.json")


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.post("/insurace-detail")
def submit_insurace(*, detail_in: Input):
    input = detail_in.model_dump()
    premium = infer(input)
    return {"Premium Evalation": premium}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
