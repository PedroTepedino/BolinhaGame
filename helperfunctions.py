import random
from graphics import color_rgb


def get_random_color() -> color_rgb:
    return color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))