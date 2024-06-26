#!/bin/bash

face="$1"
style="$2"
ufo="$3"

devaf="Maurya"
kndaf="Badami"
tamlf="Vaigai"

psfcopyglyphs -f --rename rename --unicode usv -i ${cs}/panini/main4gujr.csv -s "${deva}/${devaf}-${style}.ufo" ${ufo}
psfcopyglyphs -f --rename rename --unicode usv -i ${cs}/badami/main4gujr.csv -s "${knda}/${kndaf}-${style}.ufo" ${ufo}
psfcopyglyphs -f --rename rename --unicode usv -i ${cs}/thiruvalluvar/main.csv -s "${taml}/${tamlf}-${style}.ufo" ${ufo}
