#include <iostream>
#include <List>

int main(int argc, const char * argv[])
{
    std::list<int> myList(5, 200);
    
    myList.push_front(47);
    
    myList.pop_back();
    
    for ( std::list<int>::iterator it = myList.begin(); it != myList.end(); it++ )
    {
        std::cout << *it << std::endl;
    }
    
    return 0;
}