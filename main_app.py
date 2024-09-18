from fastapi import FastAPI, responses
import uvicorn

app = FastAPI()


@app.get("/main")
@app.get("/")
async def main_page():
    return responses.FileResponse("templates/form.html")


if __name__ == "__main__":
    uvicorn.run(app)
