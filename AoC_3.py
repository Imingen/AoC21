
def test_one():
    question = ['00100', '11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010',]

    res = [sub.split() for sub in question]
    index = 0

    for elem in res:
        tmp_max = ""
        tmp_min = ""
        if index > 5:
            break
        tmp_max += max(elem[0][index])
        tmp_min += min(elem[0][index])
        index += 1


    print(tmp_min, tmp_max)

if __name__ == '__main__':
    test_one()