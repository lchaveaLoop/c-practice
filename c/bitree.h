#include"sqllist.h"
#ifndef BITREE_H
typedef struct BiTNode
{
    Datatype data;
    BiTNode *l,*r;    
}BiTNode,*BiTree;