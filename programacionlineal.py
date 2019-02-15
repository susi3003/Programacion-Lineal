from pulp import *

x = LpVariable("x", 0, 3)
y = LpVariable("y", 0, 1)

prob = LpProblem("myProblem", LpMinimize)
prob += x + y <= 2

prob += -4*x + y

status = prob.solve()
assssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
print(value(x), value(y))
