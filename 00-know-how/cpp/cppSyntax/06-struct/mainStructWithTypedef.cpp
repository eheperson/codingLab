#include<iostream>
#include <cstring>

using namespace std;

typedef struct Student{
    char name[20];
    int points;
    double meanAveragePoint;
} Students;


int main(){

    //define a struct type
    Students Mehmet;

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