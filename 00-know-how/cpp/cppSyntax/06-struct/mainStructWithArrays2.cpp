#include<iostream>
#include<cstring>

using namespace std;

struct student{
    char name[50];
    char sname[50];
    int point;
    static int studentNo;
};

typedef struct student Students;
typedef Students* StudentsPtr;

int Students::studentNo = 0;

enum choices{
    Continue = 0,
    AddStudent = 1,
    DisplayStudent = 2,
    Exit = -1
};
typedef  enum choices Choice;

void addStudent(StudentsPtr);
void displayStudents(StudentsPtr);
void displayProgramInfo();

#define STUDENT_SIZE  5

int main(){
    Students std[STUDENT_SIZE];
    StudentsPtr stdPtr = std;   

    int choice = 0;

    while(choice != -1){

        displayProgramInfo();
        cout << "Please enter your choice  : ";
        cin >> choice;

        switch (choice){
            case AddStudent:
                addStudent(stdPtr);
                break;

            case DisplayStudent:
                displayStudents(stdPtr);
                break;

            case Exit:
                choice = -1;
                break;
            
            default:
                cout << "Please  select proper choices .. !" << endl;
                break;
        }
    }

    return 0;
}

void addStudent(StudentsPtr stdptr){
    char name[50];
    char surname[50];
    int point;

    cout << "Enter student name    : " ;
    cin >> name;
    cout << "Enter student surname : " ;
    cin >> surname;
    cout << "Enter student point   : " ;
    cin >> point;

    strcpy((*(stdptr + stdptr->studentNo)).name, name);
    strcpy((*(stdptr + stdptr->studentNo)).sname, surname);
    (*(stdptr + stdptr->studentNo)).point = point;

    stdptr->studentNo += 1;
}


void displayStudents(StudentsPtr stdptr){
    for(int i = 0; i<stdptr->studentNo; i++){
        cout << i+1 << ". strudent name    : " << (*(stdptr + i)).name  << endl;
        cout << i+1 << ". strudent surname : " << (*(stdptr + i)).sname << endl;
        cout << i+1 << ". strudent point   : " << (*(stdptr + i)).point << endl;
        cout << endl;
    }
}

void displayProgramInfo(){
    cout << "Add New Student           ->  1" << endl;
    cout << "Display Existing Students ->  2" << endl;
    cout << "Exit Program              -> -1" << endl;
}