# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/mpuig/ur5arm_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/mpuig/ur5arm_ws/build

# Utility rule file for omni_msgs_generate_messages_cpp.

# Include the progress variables for this target.
include phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp.dir/progress.make

phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp: /home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniButtonEvent.h
phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp: /home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniState.h
phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp: /home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniFeedback.h


/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniButtonEvent.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniButtonEvent.h: /home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs/msg/OmniButtonEvent.msg
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniButtonEvent.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/mpuig/ur5arm_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating C++ code from omni_msgs/OmniButtonEvent.msg"
	cd /home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs && /home/mpuig/ur5arm_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs/msg/OmniButtonEvent.msg -Iomni_msgs:/home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs/msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/cmake/../msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -p omni_msgs -o /home/mpuig/ur5arm_ws/devel/include/omni_msgs -e /opt/ros/melodic/share/gencpp/cmake/..

/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniState.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniState.h: /home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs/msg/OmniState.msg
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniState.h: /opt/ros/melodic/share/geometry_msgs/msg/Vector3.msg
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniState.h: /opt/ros/melodic/share/geometry_msgs/msg/Pose.msg
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniState.h: /opt/ros/melodic/share/geometry_msgs/msg/Point.msg
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniState.h: /opt/ros/melodic/share/geometry_msgs/msg/Quaternion.msg
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniState.h: /opt/ros/melodic/share/std_msgs/msg/Header.msg
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniState.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/mpuig/ur5arm_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating C++ code from omni_msgs/OmniState.msg"
	cd /home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs && /home/mpuig/ur5arm_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs/msg/OmniState.msg -Iomni_msgs:/home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs/msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/cmake/../msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -p omni_msgs -o /home/mpuig/ur5arm_ws/devel/include/omni_msgs -e /opt/ros/melodic/share/gencpp/cmake/..

/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniFeedback.h: /opt/ros/melodic/lib/gencpp/gen_cpp.py
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniFeedback.h: /home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs/msg/OmniFeedback.msg
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniFeedback.h: /opt/ros/melodic/share/geometry_msgs/msg/Vector3.msg
/home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniFeedback.h: /opt/ros/melodic/share/gencpp/msg.h.template
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/mpuig/ur5arm_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Generating C++ code from omni_msgs/OmniFeedback.msg"
	cd /home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs && /home/mpuig/ur5arm_ws/build/catkin_generated/env_cached.sh /usr/bin/python2 /opt/ros/melodic/share/gencpp/cmake/../../../lib/gencpp/gen_cpp.py /home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs/msg/OmniFeedback.msg -Iomni_msgs:/home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs/msg -Igeometry_msgs:/opt/ros/melodic/share/geometry_msgs/cmake/../msg -Isensor_msgs:/opt/ros/melodic/share/sensor_msgs/cmake/../msg -Istd_msgs:/opt/ros/melodic/share/std_msgs/cmake/../msg -p omni_msgs -o /home/mpuig/ur5arm_ws/devel/include/omni_msgs -e /opt/ros/melodic/share/gencpp/cmake/..

omni_msgs_generate_messages_cpp: phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp
omni_msgs_generate_messages_cpp: /home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniButtonEvent.h
omni_msgs_generate_messages_cpp: /home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniState.h
omni_msgs_generate_messages_cpp: /home/mpuig/ur5arm_ws/devel/include/omni_msgs/OmniFeedback.h
omni_msgs_generate_messages_cpp: phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp.dir/build.make

.PHONY : omni_msgs_generate_messages_cpp

# Rule to build all files generated by this target.
phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp.dir/build: omni_msgs_generate_messages_cpp

.PHONY : phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp.dir/build

phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp.dir/clean:
	cd /home/mpuig/ur5arm_ws/build/phantom_omni/omni_msgs && $(CMAKE_COMMAND) -P CMakeFiles/omni_msgs_generate_messages_cpp.dir/cmake_clean.cmake
.PHONY : phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp.dir/clean

phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp.dir/depend:
	cd /home/mpuig/ur5arm_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/mpuig/ur5arm_ws/src /home/mpuig/ur5arm_ws/src/phantom_omni/omni_msgs /home/mpuig/ur5arm_ws/build /home/mpuig/ur5arm_ws/build/phantom_omni/omni_msgs /home/mpuig/ur5arm_ws/build/phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : phantom_omni/omni_msgs/CMakeFiles/omni_msgs_generate_messages_cpp.dir/depend
