import os
import os.path

def przegladanie(root):
    file_list = os.listdir(root)
    dir_list = []
    pliki_jednakowy_rozmiar = {}
    for item in file_list:
        if os.path.isfile(os.path.join(root, item)):
            full_name = os.path.join(root, item)
            file_size = os.path.getsize(full_name)
            print(full_name, file_size)
            pliki_jednakowy_rozmiar.setdefault(file_size, [])
            pliki_jednakowy_rozmiar[file_size].append(full_name)
        if os.path.isdir(os.path.join(root, item)):
            dir_list.append(item)
    print(pliki_jednakowy_rozmiar)
    for dirname in dir_list:
        przegladanie(os.path.join(root, dirname))


przegladanie('.')