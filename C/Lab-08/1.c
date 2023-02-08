#include <stdio.h>
#include <stdlib.h>

void main(){
    int n;
    scanf("%d",&n);
    int temp =n;
    do
    {
        int *a;
        if (n<=temp)
        {
            a =(int*) malloc(n*sizeof(int));
            for (int i = 0; i < n; i++)
                {
                        scanf("%d",&a[i]);
                }
        }
        else
        {
            free(a);
            a =(int*) malloc(n*sizeof(int));
            for (int i = 0; i < n; i++)
                {
                        scanf("%d",&a[i]);
                }
        }
        for (int i = 0; i < n; ++i) {
                    printf("%d ",a[i]);
            }  
        int temp = n;
        scanf("%d",&n);
        } while (n>0);
    
}