#include "bitree.h"
//先序遍历的非递归算法一
void PreOder(BiTNode *b)
{
    //创建栈
    BiTNode *st[MAX_SIZE], *p;
    int top = -1;
    //根节点入栈
    st[top] = *b;
    top++;
    //栈不为空，循环
    while (top > -1)
    {
        //退栈，访问节点
        p = st[top];
        top--;
        printf("data=%d", p->data);
        //右孩子入栈
        if (r != NULL)
        {
            st[top] = p->r;
            top++;
        }
        //左孩子入栈
        if (l != NULL)
        {
            st[top] = p->l;
            top++;
        }
    }
}

/*
先序遍历的非递归算法二
if(当前b树不为空)
{
    p=b;
    while(栈不为空或者p!=NULL)
    {
        访问p所指节点；
        将p进栈；
        p=p->lchild;
        if(栈不空)
        {
            出栈p；
            p=p->rchild;
        }
    }
}
*/