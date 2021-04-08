cmake_minimum_required(VERSION 3.16.3)

project(ehe)

add_executable(${PROJECT_NAME} main.cpp)

# we add subdirectory called Adder
# which is a folder with anoher cmakelist.txt   
add_subdirectory(Adder)

#where the includes are
# it ollows us to #include<adder.h> than #include "adder.h"
target_include_directories(${PROJECT_NAME} PUBLIC Adder)


#where to find Adder(linker)
#where is our library gonna be
# Adder is path our build > out/build/Adder
target_link_directories(${PROJECT_NAME} PRIVATE Adder)

 
# linking library to executable
#it just links that library to our project
target_link_libraries(${PROJECT_NAME} adder)
# if we have multiple libraries ..
# target_link_libraries(${PROJECT_NAME} adder lib2 lib3 lib4 ...)