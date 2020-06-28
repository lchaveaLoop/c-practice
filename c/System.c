#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>
#include<math.h>
struct PCB *head,*tail;


typedef struct PCB
{
	char ID[10];
	int RunTime;
	int pri;
	char state;
	struct PCB *next;
}PCB;

struct PCB* init(struct PCB &p, int n)
{
		p=(struct PCB *)malloc(sizeof(struct PCB));
		p->next=NULL;//建立一个带头节点的单链表
		for(int i=0;i<n;i++)
		{
			p = (struct PCB *)malloc(sizeof(struct PCB));//生产新节点
			p->ID[0] = 'p';
			p->ID[1] = i + '0';
			p->ID[2] = '0';
			printf("id:%d\n", p->ID);

			printf("please input pri\t");
			scanf("%d",&p->pri);

			printf("please input Runtime\t");
			scanf("%d",&p->RunTime);

			p->next = head->next;
			head->next = p;
		}
	/*
	p->ID[0] = 'p';
	p->ID[1] = i + '0';
	p->ID[2] = '0';
	printf("id:%d\n", p->ID);

	printf("please input pri\t");
    scanf("%d",&p->pri);

	printf("please input Runtime\t");
    scanf("%d",&p->RunTime);

	p->next = NULL;
	*/
	/*p->runtime = i+1;
	p->priority = i;
	p->status = 'R';*/

	return p;
}

/*
void run(struct PCB *p)
{
	printf("progress:%s,Runtime:%d,priority:%d", p->ID, p->RunTime, p->pri);
	if (p->RunTime > 0)
	{
		p->RunTime--;
	}
	if (p->pri > 0)
	{
		p->pri--;
	}

}
*/
/*
struct PCB * Change(struct PCB *p)
{
	p->next = head->next;
	head->next = p;
	printf("progress:%s,Runtime:%d,priority:%d", p->ID, p->RunTime, p->pri);
	return head->next;
}*/
/*
struct PCB * SecletID(struct PCB *s,int n ,struct PCB *t)
{
	int pMax = 0;
	int i=0;
	for (; i < n; i++)
	{
		while (s->pri>0)
		{
			if (s->pri>pMax)
			{
				pMax = s->pri;
				if (t->pri>pMax)
				{
					pMax = t->pri;
					Change(t);
					return t;
				}
				else if (t->pri == pMax)
				{
					t->next = s->next;
					s->next = t;
				}
				Change(s);
			}
		}
	}
	return s;
};
*/
void main()
{
	int n=0;
	printf("please input n");
	scanf("%d",&n);
	struct PCB *p ;//*q;//p为执行队列指针，q为待插入队列指针
	init(p,n);

}
