from math import sqrt
def magnitude(v,w):
    return sqrt(sum([(v_i-w_i)**2
            for v_i,w_i in zip(v,w)]))

print(magnitude([1,2,4],[5,6,6]))