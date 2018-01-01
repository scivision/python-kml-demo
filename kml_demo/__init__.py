#!/usr/bin/env python
"""
this example assumes you're using simplekml 1.3 or newer
"""
from simplekml import Kml
import pandas as pd  #this is for testing only, normally you might read from file
import numpy as np
from tempfile import mkstemp
#
from pymap3d.vincenty import vreckon


def demokml(mps, Np, Ts, lon0, lat0, tstart, azim):
    t, lonLatAlt = sampledata(Np, mps, Ts, lon0, lat0, tstart, azim)

    makekml(t, lonLatAlt, lat0, lon0)

    return t,lonLatAlt


def makekml(t, lonLatAlt, lat0, lon0):

    assert isinstance(lonLatAlt,np.ndarray) and lonLatAlt.ndim==2 and lonLatAlt.shape[1]==3

    kml = Kml(name='My Kml')
#    doc = kml.newdocument(name='My Doc',snippet=Snippet('snippet'))
#    doc.lookat.gxtimespan.begin = t[0]
#    doc.lookat.gxtimespan.end = t[-1]
#    doc.lookat.latitude = lat0
#    doc.lookat.longitude = lon0
#    doc.lookat.range = 1e3

    #fol = kml.newfolder(name='My Tracks')

    trk = kml.newgxtrack(name='My Track')
    trk.newwhen(t)
    trk.newgxcoord(lonLatAlt.tolist()) #list of lon,lat,alt, NOT ndarray!

    # Styling (from simplekml docs)
#    trk.stylemap.normalstyle.iconstyle.icon.href = 'http://earth.google.com/images/kml-icons/track-directional/track-0.png'
#    trk.stylemap.normalstyle.linestyle.color = '99ffac59'
#    trk.stylemap.normalstyle.linestyle.width = 6
#    trk.stylemap.highlightstyle.iconstyle.icon.href = 'http://earth.google.com/images/kml-icons/track-directional/track-0.png'
#    trk.stylemap.highlightstyle.iconstyle.scale = 1.2
#    trk.stylemap.highlightstyle.linestyle.color = '99ffac59'
#    trk.stylemap.highlightstyle.linestyle.width = 8
    kfn=mkstemp(suffix='.kml')[1]
    print('writing to',kfn)
    kml.save(kfn)


def sampledata(Np,mps,Ts, lon0, lat0,tstart, azim):
    # mps: speed meters/sec
    # Np: number of points
    # Ts:
    freq = f'{Ts}S'
    tr = pd.date_range(tstart,periods=Np,freq=freq).to_pydatetime()
    t = [t.isoformat(timespec='seconds') for t in tr]

    rng = mps * np.arange(0,Np*Ts,Ts)

    lonLatAlt = np.zeros((Np,3))
    lonLatAlt[:,1], lonLatAlt[:,0] = vreckon(lat0, lon0, rng, azim=azim)[:2]

    return t, lonLatAlt


def mph2mps(mph):
    return mph * 0.44704


def kph2mps(kph):
    return kph * 0.277778


