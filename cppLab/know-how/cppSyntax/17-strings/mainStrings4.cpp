#include<iostream>
#include<cstring>

using namespace std;

int main(){
    char str1[11] = "Hello";
    char str2[10] = "World";
    char str3[10];
    char str4[10] = "World";
    char str5[10] = "Worlds";
    char str6[12] = "Hello World";

    int len;

    strcat(str1, " ");
    strcat(str1, str2);
    cout << "strcat result : " << str1 << endl;

    cout << endl; 

    len = strlen(str2);
    cout << "Length of str2 : " << len << endl;
    // char size is 10 but strlen will return 5
    // because the the real value of str2 : 'World/0'
    // null character is end of the string for strlen.
    // and null character is always placed after the last character !!!!

    cout << endl;

    int compare1 = strcmp(str2,str4);
    cout << "strcmp result for same strings : " << compare1 << endl;
    int compare2 = strcmp(str2, str5);
    cout << "strcmp result for different strings : " << compare2 << endl;

    cout << endl;

    char ch = 'e';
    // or
    //int ch = 'e';
    /*
        char is 1 byte and int is 4 byte
        it is possible to store 1 byte value in 4 byte storage
        ( store char in int)
        in computer universe they are same thing, 
        they are only bits stored in some adresses

        but if we try store a char like 'e' in int
        the value of the int will be the ASCII code of 'e'
    */
   
    char* p = strchr(str6, ch);
    cout << "String starting from " << ch << " is " << p << endl;
    return 0;
}