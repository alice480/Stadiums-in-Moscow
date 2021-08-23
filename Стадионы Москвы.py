import os
import sys

import pygame
import requests

map_request = "https://static-maps.yandex.ru/1.x/?ll=37.617635,55.755814&z=11&size=450,450&l=map&pt=37.707593,55.812307,pm2rdm~37.559379,55.791243,pm2rdm~37.549354,55.713248,pm2rdm"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((450, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)