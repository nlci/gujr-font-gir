#!/usr/bin/python3

from fontParts.world import *
from palaso.unicode.ucd import get_ucd
import sys

# Open UFO
ufo = sys.argv[1]
font = OpenFont(ufo)
print(f'Add anchors for {ufo}')

# Modify UFO

## Marks
above_x = below_x = None
above_marks = ['anusvara','candrabindu']
below_marks = ['nukta', 'anudatta']
for mark in above_marks + below_marks:
    glyph = font[mark]
    glyph.width = 0
    (xmin, ymin, xmax, ymax) = glyph.bounds
    xcenter = (xmin + xmax) / 2

    if mark in above_marks:
        if not above_x:
            x = above_x = xcenter
            y = above_y = ymin
        name = '_A'
    else:
        if not below_x:
            x = below_x = xcenter
            y = below_y = ymax
        name = '_B'
    glyph.appendAnchor(name, (x, y))

## Process all glyphs
bases = set()
for glyph in font:
    # remove anchors on imported indic characters
    if glyph.name.startswith('vedic'):
        for anchor in glyph.anchors:
            glyph.removeAnchor(anchor)

    # find bases
    for sep in ('.', '_'):
        base_name = glyph.name.partition(sep)[0]
        if not base_name:
            continue
        if base_name in font:
            base = font[base_name]
            if base.unicode:
                if get_ucd(base.unicode, 'na').startswith('GUJARATI') and get_ucd(base.unicode, 'InSC') in ('Vowel_Independent', 'Consonant'):
                    glyph.appendAnchor('A', (glyph.width + above_x, above_y))
                    glyph.appendAnchor('B', (glyph.width + below_x, below_y))
                    break

# Save UFO
font.changed()
font.save()
font.close()
