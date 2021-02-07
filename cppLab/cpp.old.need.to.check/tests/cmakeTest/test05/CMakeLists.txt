cmake_minimum_required(VERSION 3.16.3)

# To versioning ur project
project(EHE VERSION 1.0)

add_executable(${PROJECT_NAME} main.cpp)

configure_file(EHEConfig.h.in EHEConfig.h)

# we add subdirectory called Adder
# which is a folder with anoher cmakelist.txt   
add_subdirectory(Adder)

target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_BINARY_DIR})

##############################################################################################
# To clone directory from github woth CMakeLists.txt
# Do it before  adding subdirectory of cloned library
#       add_subdirectory(external/glfw-master)
##############################################################################################
#           DOWNLOAD ALL THE SUBMODULES
find_package(Git QUIET)
if(GIT_FOUND AND EXISTS "${PROJECT_SOURCE_DIR}/.git")
# Update submodules as needed
    option(GIT_SUBMODULE "Check submodules during build" ON)
    if(GIT_SUBMODULE)
        message(STATUS "Submodule update")
        execute_process(COMMAND ${GIT_EXECUTABLE} submodule update --init --recursive
                        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
                        RESULT_VARIABLE GIT_SUBMOD_RESULT)
        if(NOT GIT_SUBMOD_RESULT EQUAL "0")
            message(FATAL_ERROR "git submodule update --init failed with ${GIT_SUBMOD_RESULT}, please checkout submodules")
        endif()
    endif()
endif()


#           CHECK ALL THE SUBMODULES
if(NOT EXISTS "${PROJECT_SOURCE_DIR}/external/glfw/CMakeLists.txt")
    message(FATAL_ERROR "The glfw submodules was not downloaded! GIT_SUBMODULE was turned off or failed. Please update submodules and try again.")
endif()
##############################################################################################
add_subdirectory(external/glfw-master)

#where the includes are
# it ollows us to #include<adder.h> than #include "adder.h"
target_include_directories(${PROJECT_NAME} 
    PUBLIC Adder 
    PUBLIC external/glfw-master/include)
# or
# target_include_directories(${PROJECT_NAME} PUBLIC Adder)
# target_include_directories(${PROJECT_NAME} PUBLIC external/glfw-master/include)

#where to find Adder(linker)
#where is our library gonna be
# Adder is path our build > out/build/Adder
target_link_directories(${PROJECT_NAME} 
    PRIVATE Adder
    PRIVATE external/glfw-master/src)

 
# linking library to executable
#it just links that library to our project
target_link_libraries(${PROJECT_NAME} adder glfw)
# if we have multiple libraries ..
# target_link_libraries(${PROJECT_NAME} adder lib2 lib3 lib4 ...)