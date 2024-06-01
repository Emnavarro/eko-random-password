from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel
from starlette import status
import random
import string

app = FastAPI()

class InputParams(BaseModel):
    length: int
    lowercase: int
    uppercase: int
    digits: int
    

def validate_params(
    length: int = Query(..., description="La longitud total de la contraseña"),
    lowercase: int = Query(..., description="El número de letras minúsculas"),
    uppercase: int = Query(..., description="El número de letras mayúsculas"),
    digits: int = Query(..., description="El número de dígitos")
) -> InputParams:
    if length < 20:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="La longitud tiene que ser mayor que 19")
    if lowercase < 10:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="La letras minusculas no pueden ser inferiores a 10")
    if uppercase < 10:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="La letras mayuculas no pueden ser inferiores a 10")
    if digits < 10:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Los digitos no pueden ser inferiores a 10")
    
    
    
    if lowercase + uppercase + digits > length:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La suma de todo tiene que ser igual a la longitud total."
        )
    return InputParams(length=length, lowercase=lowercase, uppercase=uppercase, digits=digits)

def generate_password(params: InputParams) -> str:
    password = (
        random.choices(string.ascii_lowercase, k=params.lowercase) +
        random.choices(string.ascii_uppercase, k=params.uppercase) +
        random.choices(string.digits, k=params.digits)
    )
    if len(password) < params.length:
        chars_left = params.length - len(password)
        password += random.choices(string.ascii_letters + string.digits, k=chars_left)
    random.shuffle(password)
    return ''.join(password)


@app.get("/generate-password/", status_code=status.HTTP_201_CREATED)
async def generate_password_endpoint(params: InputParams = Depends(validate_params)):
    password = generate_password(params)
    return {"password": password}