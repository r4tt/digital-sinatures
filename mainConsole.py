from model.ecdsaModule import *
from usecase.CreateKey import createKey
from usecase.CreateSignature import createSignature
from usecase.VerifySignature import verifySignature

if __name__ == '__main__':
    M = 123123718736132617326

    d, publicKey = createKey(BASECURVE)
    print("privateKey\n", d, "\n")

    print("publicKey\n", publicKey, "\n")
    signature = createSignature(
        E=BASECURVE,
        M=M,
        publicKey=publicKey,
        d=d,
    )
    print("signature\n", signature, "\n")

    ss = verifySignature(
        E=BASECURVE,
        publicKey=publicKey,
        signature=signature,
    )
    print("verify = ", ss)