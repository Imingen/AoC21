import question_reader as qr

def test_one():

    question = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']


    depth = 0
    horizontal = 0

    for elem in question:

        direction, value = elem.split()

        if direction == 'forward':
            horizontal += int(value)
        if direction == 'down':
            depth += int(value)
        if direction == 'up':
            depth -= int(value)
    
    print(f"Depth: {depth}, Horizontal: {horizontal}")
    print(f"Value: {int(depth) * int(horizontal)}")


def real_one():
    question = qr.read("2_1")

    depth = 0
    horizontal = 0

    for elem in question:

        direction, value = elem.split()

        if direction == 'forward':
            horizontal += int(value)
        if direction == 'down':
            depth += int(value)
        if direction == 'up':
            depth -= int(value)
    
    print(f"Depth: {depth}, Horizontal: {horizontal}")
    print(f"Value: {int(depth) * int(horizontal)}")


def test_two():
    question = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

    depth = 0
    horizontal = 0
    aim = 0

    for elem in question:

        direction, value = elem.split()

        if direction == 'forward':
            horizontal += int(value)
            depth += aim * int(value)

        if direction == 'up':
            aim -= int(value)

        if direction == 'down':
            aim += int(value)

    print(f"Aim: {aim}, depth: {depth}, horizontal: {horizontal}")
    print(f"Answer = {int(depth) * int(horizontal)}")

def two():
    question = qr.read("2_2")

    depth = 0
    horizontal = 0
    aim = 0

    for elem in question:

        direction, value = elem.split()

        if direction == 'forward':
            horizontal += int(value)
            depth += aim * int(value)

        if direction == 'up':
            aim -= int(value)

        if direction == 'down':
            aim += int(value)

    print(f"Aim: {aim}, depth: {depth}, horizontal: {horizontal}")
    print(f"Answer = {int(depth) * int(horizontal)}")


if __name__ == "__main__":
    two()