from writekml import demokml,kph2mps

kph=1; Np=25; Ts=1; lon0=-100; lat0=50; tstart='2014-01-01T00:00:00';azim=145
mps = kph2mps(kph)
t,lonLatAlt,kfn = demokml(mps, Np, Ts, lon0, lat0, tstart, azim)
#%% spot check
with open(kfn,'r') as f:
    txt = f.readlines()

assert txt[26].strip() == '<when>2014-01-01T00:00:18</when>'
# python 2 and python 3 have different digits of precision observed here, is this
# an issue with simplekml or just inherent?
t47 = txt[47].split()
assert t47[0][:24] == '<gx:coord>-99.9999688883'
assert t47[1][:13] == '49.9999713601'
assert t47[2] =='0.0</gx:coord>'
