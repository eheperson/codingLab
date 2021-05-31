#include<iostream>
#include<cstring>

using namespace std;

struct student{
    char name[50];
    char surName[50];
    int point;
};



typedef struct student Student;
typedef Student* ptrStudent;


#define STUDENT_SIZE 3




void initStudent(ptrStudent studentVar, int size);
void displayStudent(ptrStudent studentVar, int size);

int main(){

    Student std[STUDENT_SIZE];
    ptrStudent stdPtr = std;

    initStudent(stdPtr, STUDENT_SIZE);

    displayStudent(stdPtr, STUDENT_SIZE);

    return 0;
}

void initStudent(ptrStudent studentVar, int size){

    char name[50];
    char sname[50];
    int point;

    for(int i = 0; i<size; i++){
        cout << "Enter the first student name    :";
        cin >> name;
        cout << "Enter the first student surname :";
        cin >> sname;
        cout << "Enter the first student point   :";
        cin >> point;

        strcpy(studentVar->name, name);
        strcpy(studentVar->surName, sname);
        studentVar->point = point;
    };
};


void displayStudent(ptrStudent studentVar, int size){
    for(int i = 0; i<size; i++){
        cout << "Name of the first student    :" << studentVar->name << endl;
        cout << "Surname of the first student :" << studentVar->surName << endl;
        cout << "Point of the first student   :" <<studentVar->point << endl;
    }
};