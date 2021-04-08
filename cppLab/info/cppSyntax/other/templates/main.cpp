#include<iostream>

using namespace std;

template <class Type>
Type GetAverage (Type a[], size_t n)
{
	Type sum ; 

  for (int i=0; i<n; i++) 

    sum += a[i]; 

    return sum/n; 
};

int main() {

  float FloatArray[3] = { 1.55f, 5.44f, 12.36f};

  int  IntArray[5] = {100, 200, 400, 500, 1000};

  cout << " Average of the integer array : " << GetAverage(IntArray, 5)<<endl;

  cout << " Average of the float array : " << GetAverage(FloatArray, 3)<<endl;

  return 0;

}