#! /bin/sh 

#cmake -S . -B out/build

#to use cmake with options
# (check the /external/glfw-maser/CMakeLists.txt : options)
cmake -DGLFW_BUILD_DOCS=OFF -S . -B out/build