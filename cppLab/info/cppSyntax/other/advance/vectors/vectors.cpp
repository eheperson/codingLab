#include <iostream>

#include <Vector>

int main(int argc, const char * argv[])
{
    std::vector<int> myVector;
    
    myVector.push_back(45);
    myVector.push_back(23);
    myVector.push_back(1);
    myVector.push_back(989);
    
    std::cout << myVector[3] << std::endl;
    
    return 0;
}