n = 10000

import numpy as np

npts = int(np.sqrt(n))

[X, Y] = np.meshgrid(np.arange(-2,2,4.0/npts),np.arange(-2,2,4.0/npts))

Z = 5*X*np.exp(-X*X-Y*Y)

XYZ = np.zeros((np.power(npts,2),3))
XYZ[:,0] = np.reshape(X,np.power(npts,2),1)
XYZ[:,1] = np.reshape(Y,np.power(npts,2),1)
XYZ[:,2] = np.reshape(Z,np.power(npts,2),1)

XT = X - 1.0
YT = Y - 0.5
ZT = Z + 1.0

XYZT = np.zeros((np.power(npts,2),3))
XYZT[:,0] = np.reshape(XT,np.power(npts,2),1)
XYZT[:,1] = np.reshape(YT,np.power(npts,2),1)
XYZT[:,2] = np.reshape(ZT,np.power(npts,2),1)

from pyicp import icp

transform, residual = icp(XYZ, XYZT)

print(transform)
print(residual)

