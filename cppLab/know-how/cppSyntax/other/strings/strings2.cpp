#include<iostream>
#include<string>
#include<sstream> //lib for string stream


int main( int argc, const char * argv[]){

    std::string s("this is a string ");
    std::cout<<s.c_str()<<std::endl;

    // STRING STREAM
    std::string str("344");
    int i;
    std::stringstream(str) >> i;

    

    return 0;
}