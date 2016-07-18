#!/usr/bin/env python
from numpy.testing import assert_allclose
from writekml import demokml,kph2mps

kph=100; Np=25; Ts=1; lon0=-100; lat0=50; tstart='2014-01-01T00:00:00';azim=145
mps = kph2mps(kph)
t,lonLatAlt,kfn = demokml(mps, Np, Ts, lon0, lat0, tstart, azim)
#%% spot check
with open(kfn,'r') as f:
    txt = f.readlines()

assert txt[26].strip() == '<when>2014-01-01T00:00:18</when>'
# python 2 and python 3 have different digits of precision observed here, is this
# an issue with simplekml or just inherent?
t47 = txt[47].split()
assert_allclose(float(t47[0].split('>')[1]),-99.9968890147576)
assert_allclose(float(t47[1]),49.99713596348202) #rounding difference between py2/3
assert float(t47[2].split('<')[0]) == 0
