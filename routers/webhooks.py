from fastapi import APIRouter, Request

router = APIRouter(
  prefix="/webhook",
  tags=["Webhooks"]
)

@router.post("/repository")
async def webhook(request: Request):
  body_json = {}

  try: 
    body_json = await request.json()
  except:
    print("An exception occurred")

  print(body_json)
  