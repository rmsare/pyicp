# project
cmake_minimum_required (VERSION 2.6)
project (icp) 
include(GNUInstallDirs)
# directories
set (ICP_SRC_DIR src)
set (ICP_INCLUDE_DIR include)
FIND_PATH(BOOST_DIR "boost")

# include directory
include_directories("${ICP_INCLUDE_DIR}")
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
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "lib")

# build shared library
add_library(icp STATIC 
	    src/icp.cpp
	    src/icpPointToPlane.cpp
	    src/icpPointToPoint.cpp
	    src/kdtree.cpp
	    src/matrix.cpp
)

set_target_properties(icp PROPERTIES 
				PUBLIC_HEADER api/libicp.h)
configure_file(icp.pc.in icp.pc @ONLY)
target_include_directories(icp PRIVATE .)
install(TARGETS icp
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
        ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}/static
	PUBLIC_HEADER DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${CMAKE_BINARY_DIR}/icp.pc
	DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/pkgconfig)

 
