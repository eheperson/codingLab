/*
    C/C++ arrays allow you to define variables that combine several 
    data items of the same kind, but structure is another user defined 
    data type which allows you to combine data items of different kinds.

    Syntax:
        struct [structure tag] {
            member definition;
            member definition;
            ...
            member definition;
            } [one or more structure variables];  

    > To access any member of a structure, we use the member access operator (.).
*/

//structure decleration 

struct Student{
    char name[20];
    int points;
    double meanAveragePoint;
};

/* or

struct Student{
    char name[20];
    int point;
    double meanAverage;
} std1;

toaccess member of std1 in main() scope :
    std1.name = 'eeee';
    std1.point = 45;
    std1.meanAverge = 45.6;

*/

#include<iostream>
#include <cstring>

using namespace std;


int main(){

    //define a struct type
    struct Student Mehmet;

    //assign values to struct type
    Mehmet.meanAveragePoint = 3.15;
    Mehmet.points = 70;
    
    // assignment to char array
    //  to assign name we must use strcpy()
    strcpy(Mehmet.name, "Mehmet");

    cout << "Mehmet's meanAveragePoints  : " << Mehmet.meanAveragePoint << endl;
    cout << "Mehmet's points             : " << Mehmet.points << endl;
    cout << "Mehmet's name               : " << Mehmet.name << endl;


    return 0;
}