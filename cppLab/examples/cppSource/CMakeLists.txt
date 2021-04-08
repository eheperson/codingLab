#
#
# Add these lines at the top (must be added before you use project() or enable_language() command)
set(CMAKE_CXX_COMPILER "D:/apps/msys64/mingw64/bin/g++.exe")
set(CMAKE_MAKE_PROGRAM "D:/apps/msys64/mingw64/bin/mingw32-make.exe")
#
#
cmake_minimum_required(VERSION 3.20)
project(cppsource)

#
#
add_executable(cppsource "src/main.cpp")