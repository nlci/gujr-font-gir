#!/usr/bin/python3

from fontParts.world import *
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)

# Modify UFO
danda = font['u0AE6']
danda.name = 'zero.gujr'

## Omega
greek = font['uni03A9']
greek.unicode = 0x03A9
greek.unicodes = [greek.unicode]

# Save UFO
font.changed()
font.save()
font.close()
