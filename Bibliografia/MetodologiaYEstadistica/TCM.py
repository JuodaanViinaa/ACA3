from statistics import mean
import matplotlib.pyplot as plt
import random

datos = []
for i in range(100):
    datos.append(random.randint(145, 180))
print(mean(datos))

medias = []
for _ in range(1000000):
    muestra = random.sample(datos, 10)
    media = mean(muestra)
    medias.append(media)
print(mean(medias))

plt.hist(medias, bins=50)
plt.show()
