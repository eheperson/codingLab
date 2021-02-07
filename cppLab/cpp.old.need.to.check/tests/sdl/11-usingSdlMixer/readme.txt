to work with audio files in SDL
we have to install sdl_mixer

sudo apt-get install libsdl2-mixer-dev

to compile main cpp : 
g++ -o  sdlImages  main.cpp `pkg-config --libs --cflags sdl2` -lSDL2_image -lSDL2_mixer

---------------------------------------------------------------------------------
for the > > > > > >  > 21_sound_effects_and_music.cpp
---------------------------------------------------------------------------------

Copyright Notice:
-----------------
The files within this zip file are copyrighted by Lazy Foo' Productions (2004-2020)
and may not be redistributed without written permission.

This project is linked against:
----------------------------------------
Windows:
SDL2
SDL2main
SDL2_image
SDL2_ttf
SDL2_mixer

*nix:
SDL2
SDL2_image
SDL2_ttf
SDL2_mixer
