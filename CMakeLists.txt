cmake_minimum_required(VERSION 2.6)
project(pyicp)

set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/cmake )

find_package(PythonInterp)
find_package(PythonLibs)

include(UseCython)

add_subdirectory(./libicp/)
include_directories(./libicp/api ./python/)
add_dependencies(pyicp libicp)

set_source_files_properties(./python/pyicp.pyx PROPERTIES CYTHON_IS_CXX TRUE)

cython_add_module(pyicp ./python/pyicp.pyx)
