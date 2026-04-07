# Sprout Valley: 2D RPG Game | Python, Pygame, Tiled, Pixel art |
**RPG game where players can farm, harvest, chop trees, get apples and trade with daytime transition and weather changes.**

Sprout Land is an interactive 2D farming simulator built with Python and Pygame. Heavily inspired by the mechanics of Stardew Valley, this project serves as a deep dive into game architecture, specifically focusing on complex sprite grouping, z-index camera sorting, and state-driven player interactions. From chopping down trees to watering dirt patches that dry up with the morning sun, this game brings a functional slice of country life directly to your terminal.

#### To play
Downoad the whole repo and run the main.exe file

#### Dowload(For Devs)
Dowload the whole repo and run the main.py file in the code section to play the game

if the graphics look reversed do the following: 
1. got to code/support.py
2. replace the following snippets

remove
```python
def import_folder(path):

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
```
add replace it with
```python
def import_folder(path):

    if os.path.isdir(path):
        surface_list = []
        for _, __, img_files in walk(path):
            for image in img_files[::-1]:
                full_path = path + '/' + image
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
            surface_list.reverse()

        return surface_list

    else:
        raise Exception(f'{path} does not exist')
```

### How to play
- **arrow keys**  -  player movement
- **space** - tool use
- **q** - tool change
- **left control**  -  use seed
- **e** - seed change
- **enter** - trade, sleep

You start of in front of your house, use hoe and seeds to plant crops (dont forget to water them XD). chop down trees to get apples and wood. Trader is on the top left corner, you can trade stuff u farm for money or buy new seeds.

### Features
- Farming & growing (Multiple Tools and Seeds to use)
- Daytime cycle
- weather changes
- trees
- sounds
- animations

### Future plans
- Need to make a money bar showing how much money a player has
- Inventory show
- game phases
- SQL connection to save data and continue progress when start later on
