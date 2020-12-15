import matplotlib.pyplot as plt

data = {'A': 19, 'H': 21, 'C': 20, 'F': 30}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('numero di studenti delle classi')


plt.show()