#include<iostream>
#include "SDL.h"
#include "Screen.h"

using namespace std;
using namespace particleScreen;

int main(int argc, char* argv[]){


    Screen screen;

    if( screen.init() == false){
        cout << " Error at initializing SDL !!" << endl;
    };

    
    while (true){
        // Update Particles

        //Draw Particles
        for( int j = 0; j < Screen :: SCREEN_HEIGHT; j++){
            for( int i = 0; i < Screen :: SCREEN_WIDTH; i++){
                screen.setPixel(i, j, 128, 0, 255);
            }
        }
        //screen.setPixel( 400, 300, 255, 255, 255);

        //Draw the Screen
        screen.update();

        //Check For Messages/Events

        if(screen.processEvents() == false){
            break;
        };

    };
    
    screen.close();
    cout<<"ehe"<<endl;

    return 0;

}