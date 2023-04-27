
def read(file_name):
    path = f"./questions/{file_name}.txt"
    with open(path, 'r') as f:
        question = f.read().splitlines()

    return question