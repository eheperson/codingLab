#include<iostream>
#include<string>
#include<fstream>


int main(){


    std::ifstream f;

    f.open("./source_files/Small_area.xcf");

    if (f.is_open()) {
        std::cout<<"succeeed"<<std::endl;
        std::string tp;
        while(getline(f, tp)){ 
            std::cout << tp << "\n"; //print the data of the string
        }
        f.close(); //close the file object.
    }

    return 0;

}