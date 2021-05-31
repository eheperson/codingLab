#include "essence.h"

/* Public Member Function Definitions */
void essence::setPublic(int p){
            this->testPublic = p;
};

int essence::getPublic(void){
    return this->testPublic;
}

/* Private Member Function Definitions */
void essence::setPrivate(int p){
            this->testPrivate = p;
};

int essence::getPrivate(void){
    return this->testPrivate;
}


/* Protected Member Function Definitions */
void essence::setProtected(int p){
            this->testProtected = p;
};

int essence::getProtected(void){
    return this->testProtected;
}