#Multiplication of a vector by a constant

def multiply(c,vector):
    return [c*v for v in vector]

print(multiply(3,[1,2,3,4]))

#Division of a vectors

def divide(v,w):
    return [v_i/w_i for v_i,w_i in zip(v,w)]

print(divide([2,4,6],[1,2,3]))