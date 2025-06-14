#!/usr/bin/python3
# this is a smith configuration file

# gir

# command line options
opts = preprocess_args(
    {'opt' : '-l'}, # build fonts from legacy for inclusion into final fonts
    {'opt' : '-r'}, # only build the regular font
    )

import os2

# override the default folders
DOCDIR = ['documentation', 'web']

# set meta-information
script='gujr'
APPNAME='nlci-' + script

DESC_SHORT='Gujarati Unicode font with OT support'
DESC_NAME='NLCI-' + script
getufoinfo('source/Gir-Regular.ufo')
# BUILDLABEL = 'beta1'

# Set up the FTML tests
ftmlTest('tools/ftml-smith.xsl')

# set fonts to build
faces = ('Gir',)
facesLegacy = ('GIRR',)
styles = ('-R', '-B', '-I')
stylesName = ('Regular', 'Bold', 'Italic')
stylesLegacy = ('', 'BD', 'I')
dspaces = ('Roman', 'Italic')

# set build parameters
fontbase = 'source/'
archive = fontbase + 'archive/unhinted/'
generated = 'generated/'
tag = script.upper()

panose = [2, 0, 0, 3]
codePageRange = [0, 29]
unicodeRange = [0, 1, 2, 3, 5, 6, 7, 15, 18, 31, 32, 33, 35, 38, 39, 40, 45, 60, 62, 67, 69, 91]
hackos2 = os2.hackos2(panose, codePageRange, unicodeRange)

if '-l' in opts:
    for f, fLegacy in zip(faces, facesLegacy):
        for (s, sn, sLegacy) in zip(styles, stylesName, stylesLegacy):
            missing_style = sLegacy
            if missing_style == 'BD':
                missing_style = ''
            missing = '../' + archive + fLegacy + missing_style + '.ttf'
            font(target = process('ufo/' + f + '-' + sn.replace(' ', '') + '.ttf',
                    cmd(hackos2 + ' ${DEP} ${TGT}'),
                    name(f, lang='en-US', subfamily=(sn))
                    ),
                source = legacy(f + s + '.ttf',
                                source = archive + fLegacy + sLegacy + '.ttf',
                                xml = fontbase + 'gir_unicode.xml',
                                params = ' -f ' + missing,
                                noap = '')
                )

if '-l' in opts:
    faces = list()
for f in faces:
    p = package(
        appname = APPNAME + '-' + f.lower(),
        version = VERSION,
        docdir = DOCDIR # 'documentation'
    )
    for dspace in dspaces:
        d = designspace('source/' + f + dspace + '.designspace',
            target = process('${DS:FILENAME_BASE}.ttf',
                cmd('psfchangettfglyphnames ${SRC} ${DEP} ${TGT}', ['source/${DS:FILENAME_BASE}.ufo'])
            ),
            instances = ['Gir Regular'] if '-r' in opts else None,
            opentype=fea(generated + '${DS:FILENAME_BASE}.fea',
                mapfile = generated + '${DS:FILENAME_BASE}.map',
                master = fontbase + 'main.feax',
                make_params = ''
                ),
            #graphite = gdl(generated + '${DS:FILENAME_BASE}.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2',
            #    params =  '-e ${DS:FILENAME_BASE}_gdlerr.txt'
            #    ),
            #classes = fontbase + 'gir_classes.xml',
            #ap = generated + '${DS:FILENAME_BASE}.xml',
            version = VERSION,
            woff = woff('woff/${DS:FILENAME_BASE}', type='woff2',
                metadata = '../source/${DS:FAMILYNAME_NOSPC}-WOFF-metadata.xml'),
            script = 'gjr2', # 'gujr'
            package = p,
            pdf = fret(params = '-oi')
        )
