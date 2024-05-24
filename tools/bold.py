#!/usr/bin/python3

import fontforge
import argparse


def main():
    parser = argparse.ArgumentParser(description='Check character inventory of a TTF font')
    parser.add_argument('sfd', help='SFD file to modify')
    parser.add_argument('glyphs', help='Glyphs to process', nargs='+')
    parser.add_argument('--version', action='version', version='%(prog)s ' + '0.1')
    args = parser.parse_args()

    print(f'Faking bold in {args.sfd}')
    font = fontforge.open(args.sfd)
    for glyph_name in args.glyphs:
        print(glyph_name)
        glyph = font[glyph_name]
        glyph.changeWeight(15)
        # glyph.genericGlyphChange('horizontalVertical', stemHeightScale=1.1, stemWidthScale=1.5)
    font.save()


if __name__ == '__main__':
    main()
