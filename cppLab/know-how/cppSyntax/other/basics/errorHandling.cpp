#include <iostream>

int main(int argc, const char * argv[])
{
    int i = 11;
    
    try
    {
        if (i < 10)
        {
            std::cout << i << std::endl;
        }
        else
        {
            throw 1;
        }
    }
    catch(int error)
    {
        std::cout << error << std::endl;
    }
    
    return 0;
}