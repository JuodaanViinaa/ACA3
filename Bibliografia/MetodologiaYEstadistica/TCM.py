from statistics import mean
import matplotlib.pyplot as plt
import random

# datos = []
# for i in range(100):
#     datos.append(random.randint(145, 180))
# print(mean(datos))
# 
# medias = []
# for _ in range(1000000):
#     muestra = random.sample(datos, 10)
#     media = mean(muestra)
#     medias.append(media)
# print(mean(medias))
# 
# plt.hist(medias, bins=50)
# plt.show()
datos = [165, 163, 160, 152, 160, 155, 156, 158, 165, 149, 182, 155, 150, 177, 
         159, 175, 163, 155, 152, 170, 161, 160, 173]

media_pob = mean(datos)
print(media_pob)

diferencias = []
for _ in range(1000000):
    muestra1 = random.sample(datos, 5)
    muestra2 = random.sample(datos, 5)
    media1 = mean(muestra1)
    media2 = mean(muestra2)
    diferencias.append(media1 - media2)
diferencia_media = mean(diferencias)

print(f"Diferencia entre medias: {diferencia_media}")

plt.hist(diferencias, bins=50, range=(-20, 20))
plt.show()
