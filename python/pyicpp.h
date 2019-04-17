#ifndef PYICPP_H
#define PYICPP_H

#include "icp.h"
#include "matrix.h"

double pyicp(double *fixed, int32_t num_fixed, double *moving, int32_t num_moving, double *rotation, double *translation);

#endif // PYICPP_H
