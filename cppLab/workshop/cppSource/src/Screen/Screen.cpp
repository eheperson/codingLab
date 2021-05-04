#include "Screen.h"
#include<iostream>

using namespace std;

namespace particleScreen{

    // Constructor initialization list
    Screen :: Screen() : window(NULL), renderer(NULL), texture(NULL), buffer(NULL){};
/*----------------------------------------------------------------------------------*/  
/*----------------------------------------------------------------------------------*/  
    bool Screen :: init(){
            if(SDL_Init(SDL_INIT_VIDEO) < 0){
                cout << "SDL Init Failed !" << endl;
                return false;
            }
            else{
                cout << "SDL Init Succeed !" << endl;
            }
            /**/
            window = SDL_CreateWindow("Particle Fire Simulation",
                                                SDL_WINDOWPOS_UNDEFINED,
                                                SDL_WINDOWPOS_UNDEFINED,
                                                SCREEN_WIDTH,
                                                SCREEN_HEIGHT,
                                                SDL_WINDOW_SHOWN);
            if(window == NULL){
                SDL_Quit();
                return false;
            }
            /**/
            renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_PRESENTVSYNC);
                                        //(window to render, _, ensures our rendering syncronized without refresh)
            if (renderer == NULL){
                cout << "Could not create renderer !!" << endl;

                SDL_DestroyWindow(window);
                SDL_Quit();

                return false;
            }
            /**/
            texture = SDL_CreateTexture(renderer,
                                        SDL_PIXELFORMAT_RGBA8888,
                                        SDL_TEXTUREACCESS_STATIC,
                                        SCREEN_WIDTH,
                                        SCREEN_HEIGHT);
            if (texture == NULL){
                cout << "Could not create texture !!" << endl;

                SDL_DestroyRenderer(renderer);
                SDL_DestroyWindow(window);
                SDL_Quit();

                return false;
            }
            /**/
            buffer = new Uint32[SCREEN_WIDTH * SCREEN_HEIGHT];
            memset(buffer, 0, SCREEN_WIDTH*SCREEN_HEIGHT*sizeof(Uint32));
/*            
            // to access one pixel on window 
            buffer[30000] = 0xFFFFFFFF;

            
                // we could do something  like memset
                
                for(int i = 0; i < SCREEN_WIDTH*SCREEN_HEIGHT; i++){
                    buffer[i] = 0xFFFFFFFF;
                }
*/

            return true;
    };
/*----------------------------------------------------------------------------------*/  
/*----------------------------------------------------------------------------------*/    
    bool Screen :: processEvents(){
        SDL_Event event;
        /**/
        while(SDL_PollEvent( &event )){
            if(event.type == SDL_QUIT)
                return false;
            
        };       
        return true;
    };
/*----------------------------------------------------------------------------------*/  
/*----------------------------------------------------------------------------------*/  
    void Screen :: close(){
        delete [] buffer;
        /**/
        SDL_DestroyRenderer(renderer);
        SDL_DestroyTexture(texture);
        SDL_DestroyWindow(window);
        SDL_Quit();
    };
/*----------------------------------------------------------------------------------*/  
/*----------------------------------------------------------------------------------*/  
    void Screen :: update(){
        SDL_UpdateTexture(texture, NULL, buffer, SCREEN_WIDTH*sizeof(Uint32));
        SDL_RenderClear(renderer);
        SDL_RenderCopy(renderer, texture, NULL, NULL);
        SDL_RenderPresent(renderer);
    }
/*----------------------------------------------------------------------------------*/  
/*----------------------------------------------------------------------------------*/  
    void Screen :: setPixel(int x, int y,  Uint8 red, Uint8 green, Uint8 blue){
        /**/
        Uint32 color = 0; 
        /**/
        color += red;   //add red channel
        color <<= 8;    //bitshifting - 8bit
        color += green; //add green clannel
        color <<= 8;    //bitshifting - 8bit
        color += blue;  //add blue channel
        color <<= 8;    //bitshifting - 8bit
        color += 0xFF;  //add alpha channel
        /**/
        buffer[(y * SCREEN_WIDTH) + x] = color;
    };

}