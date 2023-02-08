#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);
    int *a = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) 
        scanf("%d", &a[i]);


    int m;
    scanf("%d", &m);
    int *b = (int *)malloc(sizeof(int) * m);
    for (int i = 0; i < m; i++) 
        scanf("%d", &b[i]);
    

int *c = (int *)malloc(sizeof(int) * (n + m));
int ai = 0, bi = 0;

for (int i = 0; i < n + m; i++) 
{
    if (ai < n && (bi >= m || a[ai] < b[bi])) {
        c[i] = a[ai];
        ai++;
    } 
    else {
        c[i] = b[bi];
        bi++;
    }
}

for (int i = 0; i < n + m; i++) {
printf("%d ", c[i]);
}

free(a);
free(b);
free(c);

return 0;
}



