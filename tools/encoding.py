#!/usr/bin/python3

import fontParts.world as fontparts
import sys

# Open UFO
ufo = sys.argv[1]
font = fontparts.OpenFont(ufo)

# Modify UFO
for glyph in font:
    if glyph.name == 'ra_virama':
        glyph.name = 'reph'
    elif glyph.name.startswith('ra_umatra'):
        pass
    elif glyph.name.startswith('ra_uumatra'):
        pass
    elif glyph.name.startswith('ra_'):
        glyph.name = 'reph_' + glyph.name.removeprefix('ra_') # ligature with reph
    elif glyph.name.startswith('virama_ra'):
        glyph.name = glyph.name.replace('virama_ra', 'vattu')

# Save UFO
font.changed()
font.save()
font.close()
