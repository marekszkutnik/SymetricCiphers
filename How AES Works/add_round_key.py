import numpy

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


# def add_round_key(s, k):
#     return numpy.bitwise_xor(s, k).tolist()

def add_round_key(state, key):
    """ It XORs the current state with the current round key"""
    for i in range(4):
        for j in range(4):
            state[i][j] ^= key[i][j]
    return state


def matrix2bytes(matrix):
    return bytes(sum(matrix, []))


matrix = add_round_key(state, round_key)
result = matrix2bytes(matrix)

print("Result: ", result.decode('utf-8'))

# output: crypto{r0undk3y}
