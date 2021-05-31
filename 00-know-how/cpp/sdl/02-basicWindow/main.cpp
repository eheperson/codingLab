#include <iostream>

#include "SDL.h"


using namespace std;

/*
SDL_Window* SDL_CreateWindow(const char* title,
                             int         x,
                             int         y,d
                             int         w,
                             int         h,
                             Uint32      flags)

*/


int main(int argc, char* argv[]){

    SDL_Init(SDL_INIT_EVERYTHING);

    SDL_Window* window;

    window = SDL_CreateWindow( "Test Window",
                                SDL_WINDOWPOS_UNDEFINED,
                                SDL_WINDOWPOS_UNDEFINED,
                                400,
                                200,
                                SDL_WINDOW_RESIZABLE);
    if(window == NULL){
        cout<< "There was an error initializinf the window !"<<endl
            << SDL_GetError() << endl;
    }

    SDL_Delay(5000);

    SDL_DestroyWindow(window);

    SDL_Quit();
    return 0;
}