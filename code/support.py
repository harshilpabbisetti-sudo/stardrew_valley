import os.path
from os import walk
import pygame
import sys


def join(path_list):
    return os.path.join(*path_list)


def clean_path(path):
    # making path platform/os independent
    if "/" in path:
        os.path.join(*path.split('/'))

    elif "\\" in path:
        os.path.join(*path.split('/'))
    return os.path.normpath(path)


def get_abs_path(path):
    path = clean_path(path)
    # 1. Check if the game is running as a bundled executable
    if getattr(sys, 'frozen', False):
        # The root is the folder where the .exe itself lives
        game_folder_path = os.path.dirname(sys.executable)
    else:
        # The root is one level up from this script (development mode)
        game_folder_path = os.path.dirname(clean_path(os.path.dirname(os.path.abspath(__file__))))

    # 2. Use os.path.join instead of + to avoid slash errors between Windows/Mac
    return os.path.join(game_folder_path, path)


def import_folder(path):
    path = get_abs_path(path)
    if os.path.isdir(path):
        surface_list = []
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = join([path, image])
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
            surface_list.reverse()

        return surface_list

    else:
        raise Exception(f'{path} does not exist')


def import_folder_dict(path):
    path = get_abs_path(path)
    if os.path.isdir(path):
        surf_dict = {}
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = join([path, image])
                image_surf = pygame.image.load(full_path).convert_alpha()
                surf_dict[image.split('.')[0]] = image_surf

        return surf_dict
    else:
        raise Exception(f'{path} does not exist')
