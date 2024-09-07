from fastapi import FastAPI

app = FastAPI(debug=True)

@app.get("/")
async def test(): 
  return {
    "cash": "Of course sr!"
  }