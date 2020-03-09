import numpy as np
cimport pyicp
cimport numpy as np
from libc.stdlib cimport malloc, free

def icp(np.ndarray[double, ndim = 2, mode = 'c'] fixed not None, np.ndarray[double, ndim = 2, mode = 'c'] moving not None):

  m_fixed, n_fixed = fixed.shape[0], fixed.shape[1]
  m_moving, n_moving = moving.shape[0], moving.shape[1]

  assert n_fixed == 3
  assert n_moving == 3

  cdef double *rotation = <double *> malloc(9*sizeof(double))
  cdef double *translation = <double *> malloc(3*sizeof(double))
  cdef double resid

  with nogil:
     resid = pyicp(&fixed[0,0], m_fixed, &moving[0,0], m_moving, rotation, translation);

  transform = np.array([[rotation[0], rotation[1], rotation[2], translation[0]],[rotation[3], rotation[4], rotation[5], translation[1]],[rotation[6], rotation[7], rotation[8], translation[2]],[0.0, 0.0, 0.0, 1.0]])

  residual = np.array([resid])

  free(rotation)
  free(translation)

  return transform, residual


