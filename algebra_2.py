list_of_vectors=[[1,2,3],[4,5,6],[5,7,8],[3,8,9]]

from operator import add
from functools import reduce

def vector_sum(vectors):
    result=vectors[0]
    for x in vectors[1:]:
        result=list(map(add,result,x))
    return result


from operator import add

def add_vectors_1(v,w):
    return list(map(add,v,w))



print(vector_sum(list_of_vectors))

"""Another way of doing vectors addition is by using
reduce method which takes 2 arguments , one is the function and 
2nd is the "single" list on which function is applied"""

""""Here we cant pass "vector_sum function in 1st argument
of reduce function beause it receives a function which is applied
b/w two variable"""

def vector_sum1(vectors):
    return reduce(add_vectors_1,vectors)

print(vector_sum1(list_of_vectors))
