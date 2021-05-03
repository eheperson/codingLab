#
#
set(CMAKE_C_COMPILER "D:/apps/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/gcc.exe")
set(CMAKE_CXX_COMPILER "D:/apps/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/g++.exe")
#set(CMAKE_MAKE_PROGRAM "D:/apps/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/mingw32-make.exe")

set(CMAKE_BUILD_TYPE Release)
#
cmake_minimum_required(VERSION 3.20.2)
project(ehe) #project name : ehe, ${PROJECT_NAME}->ehe
#
add_executable(${PROJECT_NAME} src/main.cpp)
