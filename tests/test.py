#!/usr/bin/env python
from numpy.testing import assert_allclose
from fastkml import kml
"""
FastKML does NOT support track
https://github.com/cleder/fastkml/issues/37
"""
from kml_demo import kph2mps,makekml
from kml_demo.data import sampledata

ofn = 'test.kml'

kph=100
Np=25
Ts=1
lon0=-100
lat0=50
tstart='2014-01-01T00:00:00';azim=145

def demokml(mps, Np, Ts, lon0, lat0, tstart, azim):
    t, lonLatAlt = sampledata(Np, mps, Ts, lon0, lat0, tstart, azim)

    makekml(t, lonLatAlt, lat0, lon0, ofn)

    return t,lonLatAlt

mps = kph2mps(kph)
t,lonLatAlt = demokml(mps, Np, Ts, lon0, lat0, tstart, azim)
#%% spot check
with open(ofn, 'r') as f:
    txt = f.readlines()

with open(ofn, 'rb') as f:
    btxt = f.read()

k = kml.KML()
k.from_string(btxt)

assert txt[25].strip() == '<when>2014-01-01T00:00:18</when>'
# python 2 and python 3 have different digits of precision observed here, is this
# an issue with simplekml or just inherent?
t47 = txt[46].split()
assert_allclose(float(t47[0].split('>')[1]),-99.9968890147576)
assert_allclose(float(t47[1]),49.99713596348202) #rounding difference between py2/3
assert float(t47[2].split('<')[0]) == 0
