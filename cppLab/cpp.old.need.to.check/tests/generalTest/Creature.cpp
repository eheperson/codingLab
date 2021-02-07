#include "Creature.h"


Creature::Creature(){
    cout<< "Creature Created !!"<<endl;
};

Creature::~Creature(){
    cout<< "Creature Destroyed for : "<< name<<endl;
};

Creature::Creature(const Creature& other){
    name = other.name;
    cout<< "Creature Created by Copying !!"<<endl;
};



void Creature::setName(string name){
    this->name = name;
}

void Creature::speak() const{
    cout<<"My name is :"<<name<<endl;
}

Creature createCreatureNorm(){
    Creature a;
    return a;
}

Creature& createCreatureRef(){
    Creature a;
    return a;
}

Creature* createCreaturePtr(){
    Creature *pCrtr = new Creature();
    return pCrtr;
}
