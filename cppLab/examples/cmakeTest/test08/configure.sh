#! /bin/sh 

#cmake -S . -B out/build

#to use cmake with options
# (check the /external/glfw-maser/CMakeLists.txt : options)
# if we do not change  -DUSE_ADDER it remains default as in CMakeLists.txt
cmake -DGLFW_BUILD_DOCS=ON -DUSE_ADDER=ON -S . -B out/build