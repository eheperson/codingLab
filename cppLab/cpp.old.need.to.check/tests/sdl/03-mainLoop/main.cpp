#include <iostream>

#include "SDL.h"


using namespace std;


int main(int argc, char* argv[]){

    SDL_Init(SDL_INIT_EVERYTHING);

    SDL_Window* window;
    SDL_Event   event;
    bool run = true;

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

    while(run){
        while(SDL_PollEvent(&event)){
            if(event.type == SDL_QUIT){
                run = false;
                break;
            }
        }
    }

    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}