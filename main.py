from http import HTTPStatus
from typing import Annotated
from uuid import UUID

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from requests import Session

from database import InfraModels
from database.database import SessionLocal, engine
from display.create_key_request import CreateKeyRequest
from display.create_key_response import getCreateKeyResponse
from display.create_signature_request import CreateSignatureRequest
from display.create_signature_response import CreateSignatureResponse, Signature
from display.verify_signature_request import VerifySignatureRequest
from display.verify_signature_response import VerifySignatureResponse
from model.ecdsaModule import BASECURVE
from model.Signature import Signature as SignatureModel
from usecase.CreateKey import createKey
from usecase.CreateSignature import createSignature
from usecase.VerifySignature import verifySignature

app = FastAPI()

InfraModels.Base.metadata.create_all(bind=engine)

class Users(BaseModel):
    id: UUID
    i: str
    d: str

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/api/v1/key/create", status_code=HTTPStatus.CREATED.value)
async def create_key(request: CreateKeyRequest, db: db_dependency):
    check = db.query(InfraModels.User).filter(InfraModels.User.id == request.userId)
    if check.count() != 0:
        raise HTTPException(status_code = HTTPStatus.CONFLICT,detail='user already exists')
    else:
        i, priKey, pubKey = createKey(BASECURVE)
        infra_user = InfraModels.User()
        infra_user.id = request.userId
        infra_user.i = str(i)
        infra_user.d = str(priKey)
        db.add(infra_user)
        db.commit()
        return getCreateKeyResponse(pubKey, priKey)


@app.post("/api/v1/signature/create", status_code=HTTPStatus.CREATED.value)
async def create_signature(request: CreateSignatureRequest, db: db_dependency):
    user = db.query(InfraModels.User).filter(InfraModels.User.id == request.userId).first()
    if user is None:
        raise HTTPException(status_code = HTTPStatus.NOT_FOUND,detail='user does not exist')
    else:
        signature = createSignature(hash(request.M), BASECURVE, int(user.i), int(user.d))
        return CreateSignatureResponse(
            M = request.M,
            signature = Signature(r = signature.r, s = signature.s),
        )

@app.post("/api/v1/signature/verify",status_code=200)
async def verify_signature(request: VerifySignatureRequest, db: db_dependency):
    user = db.query(InfraModels.User).filter(InfraModels.User.id == request.userId).first()
    if user is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='user does not exist')
    else:
        check = verifySignature(BASECURVE, int(user.i), int(user.d), SignatureModel(
            M = hash(request.M),
            r = int(request.signature.r),
            s = int(request.signature.s),
        ))
        return VerifySignatureResponse(check = check)
