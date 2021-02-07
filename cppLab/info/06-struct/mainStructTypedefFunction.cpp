#include<iostream>
#include <cstring>

using namespace std;

typedef struct Student{
    char name[20];
    int points;
    double meanAveragePoint;
} Students;


void studentUpdateInfo(Students* studentVar, char name[], int point, double average);
void studentDisplayInfo(Students* studentVar);

int main(){

    //define a struct type
    Students Mehmet;

    studentUpdateInfo(&Mehmet, "Mehmet", 70, 3.75);

    studentDisplayInfo(&Mehmet);


    return 0;
}

void studentUpdateInfo(Students* studentVar, char name[], int point, double average){
    strcpy(studentVar->name, name);
    studentVar->points = point;
    studentVar->meanAveragePoint = average;
}

void studentDisplayInfo(Students* studentVar){
    cout << "Student's meanAveragePoints  : " << studentVar->meanAveragePoint << endl;
    cout << "Student's points             : " << studentVar->points << endl;
    cout << "Student's name               : " << studentVar->name << endl;
};
