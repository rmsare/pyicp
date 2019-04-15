# project
cmake_minimum_required (VERSION 2.6)
project (libicp VERSION 1.0.1) 
include(GNUInstallDirs)
# directories
set (LIBICP_SRC_DIR src)
set (LIBICP_INCLUDE_DIR include)
FIND_PATH(BOOST_DIR "boost")

# include directory
include_directories("${LIBICP_INCLUDE_DIR}")
include_directories("${BOOST_DIR}")

# determine if OpenMP can/should be used
option(USE_OPENMP "Enable OpenMP?" ON) # set to OFF to disable
if(USE_OPENMP)
 FIND_PACKAGE(OpenMP)
 if(OPENMP_FOUND OR OpenMP_FOUND)
  message(STATUS "OpenMP flags = ${OpenMP_CXX_FLAGS}")
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} ${OpenMP_C_FLAGS}")
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${OpenMP_CXX_FLAGS}")
 else(OPENMP_FOUND OR OpenMP_FOUND)
  message(STATUS "OpenMP not supported")
 endif(OPENMP_FOUND OR OpenMP_FOUND)
endif(USE_OPENMP)

# sources
FILE(GLOB LIBICP_SRC_FILES "src/*.cpp")

# make release version
set(CMAKE_BUILD_TYPE Release)

# build shared library
add_library(libicp SHARED
	    src/icp.cpp
	    src/icpPointToPlane.cpp
	    src/icpPointToPoint.cpp
	    src/kdtree.cpp
	    src/matrix.cpp
)

set_target_properties(libicp PROPERTIES 
				VERSION ${PROJECT_VERSION}
				SOVERSION 1
				PUBLIC_HEADER api/libicp.h)
configure_file(libicp.pc.in libicp.pc @ONLY)
target_include_directories(libicp PRIVATE .)
install(TARGETS libicp
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${CMAKE_BINARY_DIR}/mylib.pc
	DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/pkgconfig)

 
