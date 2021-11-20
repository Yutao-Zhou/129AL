#!/bin/bash

wget -q  http://web.physics.ucsb.edu/~phys129/lipman/ -O -| grep Latest | sed -e 's/<[^><]*>//g' -e 's/&nbsp;/ /'
