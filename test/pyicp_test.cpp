#include <iostream>
#include "pyicp.h"

using namespace std;

int main (int argc, char** argv) {

  // define a 3 dim problem with 10000 model points
  // and 10000 template points:
  int32_t dim = 3;
  int32_t num = 10000;

  double dd = 4.0 / sqrt(num);
  cout << "dd: " << dd << endl;
  // allocate model and template memory
  double* M = (double*)calloc(3*num,sizeof(double));
  double* T = (double*)calloc(3*num,sizeof(double));

  // set model and template points
  cout << endl << "Creating model with 10000 points ..." << endl;
  cout << "Creating template by shifting model by (1,0.5,-1) ..." << endl;
  int32_t k=0;
  for (double x=-2; x<2; x+=dd) {
    for (double y=-2; y<2; y+=dd) {
      double z=5*x*exp(-x*x-y*y);
      M[k*3+0] = x;
      M[k*3+1] = y;
      M[k*3+2] = z;
      T[k*3+0] = x-1;
      T[k*3+1] = y-0.5;
      T[k*3+2] = z+1;
      k++;
    }
  }

  double *R = (double*)calloc(9,sizeof(double));
  double *t = (double*)calloc(3,sizeof(double));

  double residual = pyicp(M, num, T, num, R, t);

  // results
  cout << endl << "Transformation results:" << endl;
  cout << "R:" << endl << R[0] << " " << R[1] << " " << R[2] << endl;
  cout << R[3] << " " << R[4] << " " << R[5] << endl;
  cout << R[6] << " " << R[7] << " " << R[8] << endl << endl;
  cout << "t:" << endl << t[0] << " " << t[1] << " " << t[2] << endl << endl;
  cout << "Residual:"<<residual;

  // free memory
  free(M);
  free(T);

  // success
  return 0;
}
