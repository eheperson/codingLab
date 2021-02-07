/////////////////////////////////////////////////
////////// header - source file example ////////
/////////////////////////////////////////////////
#include<iostream>
#include<myString.hpp>
#include<cstring>

using namespace std;

#define SIZE 10

//execute
int main(){

    char str1[10] = "Hello";
    char str2[10] = "World";
    char str3[11];
    char str4[11];
    char str5[11];

    int len;
    int myLen;
    len = strlen(str1);
    myLen = myStrLen(str1);
    cout << "Lengt of the str1 with 'strlen()'  : " << len << endl;
    cout << "Lengt of the str1 with 'myStrLen()'  : " << myLen << endl;

    cout << endl;

    int cmpValue = strcmp(str1, str2);
    bool myCmpValue = myStrCmp(str1, str2);
    cout << "Comparision of str1 and str2 with 'strcmp()'  : " << cmpValue << endl;
    cout << "Comparision of str1 and str2 with 'myStrCmp()'  : " << myCmpValue << endl;

    cout << endl;

    strcat(str3, str1);
    strcat(str3, " ");
    strcat(str3, str2);
    cout << "Concatenation of str1 and str2 with 'strcat()'  : " << strcat(str1, str2) << endl;
    cout << "Concatenation of str1 and str2 with 'myStrCat()'  : " << myStrCat(str1, str2) << endl;
    cout << "Concatenation of str1 and str2 with 'myStrCat2()'  : " << myStrCat2(str1, str2) << endl;

    cout << endl;

    char ch ='e';
    // try for > ch ='\0'
    char* p1;
    char* p2;
    char* p3;
    p1 = strchr(str3, ch);
    p2 = myStrChr(str3, ch);
    p3 = myStrChr2(str3, ch);
    cout << "String(str3) starting from '" << ch <<"' by 'strchr()' : " << strchr(str3, ch) << endl;
    cout << "String(str3) starting from '" << ch <<"' by 'myStrChr()' : " << myStrChr(str3, ch) << endl;
    cout << "String(str3) starting from '" << ch <<"' by 'myStrChr2()' : " << myStrChr2(str3, ch) << endl;

    cout << endl;

    char* p4;
    char* p5;
    p4 = strcpy(str4, str3);
    p5 = myStrCpy(str5, str3, 11);
    cout << "Copying str3 to str4 with 'strcpy()'  : " << str4 << endl;
    cout << "Copying str3 to str4 with 'myStrCpy()'  : " << p5 << endl;


    system("Pause");

    return 0;
}




/////////////////////////////////////////////////
////////// header - source file example ////////
/////////////////////////////////////////////////