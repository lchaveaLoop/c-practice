#include "stack.h"
#include <stdio.h>
#include <stdlib.h>

status init()
{
    SQstack s;
    s.bottom = (Datatype)malloc(STACK_SIZE * sizeof(Datatype));
    if (s.bottom == NULL)
        return 0;
    s.top = s.bottom;
    s.stacksize = STACK_SIZE;
    return 1;
}

status push(SQstack s, Elem e)
{
    //if(s.bottom-s.top>=s.stacksize-1)
    if (s.bottom >= s.top - 1)
    {
        s.bottom = (Elem *)realloc(s.bottom, (STACK_SIZE + STACKINCREMENT) * sizeof(Elem));
        if (!s.bottom)
            return 0;
        s.top = s.bottom + STACKINCREMENT;
        STACK_SIZE += STACKINCREMENT;
        *s.top = e;
        s.top++;
    }
    else
    {
        printf_s("此栈已满！");
        return 0;
    }
}

status pop(SQstack s, Elem e)
{
    if (s.top == s.bottom)
    {
        printf_s("此栈为空!");
        return 0;
    }
    s.top--;
    e = *s.top;
    return 1;
}

status linkinit()
{
    LiStack a;
    a = (LiStack)malloc(sizeof(LinkNode));
    if (!a)
        return 0;
    a->next = NULL;
    return a;
}
status linkpush(LiStack top, Datatype e)
{
    LiStack p;
    p = (LiStack)malloc(sizeof(LinkNode));
    if (!p)
        return 0;
    p->data = e;
    p->next = top->next;
    return 1;
}
status linkpop(LiStack top, Datatype *e)
{
    LiStack p;
    if (top->next == NULL)
        return 0;
    p = top->next;
    e = p->data;
    top->next = p->next; //修改栈顶指针,栈顶指针往下移一位
    free(p);
    return 1;
}