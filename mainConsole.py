from model.ecdsaModule import *
from usecase.CreateKey import createKey
from usecase.CreateSignature import createSignature
from usecase.VerifySignature import verifySignature

if __name__ == '__main__':
    M = 123123718736132617326

    d, publicKey = createKey(curve)
    print("privateKey\n", d, "\n")

    print("publicKey\n", publicKey, "\n")
    signature = createSignature(
        E=curve,
        M=M,
        publicKey=publicKey,
        d=d,
    )
    print("signature\n", signature, "\n")

    ss = verifySignature(
        E=curve,
        publicKey=publicKey,
        signature=signature,
    )
    print("verify = ", ss)