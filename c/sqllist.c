#include <stdlib.h>
#include <stdio.h>
#include "sqllist.h"

Status InitSqlist(SQList *L)
{
    L->ElemArray = (SQList　*)malloc(MAX_SIZE * sizeof(LNode)); //申请MAX_size个LNode
    if (!L->ElemArray)
    {
        return ERROR;
    }
    else
    {
        L->length = 0;
        return OK;
    }
};

Status InsertSqlist(SQList *L, int i, Datatype e)
{
    int j;
    if (i < 0 || i > L->length - 1) //插入位置不合理
        return ERROR;
    if (L->length =
            MAX_SIZE) //顺序表已满
    {
        printf("溢出！\n");
        return ERROR;
    }
    for (j = L->length - 1; j >= i - 1; --i) //移动ｉ－１后的所有节点
    {
        L->ElemArray[j + 1] = L->length[j];
        L->ElemArray[i - 1] = e; //在i-1处插入
        L->length++;
        return OK;
    }
}

Status DeleteSqlist(SQList *L, int i)
{
    int x;
    Datatype k;
    if (L->length == 0)
    {
        printf("顺序表为空\n");
        return ERROR
    }
    else if (i < 0 || i > L->length - 1)
    {
        printf("该元素不在顺序表中\n");
        return ERROR;
    }
    else
    {
        x = L->ElemArray[i - 1]; //保存删除节点的值
        for (k = i; k < L->length; i++)
        {
            L->ElemArray[k - 1] = L->ElemArray[k]; //ｉ后的节点位置往前移一位
            L->length--;
            return (x);
        }
    }
}

Status LocateSqlist(SQList *L, Datatype e)
//删除顺序表中值为e的第一个元素
{
    int k, i = 0;
    while (i < L->length)
    {
        /* code */
        if (L->ElemArray[i] != e)
        {
            i++
        }
        else
        {
            for (k = i + 1; k < L->length; k++)
            {
                L->ElemArray[k - 1] = L->ElemArray[k];
            }
            L->length--;
            break;
        }
    }
    if (i > L->length) //在顺序表中无本元素
    {
        printf("次元素不在本顺序表中\n");
        return ERROR;
    }

    return OK;
}

LNode *creat_Linklist(void) //头插法
{
    int data;
    LNode *head, *p;
    head = (LNode *)malloc(sizeof(LNode));
    head->next = NULL;
    scanf("data=%d\n", &data);
    while (1)
    {
        if (data == 32767)
            break; //如果输入数据达到最大值
        p = (LNode *)malloc(sizeof(LNode));
        p->data = data;
        p->next = head->next;
        head->next = p; //将新创建的节点链接为首节点
    }
    return head;
}

LNode *creat_Linklist_tail(void) //尾插法
{
    int data;
    LNode *head, *p, *last;
    head = (LNode *)malloc(sizeof(LNode));
    head->next = NULL;
    while (1)
    {
        if (data == 32767)
            break;
        p = (LNode *)malloc(sizeof(LNode));
        scanf("data=%d\n", &data);
        p->data = data;
        p->next = last->next;
        last->next = p;
        last = p;
    }
    return head;
}

Datatype Get_elem(LNode *L, int i)
{
    int j, LNode *P; //ｊ为计数器，ｐ为工作指针
    p = L->next;
    j = 1;
    while (p != NULL && j < i)
    {
        p = p->next;
        j++;
    }
    if (j != i)
    {
        return -32768;
    }
    else
        return p->data;
}

LNode *Locate_elem(LNode *L, Datatype key)
{
    LNode *p;
    P = L->next;
    while (p != NULL && p->data != key)
    {
        /* code */
        p = p->next;
    }
    if (p->data == key)
    {
        /* code */
        return p;
    }
    else
    {
        printf("所查找节点不存在\n");
        return NULL;
    }
}

LNode *Insert_Lnode(LNode *L, int i, Datatype e)
{
    int j = 0;
    LNode *p, *q;
    p = L->next;
    while (p != NULL && j < i - 1)
    {
        /* code */
        p = p->next;
        j++;
    }
    if (j != i - 1)
    {
        /* code */
        printf("插入位置不存在");
    }
    else
    {
        q = (LNode *)malloc(sizeof(LNode));
        q->data = e;
        q->next = p->next;
        p->next = q;
    }
}

LNode *Delet_Lnode(LNode *L, int i)
{
    int j = 1;
    LNode *p, *q;
    p = L;
    q = L->next;
    while (p != NULL && j < i)
    {
        /* code */
        p = q;
        q = q->next;
        j++;
    }
    if (j != i)
    {
        printf("删除位置不存在\n");
    }
    else
    {
        p->next = q->next;
        free(q);
    }
}

LNode *Delet_Londe(LNode *L,Datatype key)
{
    LNode *p,*q;
    p=L;q=L->next;
    while (q!=NULL&&q->data!=key)
    {
        /* code */
        p=q;
        q=q->next;
    }
    if (q->data==key)
    {
        /* code */
        p->next=q->next;
        free(q);
    }
    else
    {
        printf("删除元素不存在\n");
    }
    
    
}

LNode Mrege_LinkList(LNode *La,LNode *Lb)
{
    LNode *Lc,*pa,*pb,*pc,*ptr;
    Lc=La; pc=La;//La的头结点作为Lc的头结点
    pa=La->next;
    pb=Lb->next;
    while (!pa&&!pb)
    {
        if(pa->data>pb->data)
        {
            Lc->next=pb;
            pc=pb;
            pb=pb->next;
        }
        if(pa->data<pb->data)
        {
            Lc->next=pa;
            pc=pa;
            pa=pa->next;
        }
        if(pa->data==pb->data)
        {
            Lc->next=pa;
            pc=pa;
            pa=pa->next;
            ptr=pb;pb=pb->next;
            free(ptr);
        }
        if(!pa)
            pc->next=pa;
        else
            pc->next=pb;
        free(Lb);
        return Lc;
    }
     
}