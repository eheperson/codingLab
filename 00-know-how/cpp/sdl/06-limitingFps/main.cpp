#include <iostream>

#include "SDL.h"

#define window_width 400
#define window_height 200
#define fps 60



using namespace std;

void capFramerate(Uint32 starting_tick);

int main(int argc, char* argv[]){

    SDL_Init(SDL_INIT_EVERYTHING);

    SDL_Window* window = NULL;
    SDL_Event   event;

     
    bool run = true;

    window = SDL_CreateWindow( "Test Window",
                                SDL_WINDOWPOS_UNDEFINED,
                                SDL_WINDOWPOS_UNDEFINED,
                                window_width,
                                window_height,
                                SDL_WINDOW_RESIZABLE);
    if(window == NULL){
        cout<< "There was an error initializinf the window !"<<endl
            << SDL_GetError() << endl;
    }

    SDL_Surface *screen = SDL_GetWindowSurface(window);

    Uint32 white = SDL_MapRGB(screen->format,255, 255, 255);
    //                                      red   green  blue
    SDL_FillRect(screen, NULL, white);
    SDL_UpdateWindowSurface(window);

    Uint32 starting_tick;
    while(run){

        starting_tick = SDL_GetTicks();

        while(SDL_PollEvent(&event)){
            if(event.type == SDL_QUIT){
                run = false;
                break;
            }
        }

    capFramerate(starting_tick);

    }

    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}

void capFramerate(Uint32 starting_tick){
    if( (1000/fps) > SDL_GetTicks() - starting_tick ){
            SDL_Delay((1000/fps) - (SDL_GetTicks() - starting_tick));
        }
}
        