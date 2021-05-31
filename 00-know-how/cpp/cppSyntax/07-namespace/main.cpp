/////////////////////////////////////
//  Namespace Example    ///////////
/////////////////////////////////////
/*
    Consider a situation, when we have two persons with the same name, Zara, 
    in the same class. Whenever we need to differentiate them definitely we 
    would have to use some additional information along with their name, 
    like either the area, if they live in different area or their 
    mother’s or father’s name, etc.

    A namespace is designed to overcome this difficulty and is used as additional 
    information to differentiate similar functions, classes, variables etc. with the 
    same name available in different libraries. Using namespace, you can define the 
    context in which names are defined. In essence, a namespace defines a scope.
*/
#include<iostream>
#include<stdio.h>

using namespace std;


// first name space
namespace first_space {
   void func() {
      cout << "Inside first_space" << endl;
   }
}

// second name space
namespace second_space {
   void func() {
      cout << "Inside second_space" << endl;
   }
}

// third name space
namespace third_space {
   void func() {
      cout << "Inside third_space" << endl;
   }
}

/// Nested Namespaces
namespace fourth_space {
   void func() {
      cout << "Inside fourth_space" << endl;
   }
   
   // second name space
   namespace fifth_space {
      void func() {
         cout << "Fifth space, inside fourth_space" << endl;
      }
   }
}

// The 'using' directive
using namespace third_space;
//using namespace fourth_space::fifth_space;


int main () {
   // Calls function from first name space.
   first_space::func();
   
   // Calls function from second name space.
   second_space::func(); 

   //we can use funtion directly with 'using' directive
   func();

   //nestednamespace
   fourth_space::fifth_space::func();
   system("Pause");
   return 0;
}

/////////////////////////////////////
//  Namespace Example    ///////////
/////////////////////////////////////