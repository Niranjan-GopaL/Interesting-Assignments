#include <stdio.h>
#include <stdlib.h>

void main(){
    int n;
    scanf("%d",&n);
    int *a = (int*)malloc(n*sizeof(int));
    for (int i = 0; i < n; i++)
            {
                    scanf("%d",&a[i]);
            }
    int choice;
    scanf("%d",&choice);
    while (choice==1 || choice==2)
    {
        if (choice==1)
        {
            int temp = a[0];
            for (int i = 0; i < n-1; i++)
            {
                a[i]=a[i+1];
            }
            a[n-1]=temp;
            for (int i = 0; i < n; i++)
            {
                printf("%d ",a[i]);
            }
        }
        else
        {
            for (int i = 0; i <= n/2; i+=2)
            {
                int temp = a[i];
                a[i]=a[i+1];
                a[i+1]=temp;
            }
            for (int i = 0; i < n; i++)
            {
                    printf("%d ",a[i]);
            }
            
        }
        scanf("%d",&choice);
    }
    
}