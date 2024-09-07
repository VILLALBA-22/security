from fastapi import FastAPI
from .routers import webhooks

app = FastAPI()
app.include_router(webhooks.router)

@app.get("/")
async def test(): 
  return {
    "cash": "Of course sr!"
  }