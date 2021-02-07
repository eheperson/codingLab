#ifndef NS1_H
#define NS1_H

#include <iostream>
#include <sstream>
#include<string>

using namespace std;

namespace namespace1{

    const string bitchName = "Gerrard";

    class testCls{
        public:
            testCls();
            virtual ~testCls();
            void speak();

        protected:

        private:
    };
};

#endif // NS1_H
