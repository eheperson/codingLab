STL.H only supports .bmp images.
to work with other type image files
we need sdl2_image.H

sudo apt-get install libsdl2-image-dev


to compile main cpp : 
g++ -o  sdlImages  main.cpp `pkg-config --libs --cflags sdl2` -l SDL2_image



