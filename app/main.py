from fastapi import FastAPI, Header, HTTPException
from app.schemas import Message
from app.auth import create_jwt
from fastapi.responses import JSONResponse

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"

app = FastAPI()

@app.post("/DevOps")
async def devops_endpoint(
    message: Message,
    x_parse_rest_api_key: str = Header(...),
    x_jwt_kyw: str = Header(...)
):
    print("🛂 API Key recibida:", x_parse_rest_api_key)
    print("🔐 JWT Header recibido:", x_jwt_kyw)
    print("📦 Cuerpo recibido:", message)

    if x_parse_rest_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    return {"message": f"Hello {message.to} your message will be sent"}

@app.api_route("/DevOps", methods=["GET", "PUT", "DELETE", "PATCH"])
async def devops_invalid_method():
    return JSONResponse(status_code=405, content={"error": "ERROR"})

@app.get("/")
def home():
    return {"message": "Microservicio DevOps activo"}
