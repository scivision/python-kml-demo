#!/usr/bin/env python
from kml_demo import kph2mps,demokml

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