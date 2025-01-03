# Домашнее задание по теме "Файлы в операционной системе"

import time

from os import getcwd
from os import walk
from os.path import join
from os.path import getmtime
from os.path import dirname
from os.path import getsize

directory = getcwd()

for root, dirs, files in walk(directory):
    for file in files:
        filepath = join(directory, file)
        filetime = getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = getsize(file)
        parent_dir = dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')