from http import HTTPStatus
from typing import Annotated
import random

import cocks_pinch as cp
import complex_multiplication as cm
from display.create_curve_response import CreateCurveResponse
from display.curver import Point
from display.get_user_info_response import GetUserInfoResponse
from utils import print_curve, curve_to_string
from fastapi import FastAPI, Depends, HTTPException
from requests import Session

from database import InfraModels
from database.database import SessionLocal, engine
from display.create_key_request import CreateKeyRequest
from display.create_key_response import getCreateKeyResponse, PublicKey
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


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/api/v1/user/{userId}", status_code=HTTPStatus.OK.value)
async def get_user_info(userId: str, db: db_dependency):
    userInfo = db.query(InfraModels.User).filter(InfraModels.User.id == userId).first()
    if userInfo is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    userInfo.id = userId
    P = BASECURVE.g * int(userInfo.i)
    Q = P * int(userInfo.d)
    return GetUserInfoResponse(
        userId = userId,
        publicKey = PublicKey(
            Point(P.x, P.y),
            BASECURVE.field.n,
            Point(Q.x, Q.y),
        ),
    )

@app.post("/api/v1/key/create", status_code=HTTPStatus.CREATED.value)
async def create_key(request: CreateKeyRequest, db: db_dependency):
    check = db.query(InfraModels.User).filter(InfraModels.User.id == request.userId)
    if check.count() != 0:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail='user already exists')
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
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='user does not exist')
    check = db.query(InfraModels.Signature) \
        .filter(InfraModels.Signature.user_id == request.userId) \
        .filter(InfraModels.Signature.document == hash(request.M))
    if check.count() != 0:
        raise HTTPException(status_code=HTTPStatus.CONFLICT, detail='user already sign document')
    signature = createSignature(hash(request.M), BASECURVE, int(user.i), int(user.d))
    infra_signature = InfraModels.Signature()
    infra_signature.user_id = request.userId
    infra_signature.document = str(hash(request.M))
    db.add(infra_signature)
    db.commit()

    return CreateSignatureResponse(
        M=request.M,
        signature=Signature(r=signature.r, s=signature.s),
    )


@app.post("/api/v1/signature/verify", status_code=200)
async def verify_signature(request: VerifySignatureRequest, db: db_dependency):
    user = db.query(InfraModels.User).filter(InfraModels.User.id == request.userId).first()
    if user is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='user does not exist')
    else:
        check = verifySignature(BASECURVE, int(user.i), int(user.d), SignatureModel(
            M=hash(request.M),
            r=int(request.signature.r),
            s=int(request.signature.s),
        ))
        return VerifySignatureResponse(check=check)


@app.get("/api/v1/curve")
async def create_curve(numBits: int):
    k = random.randint(3, 10)
    r, k, D = cp.gen_params_from_bits(numBits, k)
    while (D < -20):
        r, k, D = cp.gen_params_from_bits(numBits, k)
    q, t, r, k, D = cp.run(r, k, D)
    E = cm.make_curve(q, t, r, k, D)
    print(E)
    return CreateCurveResponse(
        message=curve_to_string(q, t, k, r, D),
        curve=str(E),
        point=str(E.random_element()),
    )
