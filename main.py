from fastapi import FastAPI

from model.ecdsaModule import curve
from usecase.CreateKey import createKey, xx

app = FastAPI()

@app.post("/api/v1/key/create")
async def create_key():
    priKey, pubKey = createKey(curve)
    print(priKey, pubKey)
    return pubKey


@app.post("/api/v1/signature/verify")
async def verifySignature(name: str):
    return {"message": f"Hello {name}"}


@app.post("/api/v1/signature/create")
async def createSignature(name: str):
    return {"message": f"Hello {name}"}