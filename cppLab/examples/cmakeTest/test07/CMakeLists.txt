cmake_minimum_required(VERSION 3.16.3)

# To versioning ur project
project(EHE VERSION 1.0)

# adding optional libraries
# adder use logic
option(USE_ADDER "A simple library for adding 2 floats." ON)

if(USE_ADDER)
    # we add subdirectory called Adder
    # which is a folder with anoher cmakelist.txt 
    add_subdirectory(Adder)

    #list of link different libraries
    list(APPEND EXTRA_LIB_DIRS "Adder")
    list(APPEND EXTRA_INCLUDE_DIRS "${PROJECT_SOURCE_DIR}/Adder")
    # or : list(APPEND EXTRA_INCLUDES "Adder")

    list(APPEND EXTRA_LINKS adder)

endif()

configure_file(EHEConfig.h.in EHEConfig.h)

add_executable(${PROJECT_NAME} main.cpp)

target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_BINARY_DIR})


add_subdirectory(external/glfw-master)

#where the includes are
# it ollows us to #include<adder.h> than #include "adder.h"
target_include_directories(${PROJECT_NAME} 
    PUBLIC external/glfw-master/include
    ${EXTRA_INCLUDE_DIRS})

#where to find Adder(linker)
#where is our library gonna be
# Adder is path our build > out/build/Adders
target_link_directories(${PROJECT_NAME} 
    PUBLIC external/glfw-master/src
    ${EXTRA_LIB_DIRS})

 
# linking library to executable
#it just links that library to our project
target_link_libraries(${PROJECT_NAME} ${EXTRA_LINKS} glfw)
# if we have multiple libraries ..
# target_link_libraries(${PROJECT_NAME} adder lib2 lib3 lib4 ...)

install(TARGETS ${PROJECT_NANE} DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/EHEConfig.h" DESTINATION include)


include(InstallRequiredSystemLibraries)
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set(CPACK_PACKAGE_VERSION_MAJOR "${Test_VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${Test_VERSION_MINOR}")
include(CPack)