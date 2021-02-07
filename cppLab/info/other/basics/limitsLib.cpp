#include<iostream>
#include<limits>




int main() {
   std::cout << "type\tlowest type\thighest type\n";
   std::cout << "int\t"<< std::numeric_limits<int>::lowest() << '\t'<< std::numeric_limits<int>::max() << '\n';
   std::cout << "float\t"<< std::numeric_limits<float>::lowest() << '\t'<< std::numeric_limits<float>::max() << '\n';
   std::cout << "double\t"<< std::numeric_limits<double>::lowest() << '\t'<< std::numeric_limits<double>::max() << '\n';

   std::cout << std::endl << std::endl;

//   std::cout << "Max int value : " << INT_MAX << std::endl;
//   std::cout << "Min int value : " << INT_MIN << std::endl;

    return 0;
}