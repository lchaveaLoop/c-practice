#ifndef STACK_H
#define STACK_SIZE 100 //初始大小
#define STACKINCREMENT 10 //增量大小
typedef int status;
typedef int Datatype;
typedef int Elem;
typedef struct sqstack
{
    /* data */
    //struct sqstack 
    Datatype *top;
    //struct sqstack 
    Datatype *bottom;
    int stacksize ;
}SQstack;
typedef struct LinkNode{
    Datatype data;
    struct LinkNode *next;
}*LiStack;
#endif STACK_H