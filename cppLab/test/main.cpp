#include <iostream>
#include "Trial.h"
#include "Person.h"
#include "Animal.h"
#include "Creature.h"
#include "ns1.h"
#include "ns2.h"
#include <sstream>

using namespace std;


using namespace namespace2;

//using namespace namespace1;


void changeSomethingRef(double &value){
    value = 123.4l;
}

void changeSomethingNorm(double value){
    value = 123.4l;
}

void showString(string t[], const int n){
    for(int i = 0; i<n; i++){
        cout<<t[i]<<endl;
    }
    cout<<sizeof(t)<<endl;
}

void showStringPtr(string *t, const int n){
    for(int i = 0; i<n; i++){
        cout<<t[i]<<endl;
    }
    cout<<sizeof(t)<<endl;
}

void showStringPtr2(string (&t)[3]){
    for(int i = 0; i<sizeof(t)/sizeof(string); i++){
        cout<<t[i]<<endl;
    }
    cout<<sizeof(t)<<endl;
}

string t2[] = {"apple", "orange", "banana"};
string * getArray(){
    // do not return pointers to local variabls! like below
    // string t2[] = {"apple", "orange", "banana"};

    //t2 is defined in global scope
    return t2;
}

char * getMemory(){
    char *ptr = new char[100];

    return ptr;
}

void freeMemory(char *pMem){
    delete [] pMem;
}


int main()
{
    cout<<endl<<"-------------------------------------------------------"<<endl;

    {
        cout<<endl<<"-------"<<"Trial Class Scope Start"<<"-------"<<endl<<endl;

        testClass ehe;
        ehe.speak();


        cout<<endl<<endl<<"-------"<<"Trial Class Scope End"<<"-------"<<endl;
    }

    cout<<endl<<"-------------------------------------------------------"<<endl;

    {
        cout<<endl<<"-------"<<"String Stream Scope Start"<<"-------"<<endl<<endl;

        string name = "Kerim";
        int age = 98;

        stringstream ss;

        ss<<"Name is : ";
        ss<<name;
        ss<<"     ";
        ss<<"Age is : ";
        ss<<age;

        string info = ss.str();

        cout<<info;

        cout<<endl<<endl<<"-------"<<"String Stream Scope End"<<"-------"<<endl;
    }

    cout<<endl<<"-------------------------------------------------------"<<endl;

    {
        cout<<endl<<"-------"<<"Person Class Scope Start"<<"-------"<<endl<<endl;

        Person person1;
        cout<<person1.toString()<<endl;

        Person person2("Mikky");
        cout<<person2.toString()<<endl;

        Person person3("Co", 45);
        cout<<person3.toString()<<endl;

        Person person4(19);
        cout<<person4.toString()<<endl;

        cout<<endl<<endl<<"-------"<<"Person Class Scope Start"<<"-------"<<endl;
    }

    cout<<endl<<"-------------------------------------------------------"<<endl;


    {
        cout<<endl<<"-------"<<"Pointers of Arrays  Scope Start"<<"-------"<<endl<<endl;

        string texts[] = {"one", "two", "three"};

        string *ptr = texts;

        int sizeArr = sizeof(texts)/sizeof(string);

        for( int i = 0; i<sizeArr;  i++){
            cout << ptr[i] << " "<<flush;
        }

        cout<<endl;

        for( int i = 0; i<sizeArr;  i++){
            cout << *ptr << " "<<flush;
        }

        cout<<endl;

        for( int i = 0; i<sizeArr;  i++){
            cout << *ptr << " "<<flush;

            ptr += 1; //ptr++;
        }

        cout<<endl;
        cout<<endl;

        string *pFirst = &(texts[0]); // or : string *pFirst = &texts
        string *pEnd = &(texts[2]);

        while(true){
            cout <<*pFirst<< " " <<flush;

            if(pFirst == pEnd) break;

            pFirst++;
        }

        cout<<endl<<"-------"<<"Pointers of Arrays  Scope End"<<"-------"<<endl<<endl;

    }

    {
        cout<<endl<<"-------"<<"Pointers Arithmetc Scope Start"<<"-------"<<endl<<endl;

        const int NSTRINGS = 5;

        string texts[] = {"one", "two", "three", "four", "five"};

        string *ptr = texts;

        cout<<*ptr<<endl;

        ptr = ptr + 1;

        cout<<*ptr<<endl;

        ptr += 1;

        cout<<*ptr<<endl;

        ptr -= 5;

        cout<<*ptr<<endl;

        string *pEnd = &texts[NSTRINGS];

        ptr = &texts[0];

        while(ptr != pEnd){
            cout << *ptr << endl;
            ptr++;
        }

        ptr = &texts[0];
        int elements = pEnd - ptr;
        cout<<elements<<endl;

        ptr = &texts[0];
        ptr += NSTRINGS/2;
        cout<<*ptr<<endl;

        cout<<endl<<"-------"<<"Pointers Arithmetic  Scope End"<<"-------"<<endl<<endl;

    }

    {
        cout<<endl<<"-------"<<"Char Arrays Scope Start"<<"-------"<<endl<<endl;

        char text1[] = "hello";
        char text2[5] = {'h', 'e', 'l', 'l','o'};

        for(int i = 0; i<sizeof(text1); i++){
            cout<<i<< ":" << text1[i]<<endl;
        }

        cout<<endl;
        int k = 0;
        while(true){

            if(text1[k] == 0) break;
            cout<<k<< ":" << text1[k]<<endl;

            k++;
        }


        cout<<endl<<"-------"<<"Char Arrays  Scope End"<<"-------"<<endl<<endl;

    }

    {
        cout<<endl<<"-------"<<"Reversing String Scope Start"<<"-------"<<endl<<endl;

        char text[] = "hello";

        int len = sizeof(text) - 1;

        char * pStart = text;

        char * pEnd = text + len - 1;

        cout<<" first  : "<<pStart[0]<<endl;

        cout<<" end : "<<pEnd<<endl;

        while(pStart < pEnd ){

            char save = *pStart;
            *pStart = *pEnd;
            *pEnd = save;

            pStart++;
            pEnd--;
        }

        cout<<endl<<text<<endl;

        cout<<endl<<"-------"<<"Reversing String Scope End"<<"-------"<<endl<<endl;

    }

    {
        cout<<endl<<"-------"<<"References Scope Start"<<"-------"<<endl<<endl;

        int val1 =8;
        int val2 = val1;
        val2 = 10;

        cout << "value 1 : "<<val1<<endl;
        cout << "value 2 : "<<val2<<endl;

        //int val1 =8;
        int &val3 = val1;
        val3 = 10;

        cout << "value 1 : "<<val1<<endl;
        cout << "value 3 : "<<val2<<endl;


        double value = 4.321;
        changeSomethingNorm(value);
        cout<<value<<endl;


        value = 4.321;
        changeSomethingRef(value);
        cout<<value<<endl;

        cout<<endl<<"-------"<<"References Scope End"<<"-------"<<endl<<endl;

    }

    {
        cout<<endl<<"-------"<<"Const Keyword Scope Start"<<"-------"<<endl<<endl;

        const double PI = 3.141592;
        // that will occur error  > value = 10;
        //because of the cost constant
        cout<<PI<<endl;

        Animal animal;
        animal.setName("Freffedy");
        animal.speak();

        int valTest = 234;

        int value0 = 13;
        int *pVal0 = &value0;
        *pVal0 = 30 ;
        cout <<*pVal0 << endl;
        pVal0 = &valTest;
        cout <<*pVal0 << endl;

        int value1 = 8;
        const int *pVal1 = &value1;
//      *pVal1 = 12 ;// will occure error
        cout <<*pVal1 << endl;


        int value2 = 10;
        int *const pVal2 = &value2;
//      pVal2 = &value1; //will occure error
        *pVal2 = 12;
        cout <<*pVal2 << endl;

        int value3 = 14;
        const int * const pVal3 = &value3;
//      *pVal3 = 12 ;// will occure error
//      pVal3 = &value1; //will occure error
        cout <<*pVal3 << endl;

        cout<<endl<<"-------"<<"Const Keyword  Scope End"<<"-------"<<endl<<endl;
    }

    {
        cout<<endl<<"-------"<<"Copy Constructor  Scope Start"<<"-------"<<endl<<endl;
        ///watch again that wideo seriws
        Animal animal1;
        animal1.setName("Jooooe");
        //that will call copy construstor...
        Animal animal2 = animal1;

        animal2.speak();


        animal1.speak();

        animal2.setName("Boooeeee");
        animal2.speak();

        //that will call copy cnstructor also
        Animal animal3(animal1);
        animal3.speak();

        cout<<endl<<"-------"<<"Copy Constructor  Scope End"<<"-------"<<endl<<endl;

    }

    {
        cout<<endl<<"-------"<<"New Operator Scope Start"<<"-------"<<endl<<endl;

        Creature cat;
        cat.setName("Tom");
        cat.speak();

        Creature *pCrtr = new Creature();
        pCrtr->setName("Jerry");
//      (*pCrtr).setName("Jerry");
        pCrtr->speak();
//      (*pCrtr).speak();

        // if we will use new operator
        // we have to destroy the object ourselvew
        // to prevent extra ram usage
        delete pCrtr;

        Creature *pCrtr2 = NULL;

        cout<< sizeof(pCrtr)<<"bytes"<<endl;

        cout<<endl<<"-------"<<"New Operator  Scope End"<<"-------"<<endl<<endl;

    }

    {
        cout<<endl<<"-------"<<"Returning Object From Function Scope Start"<<"-------"<<endl<<endl;

        Creature frog1 = createCreatureNorm();
        frog1.setName("Bitch Boy1 :)");
        frog1.speak();

        /* Program will crash with that

        Creature &frog2 = createCreatureRef();
        frog2.setName("Bitch Boy2 :)");
        frog2.speak();

        cout<<endl<<"-------"<<"Returning Object From Function  Scope End"<<"-------"<<endl<<endl;
        */

        Creature *frog3 = createCreaturePtr();
        frog3->setName("Bitch Boy3 :)");
        frog3->speak();

        delete frog3;

    }

    {
        cout<<endl<<"-------"<<"Allocating Memory Scope Start"<<"-------"<<endl<<endl;

            int *ptr = new int;

            *ptr = 8;
            cout << *ptr <<endl;

            delete ptr;

            Creature *pCrtr = new Creature[10];

            pCrtr[5].setName("another bitch boy.");
            pCrtr[5].speak();

            delete [] pCrtr;

            char*pMem = new char[1000];
            delete [] pMem;

            char c = 'a';

            string name(12,c);
            cout<<name<<endl;

            c++;

            string name2(12,c);
            cout<<name2<<endl;

            c++;

            string name3(12,c);
            cout<<name3<<endl;

        cout<<endl<<"-------"<<"Allocating Memory Scope End"<<"-------"<<endl<<endl;

    }

    {
        cout<<endl<<"-------"<<"Arrays and Functions Scope Start"<<"-------"<<endl<<endl;

        string t[] = {"apple", "orange", "banana"};
        showString(t,3);
        cout<<sizeof(t)<<endl;
        showStringPtr(t,3);
        showStringPtr2(t);

        char *pMemory = getMemory();

        freeMemory(pMemory);
        // delete pMemory;


        cout<<endl<<"-------"<<"Arrays and Functions Scope End"<<"-------"<<endl<<endl;

    }

    {
        cout<<endl<<"-------"<<"Allocating Memory Scope Start"<<"-------"<<endl<<endl;

        string t[] = {"apple", "orange", "banana"};
        showString(t,3);
        cout<<sizeof(t)<<endl;
        showStringPtr(t,3);
        showStringPtr2(t);

        char *pMemory = getMemory();

        freeMemory(pMemory);
        // delete pMemory;


        cout<<endl<<"-------"<<"Allocating Memory Scope End"<<"-------"<<endl<<endl;

    }

    {
        cout<<endl<<"-------"<<"Namespaces Scope Start"<<"-------"<<endl<<endl;

        namespace2::testCls tester1;

        tester1.speak();

        namespace1::testCls tester2;

        tester2.speak();

        //try commentout namespace1 and run that again :
        cout<<bitchName<<endl;

        cout<<namespace1::bitchName<<endl;
        cout<<namespace2::bitchName<<endl;

        cout<<endl<<"-------"<<"Namespaces Scope End"<<"-------"<<endl<<endl;

    }

    return 0;
}






