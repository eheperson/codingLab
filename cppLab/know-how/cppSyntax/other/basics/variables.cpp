

#include<iostream>

using namespace std;

int main(){

    int item1 = 6;
    int item2 = 4;

    int totalItems = item1 + item2;

    cout << "Number of Items 1 :" << item1 << endl;
    cout << "Number of Items 2 :" << item2 << endl;

    cout << "Total Number of Items:" << totalItems << endl;

    cout << "New item 1 added to inventory ! " << endl;

    item1 += 1;

    cout << "Number of Items 1 :" << item1 << endl;


    return 0;
}