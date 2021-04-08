cmake_minimum_required(VERSION 3.19.1)

set(CMAKE_C_COMPILER "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/x86_64-w64-mingw32-gcc.exe")
set(CMAKE_CXX_COMPILER "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/x86_64-w64-mingw32-g++.exe")
set(CMAKE_MAKE_PROGRAM "C:/Program Files/mingw-w64/x86_64-8.1.0-posix-seh-rt_v6-rev0/mingw64/bin/mingw32-make.exe")


project(systemDynamicSLib)

add_executable(${PROJECT_NAME} main.cpp)

add_subdirectory(sysdyn)
target_link_directories(${PROJECT_NAME} PRIVATE SystemDynamics)
target_include_directories(${PROJECT_NAME} PUBLIC SystemDynamics)
target_link_libraries(${PROJECT_NAME} sysdyn)
