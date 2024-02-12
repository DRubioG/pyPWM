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

t=np.linspace(0,10,1000)
# print(t)
porcen = porcentaje*100
p = [int(x) for x in porcen]
output = []

for i in p[:-1]:
    for j in range(100):
        
        if (100-j)<=i:
            output.append(amplitud)
        else:
            output.append(0)
        print(j, i, output[-1])


def PWM(signal_input, amplitud = 2,period = 10, N_samples = 1000):
    porcentaje = y1/amplitud
    # print(porcentaje)

    t=np.linspace(0, period, N_samples)
    # print(t)
    porcen = porcentaje*100
    p = [int(x) for x in porcen]
    output = []

    for i in p[:-1]:
        for j in range(100):
            
            if (100-j)<=i:
                output.append(amplitud)
            else:
                output.append(0)
            print(j, i, output[-1])

    return output





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