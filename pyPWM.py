import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,101)
y = np.sin(x)+1

freq = 100/10
x1 = x[::10]
y1 = y[::10]

amplitud = 2
porcentaje = y1/amplitud
# print(porcentaje)

t=np.linspace(0,10,1100)
# print(t)
porcen = porcentaje*100
p = [int(x) for x in porcen]
output = []
for i in p[0]:
    index = 0
    for j in range(100):
        if j<=i:
            output.append(0)
        else:
            output.append(amplitud)
        index += 1

print(output)
plt.plot(t, output)
plt.plot(x, y)
plt.plot(x1, porcentaje*2)
plt.show()
#print(int(porcen))

# print(x[::10])

# plt.plot(x, y)
# plt.plot(x1, y1)
# plt.show()