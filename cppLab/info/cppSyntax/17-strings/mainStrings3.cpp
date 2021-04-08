/////////////////////////////////////////////////
//////////////// String example
/////////////////////////////////////////////////

/*

 THERE ARE SOME ERRORS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11

*/

#include<iostream>
#include<cstring>



using namespace std;


int main(){

    char str1[10] = "Ali";
    char str2[10];
    char* str3;
    char* str4;

    str3 = str1;
    cout << "str3 : " << str3 << endl;

    

    for( int i =0; i<10; i++){
        str4[i] = str1[i];

        cout << "str4 : " << str4[i] << endl;
    };

    cout << "str4 adress : " << &str4[0] << endl;
    cout << "str1 adress : " << &str1[0] << endl;


    return 0;
}


/////////////////////////////////////////////////
//////////////// String example
/////////////////////////////////////////////////