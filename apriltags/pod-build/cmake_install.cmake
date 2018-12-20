# Install script for directory: /home/tanay/Desktop/apriltags

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/tanay/Desktop/apriltags/build")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/tanay/Desktop/apriltags/pod-build/lib/libapriltags.a")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/AprilTags" TYPE FILE FILES
    "/home/tanay/Desktop/apriltags/AprilTags/Tag16h5_other.h"
    "/home/tanay/Desktop/apriltags/AprilTags/FloatImage.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Tag36h11.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Tag25h9.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Edge.h"
    "/home/tanay/Desktop/apriltags/AprilTags/TagFamily.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Gaussian.h"
    "/home/tanay/Desktop/apriltags/AprilTags/UnionFindSimple.h"
    "/home/tanay/Desktop/apriltags/AprilTags/MathUtil.h"
    "/home/tanay/Desktop/apriltags/AprilTags/TagDetector.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Tag16h5.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Segment.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Quad.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Homography33.h"
    "/home/tanay/Desktop/apriltags/AprilTags/GLine2D.h"
    "/home/tanay/Desktop/apriltags/AprilTags/XYWeight.h"
    "/home/tanay/Desktop/apriltags/AprilTags/pch.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Gridder.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Tag36h11_other.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Tag25h7.h"
    "/home/tanay/Desktop/apriltags/AprilTags/Tag36h9.h"
    "/home/tanay/Desktop/apriltags/AprilTags/GrayModel.h"
    "/home/tanay/Desktop/apriltags/AprilTags/GLineSegment2D.h"
    "/home/tanay/Desktop/apriltags/AprilTags/TagDetection.h"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/tanay/Desktop/apriltags/pod-build/lib/pkgconfig/apriltags.pc")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/tanay/Desktop/apriltags/pod-build/example/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/tanay/Desktop/apriltags/pod-build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
