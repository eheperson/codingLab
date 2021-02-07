/////////////////////////////////////////////////
//////////////// String example
/////////////////////////////////////////////////

/*
    cstring : string library for C++
        strcpy -> Copy str1 to str2
        strcat -> Concatenates str2 onto str1
        strlen -> Length of str
        strcmp -> Compare both str1 and str2
        strchr -> Searchin specific characters in string
*/

#include<iostream>
#include<cstring>



using namespace std;


int main(){

    char str1[10] = "Ali";
    char str2[10] = "Veli";
    char str3[10];

    /*
    char str5[10] = "123456789101112"; ///error
    chars are constants : const char *
    if we try exceed the reserved char size,
    compiler will get error
    we cannot change the adresses whic are not reserved
    */


    // copy str1 to str3
    strcpy(str3, str1);
    cout << "strcpy for str3 to str1 : " << str3 << endl;
    //or
    //cout << "strcpy for str3 to str1 : " << strcpy(str3, str1) << endl;

    for( int i =0; i<10; i++){
        cout << "str3[" << i << "] :" << str3[i] << endl;
    };

    cout << endl;

    for( int i =0; i<15; i++){
        cout << "str1[" << i << "] :" << str3[i] << endl;
        // or 
        // cout << "str1[" << i << "] :" << *(str3 + i) << endl;
    };
    /// char arrays are adresses also !!!!!!!!!!

    cout << endl;

    for( int i =0; i<15; i++){
        if(i>9){
            str1[i] = 'a';
        }
        cout << "str1[" << i << "] :" << str1[i] << endl;
    };

    

    return 0;
}


/////////////////////////////////////////////////
//////////////// String example
/////////////////////////////////////////////////