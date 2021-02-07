#include <iostream>
#include <iomanip>
using namespace std;

int main() {

	float value1 = 1.1;

	if(value1 == 1.1) {
		cout << "equals" << endl;
	}
	else {
		cout << "not equal" << endl;
	}

	if(value1 < 1.11) {
		cout << "equals" << endl;
	}
	else {
		cout << "not equal" << endl;
	}

	cout << setprecision(10) << value1 << endl;


	return 0;
}