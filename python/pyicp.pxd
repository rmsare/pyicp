# pyicp.pxd

cdef extern from "pyicpp.h":
    ctypedef signed int int32_t;
    double pyicp(double *fixed, int32_t num_fixed, double *moving, int32_t num_moving, double *rotation, double *translation)

