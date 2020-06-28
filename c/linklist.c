#include<stdio.h>
#include<linklist.h>

datatype getelem(linklist L,int i,datatype &e)
{
	int j=1;
	linklist p=L->next;
	j=1;
	while(p&&j<i)
	{
        p=p->next;
        ++j;
	}
	if(!p||j>i)
	return 0;
	e=p->data;
	return *e;
}
void init(linklist *L)
{
	*L = (linklist)malloc(sizeof(node));
}
bool insert(linklist &L,int i,datatype e)
{
    linklist p,s;
    int j=0;
    p=L;
    while(p&&j<i-1)
    {
        p=p->next;
        ++j;
    }
    if(!p||j>i-1)
        return false;
    s=(linklist)malloc(sizeof(node));
    s->data=e;
    s->next=p->next;
    p->next=s;
	return true;
}
bool listdelete(linklist &L,int i,datatype &e)
{
    linklist p,q;int j;
    p=L;
    j=0;
    while(p->next&&j<i-1)
    {
        p=p->next;
        ++j;
    }
    if(!p||j>i-1)
        return false;
    q=p->next;
    p->next=q->next;
	return true;
}
bool listcreat(linklist &L,int n)
{
    linklist p;
    L=(linklist)malloc(sizeof(node));
    L->next=NULL;
    for(i=n;i>o;i--)
    {
        p=(linklist)malloc(sizeof(node));
        scanf(&p->data);
        p->next=L->next;L->next=p;//插入到表头
    }
}

