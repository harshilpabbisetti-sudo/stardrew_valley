import os.path
from os import walk
import pygame


def get_abs_path(path):
    game_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
    return game_folder_path + path


def import_folder(path):
    path = get_abs_path(path)
    if os.path.isdir(path):
        surface_list = []
        for _, __, img_files in walk(path):
            for image in img_files:
                full_path = path + '/' + image
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
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surf_dict[image.split('.')[0]] = image_surf

        return surf_dict
    else:
        raise Exception(f'{path} does not exist')
