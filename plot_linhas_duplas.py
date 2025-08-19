import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [1, 3, 5, 7, 9]

plt.plot(x, y, label='Linha 1')
plt.plot(x, z, label='Linha 2')

plt.title('Exemplo com duas linhas')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
