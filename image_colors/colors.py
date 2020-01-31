#!/usr/bin/env python3

from PIL import Image
import math
from .color import Color


# Get thumbnail version of an image given the image path.
def __get_thumbnail(image_file_path):
    max_image_dimension = 10
    image = Image.open(image_file_path)
    image_width, image_height = image.size

    thumbnail_width = image_width
    thumbnail_height = image_height
    if image_width > image_height:
        thumbnail_width = max_image_dimension
        thumbnail_height = math.floor(image_height / image_width *
                                      max_image_dimension)
    else:
        thumbnail_height = max_image_dimension
        thumbnail_width = math.floor(image_width / image_height *
                                     max_image_dimension)

    return image.resize((thumbnail_width, thumbnail_height), Image.LANCZOS)


# Get unique Color objects for each pixel in a given image sorted by whitenes
# (from least white to whitest).
def __get_colors(image):
    pixels = image.load()
    rgb_colors = []
    image_width, image_height = image.size
    for x in range(image_width):
        for y in range(image_height):
            rgb_colors.append(pixels[x, y])
    rgb_colors = list(dict.fromkeys(rgb_colors))
    colors = list(map(lambda rgb: Color(rgb), rgb_colors))
    colors.sort(key=lambda color: color.whiteness)
    return colors


# Generates 16 colors perfect for a terminal from a given image.
def generate(image_file_path):
    image = __get_thumbnail(image_file_path)
    colors = __get_colors(image)

    # Set the background and foreground colors.
    bg_color = colors[0]
    fg_color = colors[-1]
    print('background color = %s\nforeground color = %s' %
          (bg_color.hexcode, fg_color.hexcode))

    # Remove the background and foreground colors as well as all the colors
    # that are similar in whiteness to these two colors from the list.
    colors = colors[1:-1]
    new_start_index = 0
    new_end_index = len(colors) - 1
    while (colors[new_start_index].whiteness - bg_color.whiteness < 40):
        new_start_index = new_start_index + 1
    while (fg_color.whiteness - colors[new_end_index].whiteness < 40):
        new_end_index = new_end_index - 1
    colors = colors[new_start_index:new_end_index]

    # Set black and bright black.
    black = colors[0]
    bright_black = colors[1]
    print('black = %s\nbright black = %s' %
          (black.hexcode, bright_black.hexcode))

    for color in colors:
        print('%s %s' % (color.hexcode, color.whiteness))
