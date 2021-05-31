#ifndef _ESSENCE_H_
#define _ESSENCE_H_

#include <iostream>

using namespace std;

class essence{
    
    private:
    /*A private member variable or function cannot be accessed, 
    or even viewed from outside the class. 
    Only the class and friend functions can access private members.*/
        
        // private members go here

        /* Private Member Variable (attribute or) */
        int testPrivate;

        /* Private Mutators*/
        void setPrivate(int p);

        /* Private Accessor*/
        int getPrivate(void);

    public:
    /*A public member is accessible from anywhere 
    outside the class but within a program. 
    You can set and get the value of public 
    variables without any member function*/

        // public members go here

        /* Public Member Variable (attribute or) */
        int testPublic;

        /* Public Mutators*/
        void setPublic(int p);

        /* Public Accessor*/
        int getPublic(void);
    
    protected:
    /*A protected member variable or function 
    is very similar to a private member 
    but it provided one additional benefit 
    that they can be accessed in child classes 
    which are called derived classes.*/

        // protected members go here

        /* Protected Member Variable (attribute or) */
        int testProtected;

        /* Protected Mutators*/
        void setProtected(int p);

        /* Protected Accessor*/
        int getProtected(void);

};

#endif