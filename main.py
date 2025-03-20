import os
import time
import re

PATH = "C:\\VirtualBox\\Virtual_share\\FasadBG_it\\Fasad\\bin\\Debug\\nc"


order = input("Введите номер заказа: ") + "nc"
freza = input("Введите номер фрезы: ")
speed = int(input("Введите скорость подачи: "))


def modify_file(filename, freza, speed):
    with open(filename, 'r') as file:
        lines = file.readlines()

    modified = False
    i = 0
    while i < len(lines):
        if 'TNO="{freza}"'.format(freza=freza) in lines[i]:
            # Ищем ближайший F_="X" (X=1-8) в последующих строках
            for j in range(i + 1, len(lines)):
                if re.search(r'F_="[1-8]"', lines[j]):
                    lines[j] = re.sub(r'(F_=)"[1-8]"', r'\1"{speed}"'.format(speed=speed), lines[j])
                    modified = True
                    i = j  # Перескакиваем обработанные строки
                    break
                # Прерываем поиск при новых параметрах или конце блока
                elif 'TNO="' in lines[j] or '\\' in lines[j]:
                    break
        i += 1

    if modified:
        with open(filename, 'w') as file:
            file.writelines(lines)
        print("Файл успешно изменён.")
        time.sleep(1)
        exit()
    else:
        print("Изменений не требуется.")
        time.sleep(1)
        exit()


if order in os.listdir(PATH):
    for i in os.listdir("{PATH}\\{order}".format(PATH=PATH, order=order)):
        if i.endswith(".mpr"):
            with open("{PATH}\\{order}\\{i}".format(PATH=PATH, order=order, i=i), "r") as file:
                modify_file("{PATH}\\{order}\\{i}".format(PATH=PATH, order=order, i=i), freza, speed)


