import matplotlib.pyplot as plt

produtos = {
    'Maçã': 5,
    'Carne': 35,
    'Ovo': 25,
    'Queijo': 12
}

fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(list(produtos.keys()), list(produtos.values()), color='skyblue')

ax.set_title('Preços dos produtos')
ax.set_xlabel('Preço')
ax.set_ylabel('Produto')

for i, valor in enumerate(produtos.values()):
    ax.text(valor + 0.1, i, str(valor), va='center')

plt.show()