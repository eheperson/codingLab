#include <iostream>
#include "ExtraClass.h"


int main(int argc, const char * argv[])
{
    ExtraClass ec;
    
    ec.PrintFunction();
    ec.i = 90;
    
    std::cout << ec.i << std::endl;
    
    return 0;
}