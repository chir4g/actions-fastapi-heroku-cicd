from fastapi import FastAPI


app = FastAPI()



@app.get("/")
async def index():
    return {"message" : "Landed on the homepage."}