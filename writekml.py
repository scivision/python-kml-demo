#!/usr/bin/env python
"""
this example assumes you're using simplekml 1.3 or newer
"""
from __future__ import division
from simplekml import Kml
import pandas as pd  #this is synthetic, normally you might read from file
import numpy as np
import sys
from tempfile import mkstemp
#
from pymap3d.vreckon import vreckon


def demokml(mps, Np, Ts, lon0, lat0, tstart, azim):
    t, lonLatAlt = sampledata(Np, mps, Ts, lon0, lat0, tstart, azim)

    kfn=makekml(t, lonLatAlt, lat0, lon0)

    return t,lonLatAlt,kfn

def makekml(t, lonLatAlt, lat0, lon0):

    assert isinstance(lonLatAlt,np.ndarray) and lonLatAlt.ndim==2 and lonLatAlt.shape[1]==3

    kml = Kml(name='My Kml',open=1)
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
    print('writing to '+kfn)
    kml.save(kfn)
    return kfn


def sampledata(Np,mps,Ts, lon0, lat0,tstart, azim):
    # mps: speed meters/sec
    # Np: number of points
    # Ts:
    freq = str(Ts) + 'S'
    tr = pd.date_range(tstart,periods=Np,freq=freq).to_pydatetime()
    t = [t.strftime('%Y-%m-%dT%H:%M:%S%Z') for t in tr]

    rng = mps * np.arange(0,Np*Ts,Ts)

    lonLatAlt = np.zeros((Np,3))
    lonLatAlt[:,1], lonLatAlt[:,0] = vreckon(lat0, lon0, rng, azim=azim)[:2]

    return t, lonLatAlt

def mph2mps(mph):
    return mph * 0.44704

def kph2mps(kph):
    return kph * 0.277778

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='example of writing a track with KML from external program data')
    p.add_argument('lat0',help='starting latitude of track',type=float)
    p.add_argument('lon0',help='starting longitude of track',type=float)
    p.add_argument('kph',help='speed of object in km/hour',type=float)
    p.add_argument('-t','--tstart',help='starting time of track in format %Y-%m-%dT%H:%M:%S',default='2014-01-01T00:00:00')
    p.add_argument('-n','--Np',help='number of points in track',type=int,default=25)
    p.add_argument('-T','--Ts',help='sample period [sec]',type=float,default=1)
    p.add_argument('-a','--azimuth',help='heading of track [deg]', type=float,default=145)
    a = p.parse_args()

    mps = kph2mps(a.kph)
    t,lonLatAlt = demokml(mps, a.Np, a.Ts, a.lon0, a.lat0, a.tstart, a.azimuth)

