#!/usr/bin/env python3

import colorsys
import math


class Color:
    def __init__(self, rgb):
        self.__r, self.__g, self.__b = rgb
        self.__hls = colorsys.rgb_to_hls(self.__r / 255, self.__g / 255,
                                         self.__b / 255)

    @staticmethod
    def fromHSL(hue, saturation, luminosity):
        rgb = colorsys.hls_to_rgb(hue, luminosity, saturation)
        rgb = list(map(lambda color: math.floor(color * 255), rgb))
        return Color(rgb)

    @property
    def hexcode(self):
        return '#{:02x}{:02x}{:02x}'.format(self.__r, self.__g, self.__b)

    @property
    def whiteness(self):
        return self.__r + self.__g + self.__b

    @property
    def saturation(self):
        return self.__hls[2]

    @property
    def hue(self):
        return self.__hls[0]

    @property
    def luminosity(self):
        return self.__hls[1]
