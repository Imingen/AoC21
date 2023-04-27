from io import BytesIO
from os import read
#import numpy as np
import re
from PIL import Image
import requests
import base64
def test_one():
    question = np.array( [3,4,3,1,2])
    days = 1
    while days <= 80:
        print(f"Day: {days}")
        for i, elem in enumerate(question):
            if elem == 6:
                question = np.append(question, 8)
                question[i] -= 1
                continue
            if elem == 0:
                question[i] = 6
                continue
            question[i] -= 1
        days += 1
        
    print(len(question))

def ok():
    sangen = [
    "Spredt og i klynger der elven seg slynger",
    "ligger du Porsblomstens by.",
    "Dampfløyter hviner og sagblader synger",
    "muntert ved kveld og ved gry.",
    "",
    "ref.:",
    "",
    "For ditt vell vårt hjerte banker,",
    "og fra fremmed havn",
    "hjem til deg går våre tanker,",
    "kjært er Porsgrunns navn.",
    "",
    "Klang ifra ambolt og svingende hammer,",
    "kullrøyk fra piper mot sky,",
    "elven med tauing av flåter og prammer, -",
    "- baugen er vendt mot det ny.",
    "",
    "ref.",
    "",
    "Vendte vi hjemad der ute fra verden,",
    "Telemarks fjelde de blå",
    "vinket imot oss: velkommen fra ferden,",
    "- byen ved elven vi så.",
    "",
    "ref."
]

    one = len(sangen[8])
    two = len(sangen[20])
    three = len(sangen[4])
    four = len(sangen[5])
    five = len(sangen[10])
    six = len(sangen[1])

    
    print(one)
    print(sangen[7][one])
    print(sangen[15][two])
    print(sangen[5][three])

    print(sangen[1][five])
    print(sangen[2][six])

    print(sangen[13][four])


def pors_8():
    with open("file.txt","r") as f:
        line_num = 0
        for line in f:
            line_num += 1
            base64_message = line
            base64_bytes = base64_message.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            print(message_bytes.decode('utf-8'))


if __name__ == '__main__':
    #ok()
    #test_one()
    pors_8()