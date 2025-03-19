import os
import time

from config import *

order = input("Введите номер заказа: ") + "nc"
mun = float(input("Введите толщину прокладки: ").replace(",", "."))


if order in os.listdir(PATH):
    for i in os.listdir("{PATH}\\{order}".format(PATH=PATH, order=order)):
        if i.endswith(".mpr"):
            with open("{PATH}\\{order}\\{i}".format(PATH=PATH, order=order, i=i), "r") as file:
                s = file.read().split('tPODK=')
                podk = s[1].splitlines()
                podk[0] = '"{mun}"'.format(mun=mun)
                s = s[0] + 'tPODK=' + '\n'.join(podk)
            with open("{PATH}\\{order}\\{i}".format(PATH=PATH, order=order, i=i), "w") as file:
                file.write(s)
    print("Заказ:", order, "измененна")
    time.sleep(10)
else:
    print("Папка с таким названием отсутствует")
    time.sleep(10)
