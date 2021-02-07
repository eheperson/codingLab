#include <iostream>
using namespace std;

int main() {
	char texts[] = "hello";

	cout << "text : " << texts << endl;

	for(int i=0; i<sizeof(texts); i++) {
		cout << i << ": " << (int)texts[i] << endl;
	}

    for(int i=0; i<sizeof(texts); i++) {
		cout << i << ": " << texts[i] << endl;
	}

    int k = 0;

    while(true){
        if(texts[k] == 0) 
            break;
        
        cout << texts[k] << flush;

        k++;
    }

	return 0;
}