making libraries optional : 

    if we make the setting is OFF, Adder librarry does not inscluded
    
    option(USE_ADDER "A simple library for adding 2 floats." ON)
    if(USE_ADDER)
        add_subdirectory(Adder)
    endif()

configure and build with cmake using commandline

./configure
./build
./run