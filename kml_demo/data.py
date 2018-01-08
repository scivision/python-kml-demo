import numpy as np
import pandas as pd  #this is for testing only, normally you might read from file
#
from pymap3d.vincenty import vreckon


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
