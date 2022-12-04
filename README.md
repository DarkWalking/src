Step 1: Prerequisites
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3-rosdep python3-rosinstall-generator python3-vcstool build-essential
$ sudo rosdep init
$ rosdep update
Step 2: Installation
2.1 Create a catkin Workspace
:star: This workspace is for install and update ROS only!DO NOT PUT YOU CODE IN IT!! Make another workspace!!!

$ mkdir ~/ros_catkin_ws
$ cd ~/ros_catkin_ws

Name the workspace “ros_catkin_workspace” so that people know it is for ROS install and update.
$ rosinstall_generator desktop --rosdistro noetic --deps --tar > noetic-desktop.rosinstall
$ mkdir ./src
$ vcs import --input noetic-desktop.rosinstall ./src

2.2 Resolving Dependencies
$ rosdep install --from-paths ./src --ignore-packages-from-source --rosdistro noetic -y

2.3 Building the catkin Workspace
$ sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3 --install-space /opt/ros/noetic
$ source /opt/ros/noetic/setup.bash
$ echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
Downloading ROS complete!!
3. Maintaining a Source Checkout
This steps is to update ROS, NOT TO INSTALL. If you’re trying to install ROS, you don’t have to do these steps.
Step 1: Update your rosinstall file
$ mv -i noetic-desktop.rosinstall noetic-desktop.rosinstall.old
Generate New Rosinstall File:
$ rosinstall_generator desktop --rosdistro noetic --deps --tar > noetic-desktop.rosinstall
Compare
$ diff -u noetic-desktop.rosinstall noetic-desktop.rosinstall.old
Step 2: Download the latest sources
If you’re satisfied with these changes, incorporate the new rosinstall file into the workspace and update your workspace:

$ vcs import --input noetic-desktop.rosinstall ./src

Step 3: Rebuild your workspace
$ sudo ./src/catkin/bin/catkin_make_isolated --install -DPYTHON_EXECUTABLE=/usr/bin/python3 --install-space /opt/ros/noetic

$ source /opt/ros/noetic/setup.bash
