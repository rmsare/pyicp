import numpy as np
import copy, imp, os

pylibicp = imp.load_dynamic("pylibicp",os.path.join(__path__[0],"python/pylibicp.so"))

def icp(fixed , moving):
   assert(isinstance(fixed,np.ndarray) and isinstance(moving,np.ndarray))
   assert(fixed.shape[1] == 3 and moving.shape[1] == 3)
   from pylibicp import icp_interface
   fixed = np.unique(copy.deepcopy(fixed), axis=0)
   moving = np.unique(copy.deepcopy(moving),axis=0)
   return icp_interface(fixed,moving)
