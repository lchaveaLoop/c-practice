#ifndef LINKLIST_H_
typedef int Status;
#define MAX_SIZE 100
typedef int Datatype;
#define ERROR 1
#define OK 1

//静态顺序表结构体
typedef struct sqllist
{
    Datatype ElemArray[MAX_SIZE];
    int length;
} SQList;

//动态顺序表结构体
typedef struct N_sqlist
{
    Datatype *elem;
    int length;
    int maxsize;
} NSQList;

//单链表节点
typedef struct LNode
{
    Datatype data;
    struct LNode *next;
} LNode, *linklist;
//linklist为结构体指针

//双向链表
typedef struct Dulnode
{
    Datatype elem;
    struct Dulnode *prior, *next;
} Dulnode;

//静态链表
typedef struct component
{
    /* data */
    Datatype data;
    int cur;
};

#endif LINKLIST_H_