



def test_one():
    question = [[2,1,9,9,9,4,3,2,1,0],
                [3,9,8,7,8,9,4,9,2,1],
                [9,8,5,6,7,8,9,8,9,2],
                [8,7,6,7,8,9,6,7,8,9],
                [9,8,9,9,9,6,5,6,7,8]]
    kok = []
    for j, elem in enumerate(question):
        for i, value in enumerate(elem):
            adj_values = []
            if j == 0 and i == 0:
               adj_values.append(question[j][i+1])
               adj_values.append(question[j+1][i])
            elif j == 0 and i == len(elem)-1:
               adj_values.append(question[j][i-1])
               adj_values.append(question[j+1][i])
            elif j == len(question)-1 and i == 0:
               adj_values.append(question[j][i+1])
               adj_values.append(question[j-1][i])
            elif j == len(question)-1 and i == len(elem)-1:
               adj_values.append(question[j][i-1])
               adj_values.append(question[j-1][i])
            elif i == len(elem)-1:
               adj_values.append(question[j-1][i])
               adj_values.append(question[j+1][i])
               adj_values.append(question[j][i-1])
            else:
               adj_values.append(question[j][i-1])
               adj_values.append(question[j][i+1])
               adj_values.append(question[j+1][i])
            
            if all(i > int(value) for i in adj_values):
                kok.append(i)
    for elem in kok:
        print(elem)






if __name__ == '__main__':
    test_one()