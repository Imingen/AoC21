



def test_one():
    question = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    increase_counter = 0
    for i, elem in enumerate(question):
        if i > 0:
            if elem > question[i-1]:
                increase_counter += 1

    print(increase_counter)

def test_two():
    question = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    increase_counter = 0
    prev = 0
    for i, elem in enumerate(question):
        if (i + 2) > len(question)-1:
            break
        result = elem + question[i+1] + question[i+2]
        if i < 1:
            prev = result
            continue

        if result > prev:
            increase_counter += 1
        
        prev = result

    print(increase_counter)


def one():
    path = f"./questions/1.txt"
    with open(path, 'r') as f:
        content = f.read().splitlines()
    
    increase_counter = 0
    for i, elem in enumerate(content):
        if i > 0:
            if int(elem) > int(content[i-1]):
                increase_counter += 1

    print(increase_counter)


def two():
    path = f"./questions/1_2.txt"
    with open(path, 'r') as f:
        question = f.read().splitlines()
    

    increase_counter = 0
    prev = 0
    for i, elem in enumerate(question):
        if (i + 2) > len(question)-1:
            break
        result = int(elem) + int(question[i+1]) + int(question[i+2])
        if i < 1:
            prev = result
            continue

        if result > prev:
            increase_counter += 1
        
        prev = result

    print(increase_counter)





if __name__ == "__main__":
    two()
