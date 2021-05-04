INSTALLING OUR SOFTWARE
############################################

if we want run our program from any directory in terminal :

2 line of code in the Adder/CMakeLists.txt
to install files in destination folder
    install(TARGETS adder DESTINATION lib)
    install(FILES adder.h DESTINATION include)

2 lines of code in ./CMakeLists.txt
    install(TARGETS ${PROJECT_NANE} DESTINATION bin)
    install(FILES "${PROJECT_BINARY_DIR}/EHEConfig.h" DESTINATION include)

############################################
Some License things

include(InstallRequiredSystemLibraries)
set(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set(CPACK_PACKAGE_VERSION_MAJOR "${Test_VERSION_MAJOR}")
set(CPACK_PACKAGE_VERSION_MINOR "${Test_VERSION_MINOR}")
include(CPack)

############################################

To pack our project 

cd out/build
sudo cpack

############################################

configure and build with cmake using commandline

./configure
./build
./run










