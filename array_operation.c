#include <stdio.h>

void print_arrays(int *a,int *b,int n)
{
    if (n==0)
    {
        printf("<empty>");
    }
    
    for (int i = 0; i < n; i++)
    {
        printf("%d %d\n",a[i],b[i]);
    }
}


int find_match(int *a,int *b,int n,int val)
{
    for (int i = 0; i < n; i++)
    {
        if (a[i]==val)
        {
            return b[i];
        }
    }
    return -1;
}

int update_match(int *a,int *b,int n,int val,int bval)
{
    for (int i = 0; i < n; i++)
    {
        if (a[i]==val)
        {
            b[i]=bval;
            return 0;
        }
        
    }
    return -1;
}

int delete_match(int *a,int *b,int n,int val)
{
    for (int i = 0; i < n; i++)
    {
        if (a[i]==val)
        {
            for (int j = i; i < n-1; j++)
            {
                a[j]=a[j+1];
                b[j]=b[j+1];
            }
            return 0;   
        }
    }
    return -1;
}

void main(){
    int n;
    scanf("%d",&n);
    int ids[n];
    int marks[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d",&ids[i],&marks[i]);
    }
    int choice;
    scanf("%d",&choice);
    while (choice>0 && choice<5)
    {
        switch (choice)
        {
        case 1:
            print_arrays(ids,marks,n);
            break;

        case 2:
            int i,val;
            scanf("%d",&i);
            val = find_match(ids,marks,n,i);
            if (val==-1)
            {
                printf("<value-not-found>");
            }
            else
            {
            printf("%d",val);
            }
            break;

        case 3:
            int val1,bval,val3;
            scanf("%d %d",&val,&bval);
            val3 = update_match(ids,marks,n,val1,bval);
            if (val3 == -1)
            {
                printf("<value-not-found>");
            }
            break;
        case 4:
            int val2,val4;
            scanf("%d",&val2);
            val4 = delete_match(ids,marks,n,val2);
            if (val4==-1)
            {
                printf("<value-not-found>");
                n++;
            }
            n=n-1;
            break;
        }
        scanf("%d",&choice);
    }
    
    
}