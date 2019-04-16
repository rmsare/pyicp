# pyicp.pxd

cdef extern from "pyicpp.h":
    double pyicp(double *fixed, int num_fixed, double *moving, int num_moving, double *rotation, double *translation)

