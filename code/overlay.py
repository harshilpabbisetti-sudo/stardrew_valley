import pygame
from settings import *
from support import get_abs_path


class Overlay:
    def __init__(self, player):

        # general setup
        self.display_surf = pygame.display.get_surface()
        self.player = player

        # imports
        overlay_path = get_abs_path('graphics/overlay/')
        self.tool_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        self.seed_surf = {seed: pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}

    def display(self):
        # tool
        tool_surf = self.tool_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom=OVERLAY_POSITIONS['tool'])
        self.display_surf.blit(tool_surf, tool_rect)

        # seed
        seed_surf = self.seed_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom=OVERLAY_POSITIONS['seed'])
        self.display_surf.blit(seed_surf, seed_rect)
