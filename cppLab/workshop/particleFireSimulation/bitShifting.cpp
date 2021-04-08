#include<iostream>
#include<iomanip>

using namespace std;


int main(int argc, char* argv []){

    // 0xFF123456
    unsigned char alpha = 0xFF;
    unsigned char red = 0x12;
    unsigned char green = 0x34;
    unsigned char blue = 0x56;

    unsigned int color = 0; 

    color += alpha;
    color <<= 8;
    color += red;
    color <<= 8;
    color += green;
    color <<= 8;
    color += blue;
    cout << "Color : ";
    cout << setfill('0') << setw(8) << hex << color << endl;
    return 0;
}