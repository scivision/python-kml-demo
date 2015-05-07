from writekml import demokml,kph2mps

kph=1; Np=25; Ts=1; lon0=-100; lat0=50; tstart='2014-01-01T00:00:00';azim=145
mps = kph2mps(kph)
t,lonLatAlt,kfn = demokml(mps, Np, Ts, lon0, lat0, tstart, azim)
#%% spot check
with open(kfn,'r') as f:
    txt = f.readlines()

assert txt[26].strip() == '<when>2014-01-01T00:00:18</when>'
assert txt[47].strip() == '<gx:coord>-99.99996888832626 49.99997136006237 0.0</gx:coord>'
