#Dot Product
from collections import defaultdict

def dot(v,w):
    return sum([v_i*w_i
            for v_i,w_i in zip(v,w)])

print (dot([1,2,3],[4,5,6]))

#Vector Product

def vector_product(v,w):
    adder = defaultdict(int)
    for n_1,v_i in enumerate(v):
        for n_2,w_i in enumerate(w):
            if (n_1!=n_2):
                if (n_1==0 and n_2==1):
                    rectangular_component="k"
                    num = 1
                elif (n_1==1 and n_2==2):
                    rectangular_component="i"
                    num = 1
                elif (n_1==2 and n_2==0):
                    rectangular_component="j"
                    num=1
                elif (n_1==1 and n_2==0):
                    rectangular_component="k"
                    num = -1
                elif (n_1==0 and n_2==2):
                    rectangular_component="j"
                    num = -1
                else:
                    rectangular_component="i"
                    num = -1
                adder[rectangular_component]+= v_i*w_i*num
                #list.append(str(v_i*w_i*num)+(rectangular_component))
    return (adder)

print(vector_product([1,2,3],[4,5,6]))#Dot Product
from collections import defaultdict

def dot(v,w):
    return sum([v_i*w_i
            for v_i,w_i in zip(v,w)])

print (dot([1,2,3],[4,5,6]))

#Vector Product

def vector_product(v,w):
    adder = defaultdict(int)
    for n_1,v_i in enumerate(v):
        for n_2,w_i in enumerate(w):
            if (n_1!=n_2):
                if (n_1==0 and n_2==1):
                    rectangular_component="k"
                    num = 1
                elif (n_1==1 and n_2==2):
                    rectangular_component="i"
                    num = 1
                elif (n_1==2 and n_2==0):
                    rectangular_component="j"
                    num=1
                elif (n_1==1 and n_2==0):
                    rectangular_component="k"
                    num = -1
                elif (n_1==0 and n_2==2):
                    rectangular_component="j"
                    num = -1
                else:
                    rectangular_component="i"
                    num = -1
                adder[rectangular_component]+= v_i*w_i*num
                #list.append(str(v_i*w_i*num)+(rectangular_component))
    return (adder)

print(vector_product([1,2,3],[4,5,6]))