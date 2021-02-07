#ifndef SCREEN_H
#define SCREEN_H

#include "SDL.h"

namespace particleScreen{

    class Screen{
        
        public : 
            const static int SCREEN_WIDTH = 800;
            const static int SCREEN_HEIGHT = 600;

        private : 
            SDL_Window* window;
            SDL_Renderer* renderer;
            SDL_Texture* texture;

            Uint32 *buffer = NULL;

        public :

            //Constructor
            Screen();

            bool init();
            bool processEvents();
            void close();
            void update();
            void setPixel(int x, int y,  Uint8 red, Uint8 green, Uint8 blue);

        protected : 

    }; 



}

#endif