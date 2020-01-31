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


# Generate complementary colors to existing buckets so that there are 7 buckets
# in total.
def __generate_color_buckets(existing_buckets):
    return existing_buckets


# Merge color buckets so that there are 7 buckets in total.
def __merge_color_buckets(existing_buckets):
    # Merge small buckets until we only have 7 buckets.
    while len(existing_buckets) > 7:
        buckets = []
        smallest_bucket_index = 0
        for i in range(1, len(existing_buckets) - 1):
            print(i)
            if len(existing_buckets[i]) < len(
                    existing_buckets[smallest_bucket_index]):
                smallest_bucket_index = i
    return existing_buckets


# Generates 16 colors perfect for a terminal from a given image.
def generate(image_file_path):
    image = __get_thumbnail(image_file_path)
    colors = __get_colors(image)

    # Get highlight and shadow color groups, sorted by saturation.
    highlights = [colors[-1]]
    shadows = [colors[0]]
    for i in range(math.floor(len(colors) / 2)):
        if colors[i].whiteness - shadows[0].whiteness < 30:
            shadows.append(colors[i])
        highlight_index = len(colors) - 1 - i
        if highlights[0].whiteness - colors[highlight_index].whiteness < 40:
            highlights.append(colors[highlight_index])
    highlights.sort(key=lambda color: color.saturation)
    shadows.sort(key=lambda color: color.saturation)

    # Set the background and foreground colors.
    bg_color = shadows[0]
    fg_color = highlights[-1]

    # Remove highlights and shadows from colors.
    colors = colors[len(shadows):-len(highlights)]

    # Set black and bright black.
    black = colors[0]
    bright_black = colors[1]

    # Remove all colors that are close in whiteness to black and bright black.
    index = 0
    while colors[index].whiteness - bright_black.whiteness < 60:
        index = index + 1
    colors = colors[index:]

    # Sort the colors into hue buckets.
    buckets = [[colors[0]]]
    colors.sort(key=lambda color: color.hue)
    for color in colors[1:]:
        if abs(buckets[-1][-1].hue - color.hue) < .05:
            buckets[-1].append(color)
        else:
            buckets.append([color])

    # Split any buckets with >=4 colors into two by saturation and merge any
    # buckets that only have 1 color.
    temp_buckets = []
    for bucket in buckets:
        bucket.sort(key=lambda color: color.saturation)
        if len(bucket) >= 4:
            mid_index = math.floor(len(bucket) / 2)
            temp_buckets.append(bucket[0:mid_index])
            temp_buckets.append(bucket[mid_index + 1:])
        else:
            temp_buckets.append(bucket)
    buckets = temp_buckets

    # If we have 7 buckets, then we're all set. Otherwise, we need to generate
    # some colors.
    if len(buckets) < 7: buckets = __generate_color_buckets(buckets)
    if len(bucket) > 7: buckets = __merge_color_buckets(buckets)

    print('background color = %s\nforeground color = %s' %
          (bg_color.hexcode, fg_color.hexcode))
    print('black = %s\nbright black = %s' %
          (black.hexcode, bright_black.hexcode))

    for bucket in buckets:
        print()
        for color in bucket:
            print('%s %s' % (color.hexcode, color.hue))
