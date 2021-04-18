from functools import reduce

dados = [2,5,6,9,10,22,1,3]
multi = lambda x,y: x * y
res = reduce(multi,dados)
print(res)