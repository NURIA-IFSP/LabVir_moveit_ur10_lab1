cmake_minimum_required(VERSION 3.0.2)
project(ur_description)

find_package(catkin REQUIRED)

catkin_package()

if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(tests/roslaunch_test_ur10e.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur10.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur12e.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur16e.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur15.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur20.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur30.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur3e.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur3.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur5e.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur7e.xml)
  roslaunch_add_file_check(tests/roslaunch_test_ur5.xml)
endif()

install(DIRECTORY cfg config launch meshes urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
