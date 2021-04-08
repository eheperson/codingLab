/*
STL or 'Standard Template Library', is a set of template classes to provide
common programming data structures and algorithms

TheSTL is made up of four main groups:
    - Algorithms
    - Containers
    - Functions
    - Utilities

STL defines a collection of standalone functions that can act on ranges of elements(iterators)
They do various typesof tasks : 
    - Non-modifying(search, compare, count)
    - Modifying (copy, move, replace, fill, partition, sort, shuffle)

Having a good knowledge of what is available from the Standard Tmeplate Library
will accelerate our programming and help us avoid re-solving low-level problems



--------CONTAINERS :

- The bread and butter of STL containers is what most developers think of
  when thet think of the C++ standard libary : 

- Provides different categories of containers:
    .Sequence Containers > vector, list, deque
    .Associative Containers > sets, maps
    .Adapter Containers > queue, stack

- STL provides function objects called functors that can be used just like functions
  They achieve this by creating a class with an operator overload of the operator()
  Some of the functionality they provide are : 
    - Aritmetic 
    - Comparison
    - Logical
  These can be used anywhere a callable is expected  

- Especially with the C++11, there are several STL headers that don't really
  fall under a category and can be considered as utilities:
    -Threads
    -Iterators
    -Chono(time)
    -Any
    -Memory

-------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------

UNDERSTANDING C++ TEMPLATES 

-To understand the C++ STL, we must first understand C++ temlates
 and what they are offer us, as programers
-Templates allow programmers to write generic C++ code that
 can apply to many different types of data 


*/

#include<iostream>

template<typename T> /* Templated Class*/
//our templated class called Container
class Container{
    T t;

    public :
        //
        explicit Container(T t): t(t){};

        /*friend funcion of the operator overload forthe insertion operator
          this will allow us to use our object into a cout call directly.
         >> This is very convenoent if we want to start outputting the contents
        of out object without having actually call individual functions on them
          */
        friend std::ostream& operator<<(std::ostream& os, const Container<T>& c){
            return (os << "Container holding : " << c.t);
        }
};
///*************************************************************************
///*************************************************************************
template<typename X> /* Templated Function */
bool isGreator(X x1, X x2){
    return x1 > x2;
};
///*************************************************************************
///*************************************************************************
/* We can also create specialized templates
   A specialized template  allows us to  do something specific for a specific type.

Templated function works for any type but
what if want to do something different if the template is
defined as an int.

To do that : : : : Specialized Templates

if we try to create call to this templated for int, 
it will cal that specialized function instead (becarefull ! syntaxes are same)
*/
template<> /*specoalizedtemplated fucntion (inside brackets is empty for specialized template)>
bool isGreator(int x1, int x2){
    std::cout<<"Specialized for int" << endl;
    return x1 > x2;
};
///*************************************************************************
///*************************************************************************
using namespace std;
int main(){
  cout << std::boolalpha;

  Container <string> s("ello"); 
  Container <int> c(30);
  /* tell the compiler we want hold int 
  so > is that the template typename 'T' is replaced with int
  everywhere there's a 'T, it's replaced by the word int

  WE CAN DO DAT FOR OUR SPECIFIC DATATYPES ALSO
  */

  /* same thing for string*/

  cout << s << endl;
  cout << c << endl;
    
  cout <<isGreator(5,10) << endl;
  cout <<isGreator(23.56,34.56) << endl;
  cout <<isGreator("zzz", "xxx") << endl;
  cout << isGreator("c", "r")<< endl;

  system("Pause");

  /* Also we can create templates as lambda functions
  normal lambda syntax : []()
  in these case : [] <template T> ()
  */

  auto f = [] <typename T> (T t1, T t2){
    return t1 == t2;
  }

  cout << "Lambda Returns : " << f(10, 10) << "\n";
  
  return 0;
}  