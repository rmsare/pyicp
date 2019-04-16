#ifndef PYICP_H
#define PYICP_H

#include "icp.h"

double pyicp(double *fixed, int num_fixed, double *moving, int num_moving, double *rotation, double *translation);

#endif // PYICP_H
