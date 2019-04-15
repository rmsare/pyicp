#include "pyicp.h"
#include "icp.h"

double pyicp(double *fixed, int32_t num_fixed, double *moving, int32_t num_moving, double *rotation, double *translation) {

  Matrix R = Matrix::eye(3);
  Matrix t(3,1);

  IcpPointToPlane icp(fixed, num_fixed, 3);
  double residual = icp.fit(moving, num_moving, R, t, -1);
  R.getData(rotation);
  t.getData(translation);
  return residual;

}

