#include <iostream>
#include "SDL.h"
#include<vector>  

#define window_width 400
#define window_height 200
#define fps 60



using namespace std;

void capFramerate(Uint32 starting_tick);

class Sprite{
    private:
        SDL_Surface *image;
        // Every Surface has Rectangle
        SDL_Rect rect;

        int origin_x, origin_y;

    public:

        Sprite(Uint32 color, int x, int y, int w = 48, int h = 64){
            image = SDL_CreateRGBSurface(0, w, h, 32, 0, 0, 0, 0);

            SDL_FillRect(image, NULL, color);

            rect = image -> clip_rect;

            origin_x = rect.w/2;
            origin_y = rect.h/2;

            rect.x = x - origin_x;
            rect.y = y - origin_y;
        }

        void update(){
            //Can be overriden!!
        };

        void draw(SDL_Surface *destination){
            SDL_BlitSurface(image, NULL, destination, &rect);
        };

        SDL_Surface* getImage( ) const{
            return image;
        ;} 

        bool operator==(const Sprite &other ) const {
            return ( image == other.getImage() );
        };
};

class SpriteGroup{
    private:
        vector <Sprite*> sprites;
        int spritesSize;
    public:  

        SpriteGroup copy( ){
            SpriteGroup newGroup;

            for(int i = 0; i < spritesSize; i++){
                newGroup.add(sprites[i]);
            }
        }

        void add( Sprite* sprite ){
            sprites.push_back(sprite);
            spritesSize = sprites.size();  
        }

        void remove(Sprite spriteObject){
            for(int i = 0; i<spritesSize; i++){
                if( *sprites[i] == spriteObject){
                    sprites.erase(sprites.begin() + i);
                };
            }

            spritesSize = sprites.size();
        }

        bool has(Sprite spriteObject){
            for(int i = 0; i<spritesSize; i++){
                if(*sprites[i] == spriteObject){
                    return true;
                }
            }

            return false;
        }

        void update( ){
            if( !sprites.empty()){
                for(int i = 0; i < spritesSize; i++){
                    sprites[i] -> update();
                }
            }
        }

        void draw( SDL_Surface* destination){
            if( !sprites.empty()){
                for(int i = 0; i < spritesSize; i++){
                    sprites[i] -> draw(destination);
                }
            }
        }

        void empty(){
            sprites.clear();
            spritesSize = sprites.size();
        }

        int size(){
            return sprites.size();
        }
        vector <Sprite*> get_sprites(){
            return sprites;
        }
};

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

    //                                      red   green  blue
    Uint32 white = SDL_MapRGB(screen->format,255, 255, 255);
    Uint32 red = SDL_MapRGB(screen->format,  255, 0, 0);
    Uint32 blue = SDL_MapRGB(screen->format,  0, 0, 255);
    SDL_FillRect(screen, NULL, white);
    

    Sprite object(red, window_width/2, window_height/2);
    Sprite object2(blue, window_width/2 - 100, window_height/2 + 20);

    SpriteGroup activeSprites;
    
    activeSprites.add(&object);
    activeSprites.add(&object2);

    activeSprites.draw(screen);

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
