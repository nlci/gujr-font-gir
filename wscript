# gir

# set folder names
out='results'
TESTDIR='tests'
STANDARDS='tests/reference'

# set meta-information
script='gujr'
APPNAME='nlci-' + script
VERSION='0.101'
TTF_VERSION='0.101'
COPYRIGHT='Copyright (c) 2009-2018, NLCI (http://www.nlci.in/fonts/)'

DESC_SHORT='Gujarati Unicode font with OT support'
DESC_LONG='''
Pan Gujarati font designed to support all the languages using the Gujarati script.
'''
DESC_NAME='NLCI-' + script
DEBPKG='fonts-nlci-' + script

# set test parameters
TESTSTRING=u'\u0a95'

# set fonts to build
faces = ('Gir',)
styles = ('-R', '-B', '-I')
stylesName = ('Regular', 'Bold', 'Italic')

# set build parameters
fontbase = 'source/'
tag = script.upper()

for f in faces:
    for (s, sn) in zip(styles, stylesName):
        font(target = process(tag + f + '-' + sn.replace(' ', '') + '.ttf',
                name(tag + ' ' + f, lang='en-US', subfamily=(sn))
                ),
            source = fontbase + f + s + '.sfd',
            opentype = fea(fontbase + f + s + '.fea', no_make = True),
            #graphite = gdl(fontbase + f + s + '.gdl',
            #    master = fontbase + 'master.gdl',
            #    make_params = '-p 1 -s 2 -l first',
            #    params = '-d -v2'
            #    ),
            #classes = fontbase + 'gir_classes.xml',
            ap = f + s + '.xml',
            version = TTF_VERSION,
            copyright = COPYRIGHT,
            license = ofl('Gir', 'NLCI'),
            woff = woff(),
            script = 'gujr',
            fret = fret(params = '-r')
        )
