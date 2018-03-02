def add_vectors(v,w):
    return [v_i+w_i for v_i,w_i in zip(v,w)]

vec_1=[1,2,3]
vec_2=[4,-5,7]

print(add_vectors(vec_1,vec_2))

#another way of vector adition

from operator import add

def add_vectors_1(v,w):
    return list(map(add,v,w))

print(add_vectors_1(vec_1,vec_2))



#subtration of vectors

def sub_vectors(v,w):
    return [v_i-w_i for v_i,w_i in zip(v,w)]

vec_1=[1,2,3]
vec_2=[4,-5,7]

print(sub_vectors(vec_1,vec_2))

#another way of vector subtration

from operator import sub

def subtract_vectors_1(v,w):
    return list(map(sub,v,w))

print(subtract_vectors_1(vec_1,vec_2))

