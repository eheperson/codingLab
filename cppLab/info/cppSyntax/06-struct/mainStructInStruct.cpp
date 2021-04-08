#include<iostream>
#include <cstring>

using namespace std;

typedef struct stringOperation{
    char name[50];
    char surName[50];
} strStructOperation;


typedef struct Student{
    strStructOperation info;
    int points;
    double meanAveragePoint;
}Students;
// or
// typedef struct Student Students;


typedef Students* ptrStudent;

void studentUpdateInfo(Students* studentVar, 
                        char name[], 
                        char sname[], 
                        int point, 
                        double average);

void studentDisplayInfo(Students* studentVar);

int main(){

    //define a struct type
    Students Mehmet;

    ptrStudent  ptrMehmet = &Mehmet;

    studentUpdateInfo(ptrMehmet, "Mehmet", "Iscan", 70, 3.75);

    studentDisplayInfo(ptrMehmet);

    cout << "Acces From main() scope  : " << endl;

    cout << "Student's name               : " << Mehmet.info.name << endl;
    cout << "Student's surname            : " << Mehmet.info.surName << endl;
    cout << "Student's meanAveragePoints  : " << Mehmet.meanAveragePoint << endl;
    cout << "Student's points             : " << Mehmet.points << endl;

    cout << "Acces From main() via struct pointer scope  : " << endl;

    cout << "Student's name               : " << ptrMehmet->info.name << endl;
    cout << "Student's surname            : " << ptrMehmet->info.surName << endl;
    cout << "Student's meanAveragePoints  : " << ptrMehmet->meanAveragePoint << endl;
    cout << "Student's points             : " << ptrMehmet->points << endl;


    return 0;
}

void studentUpdateInfo(Students* studentVar, 
                        char name[],
                        char sname[], 
                        int point, 
                        double average){

    strcpy(studentVar->info.name, name);
    strcpy(studentVar->info.surName, sname);
    studentVar->points = point;
    studentVar->meanAveragePoint = average;
}

void studentDisplayInfo(Students* studentVar){
    cout << "Student's name               : " << studentVar->info.name << endl;
    cout << "Student's surname            : " << studentVar->info.surName << endl;
    cout << "Student's meanAveragePoints  : " << studentVar->meanAveragePoint << endl;
    cout << "Student's points             : " << studentVar->points << endl;
};
