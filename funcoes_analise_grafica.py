import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,100)

fig, ax = plt.subplots()

# Função linear (y = x)
ax.plot(x, x, label='linear')

# Função quadrática (y = x²)
ax.plot(x, x**2, label='quadratic')

# Função cúbica (y = x³)
ax.plot(x, x**3, label='cubic')

ax.set_xlabel('x label') # apelido do eixo das abscissas (x)
ax.set_ylabel('y label') # apelido do eixo das ordenadas (y)
ax.set_title('Simple Plot') # titulo graf.
ax.legend() # exibe legenda

plt.show() # exibe grafico 
