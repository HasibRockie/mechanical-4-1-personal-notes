import numpy as np
import matplotlib.pyplot as plt

output_power = [216.24, 187.73, 205.19, 253.59, 292.90, 386.63, 369.41, 278.94, 252.32 ]

bsfc = [1.83, 2.11, 1.93, 1.56, 1.35, 1.02, 1.07, 1.42, 1.57]

exhaust_temp = [585.5, 584.5, 582.5, 473, 465, 471.5, 464, 500, 480]

x = []    
k = np.arange(min(output_power), max(output_power), 0.1)
y = np.poly1d(np.polyfit(output_power, exhaust_temp, 3))

for i in range(len(k)):
    x.append(y(k[i]))

plt.plot(k, x, '-', color = 'red', linewidth = 2, label = 'fitted curve')
plt.scatter(output_power, exhaust_temp, color='red', marker='o', s=50, label = 'Data point')

plt.xlabel('Electric Power Output (kW)')
plt.ylabel('Exhaust Temperature ($^oC$)')
plt.title('Fig 2 : Exhaust Temperature vs Electric Power Output')
plt.legend(loc='upper right')
plt.grid(True)
plt.show() 