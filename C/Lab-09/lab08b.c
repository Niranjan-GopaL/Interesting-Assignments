#include <stdio.h>
#include <stdlib.h>

void main()
{
	//Taking in array a
	int n;scanf("%d",&n);
	int *a=(int*)malloc(sizeof(int)*n);
	for(int i=0;i<n;i++)
	{ 
		scanf("%d",&a[i]);
	}
	
	//Taking in array b 
	int m;scanf("%d",&m);
	int *b=(int*)malloc(sizeof(int)*m);
	for(int i=0;i<m;i++)
	{ 
		scanf("%d",&b[i]);
	}

	//Constructing array c
	int *c=(int*)malloc(sizeof(int)*(n+m));
	int flag=0;
	int ai=0,bi=0;
	for(int i=0;i<n+m;i++)
	{ 
	//flag=0 is the normal mode (when an element of array b is negetive then flag=1 ,special case)
		if(flag == 0)
		{
			if(i&2==0)
			{
				c[i]=a[ai];
				ai++;
			}
			else
			{
				c[i]=b[bi];
				bi++;
				if (b[bi]<0)
					{flag=1;}
			}
		}
	//flag=1 is for construction after a negetive element has been found
		else
		{
			if(ai<n)
			{
				c[i]=a[ai];
				ai++;
			}
			else
			{
				if (bi<m)
				{
				c[i]=b[bi];
				bi++;
				}
			}
		}
	}
	for(int i=0;i<n+m;i++)
	{
		printf("%d ",c[i]);
	}
}
