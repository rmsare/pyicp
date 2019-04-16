cmake_minimum_required(VERSION 2.6)
project(pyicp)

find_package(PythonInterp)
find_package(PythonLibs)

find_path(BOOST_DIR "boost")

set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/cmake )

include(UseCython)
include(FindNumPy)

link_directories(../libicp/lib/)
include_directories(../libicp/api/)
include_directories("${BOOST_DIR}")
include_directories("${PYTHON_NUMPY_INCLUDE_DIR}")
include_directories("./")

set_source_files_properties(pyicp.pyx PROPERTIES CYTHON_IS_CXX 1)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "../")
cython_add_module(pyicp pyicp.pyx pyicpp.cpp)
target_link_libraries(pyicp icp)

