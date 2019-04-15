#ifndef PYICP_H
#define PYICP_H

#include "icp.h"

double pyicp(double *fixed, int32_t num_fixed, double *moving, int32_t num_moving, double *rotation, double *translation);

#endif // PYICP_H
