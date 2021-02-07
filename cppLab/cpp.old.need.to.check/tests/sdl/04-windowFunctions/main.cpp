#include <iostream>

#include "SDL.h"


/*-----------------------------------------------
DO NOT RUN THAT CODE
IT MIGHT BE FREEZE YOUR GNOME-SESSION
SDL_SetWindowPosition(window, x, y);
----------------------------------------------*/

using namespace std;


int main(int argc, char* argv[]){

    SDL_Init(SDL_INIT_EVERYTHING);

    SDL_Window* window;
    SDL_Event   event;

    bool run = true;

    int x, y, w, h;

    

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


    SDL_SetWindowBordered(window, SDL_TRUE);
    SDL_SetWindowTitle(window, "Emotional Pimp");
    
    w = 1550;
    h = 264;
    SDL_SetWindowSize( window, w, h);

    while(run){
        while(SDL_PollEvent(&event)){
            if(event.type == SDL_QUIT){
                run = false;
                break;
            }
        }

        SDL_GetWindowPosition(window, &x, &y);
        cout << x << " - " << y << endl;
    }

    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}