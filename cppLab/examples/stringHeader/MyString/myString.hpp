//declerations
#ifndef __ARRAY_HPP__
#define __ARRAY_HPP__

/*
        strcpy -> Copy str1 to str2
        strcat -> Concatenates str2 onto str1
        strlen -> Length of str
        strcmp -> Compare both str1 and str2
        strchr -> Searchin specific characters in string
*/

#define __myStrFunc
// __myStrFunc : it gives information to user about function

int __myStrFunc myStrLen(const char* str);

bool __myStrFunc myStrCmp(const char* str1, const char* str2);

char* __myStrFunc myStrCat(char *dest, const char* source); 

char* __myStrFunc myStrCat2(char *dest, const char* source); 

char* __myStrFunc myStrChr(char* str, char ch);

char* __myStrFunc myStrChr2(char* str, char ch);

char* __myStrFunc  myStrCpy(char* dest, const char* source, int size);

#endif