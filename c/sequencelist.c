#include<sequencelist.h>

bool listinit(seqlist *l)
{
	l->size = 0;
	return true;
}
datatype getelem(seqlist *l, int i, datatype *e)
{
	if (i<0 || i>l->size)
	{
		printf("ERROR\n");
		return false;
	}
	*e = l->list[i - 1];
	return *e;
}
bool insert(seqlist *l,int i,datatype *e)
{
	if (l->size == maxsize)
	{
		printf("线性表已满\n");
		return false;
	}
	if (i<0 || i>l->size+1)
	{
		printf("非法插入位置\n");
		return false;
	}
	if (i <= l->size)//插入位置不在表尾
	{
		for (int k = l->size; k >= i-1; k--)//插入位置元素及其后的元素后移
		{
			l->list[k + 1] = l->list[k];
		}
	}
	l->list[i - 1] = *e;
	l->size++;
	return false;
}
bool Delete(seqlist *l,int i,datatype *e)
{
	if (l->size == 0)
	{
		printf("顺序表为空\n");
		return 0;
	}
	if (i<0 || i>l->size)
	{
		printf("ERROR\n");
		return true;
	}
	*e = l->list[i - 1];
	if (i < l->size)
	{
		for (i=l->size;i>0;i--)
		{
			l->list[i - 1] = l->list[i];
		}
	}
	l->size--;
	return false;
}

bool MinDelete()
{

	return false;
}

void main()
{
	seqlist a;
	datatype x=0;
	datatype kk = 5;
	listinit(&a);
	//getelem(&a, 1, &x);
	//insert(&a,1,&kk);
	system("pause");
}


