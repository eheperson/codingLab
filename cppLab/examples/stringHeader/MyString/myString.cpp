// source code, implementations, definitions
#include<iostream>
#include "myString.hpp"

using namespace std;

int __myStrFunc myStrLen(const char* str){
    //null character '\0' : end of the char array
    int i = 0;
    while(*str != '\0'){
        str++;
        i++;
    }

    /* or 
    while(*str++ != '\0'){
        i++;
    }   
    */

    /* or 
    int i = 0;
    for( ; str[i] != '\0'; i++);
    */

    /* or 
    int i = 0;
    for( ; *(str + i) != '\0'; i++);
    */

    return i;
};

bool __myStrFunc myStrCmp(const char* str1, const char* str2){
    while(*str1 == *str2){
        if(*str1 == '\0' || *str2 == '\0')
            break;
        str1++;
        str2++;
    }

    /*or
    while(*str1++ == *str2++){
        if(*str1 == '\0' || *str2 == '\0')
            break;
    }
    */

    if(*str1 == '\0' && *str2 == '\0')
        return 0;
    else
        return false;
};

char* __myStrFunc myStrCat(char *dest, const char* source){
    int i;
    int j;

    for( i = 0; dest[i] != '\0'; i++);

    for( j = 0; source[j] != '\0'; j++){
        dest[i + j] = source[j];
    }

    dest[i + j] = '\0';

    return dest;
}; 

char* __myStrFunc myStrCat2(char *dest, const char* source){
    int i = myStrLen(dest);
    int j;

    for( i = 0; dest[i] != '\0'; i++);

    for( j = 0; source[j] != '\0'; j++){
        dest[i + j] = source[j];
    }

    dest[i + j] = '\0';

    return dest;
}; 


char* __myStrFunc myStrChr(char* str, char ch){
    while(*str != '\0'){
        if(*str == ch)
            return str;
        
        str++;
    }
    if(*str == ch)
        return str;

    return NULL;
    // return '\0';
}

char* __myStrFunc myStrChr2(char* str, char ch){
    static char* str_start = str;

    while(*str != '\0'){
        if(*str == ch)
            return str;
        
        str++;
    }
    if(*str == ch)
        return str_start;

    return NULL;
    // return '\0';
}

char* __myStrFunc  myStrCpy(char* dest, const char* source, int size){
    cout << "myStrCpy() is calling .... " << endl;
    int i;
    int destLen = size;
    int sourceLen = myStrLen(source);
    if(destLen >= sourceLen){
        for(i=0; source[i] != '\0'; i++){
            dest[i] = source[i];
        }
        dest[i] = '\0';    
    }
    else{
        cout << "Size of Dest is smaller than size of Source ..." << endl;
        for(i=0; i < destLen; i++){
            dest[i] = source[i];
        }
        dest[i] = '\0'; 
    }
    

    cout << "myStrCpy() is complete .... " << endl;

    return dest;
};