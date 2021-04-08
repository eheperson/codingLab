#ifndef CREATURE_H
#define CREATURE_H

#include <iostream>
#include <sstream>
#include<string>

using namespace std;


class Creature
{
    private:
        string name;

    public:
        Creature();
        Creature(const Creature& other);
        ~Creature();

        void setName(string name);
        void speak() const;

    protected:


};


Creature createCreatureNorm();

Creature& createCreatureRef();

Creature* createCreaturePtr();

#endif // CREATURE_H
