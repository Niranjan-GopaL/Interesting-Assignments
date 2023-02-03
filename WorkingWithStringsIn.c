#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int read_strings(char *a[], int n){

}

void swap(int a[], int i, int j){
	int t = a[i];
	a[i]=a[j];
	a[j]=t;
}

void swap_greaterup(int a[], int i){
	if (a[i] > a[i+1] )
		swap(a,i,i+1);
}

void repeat_swap_greaterup(int *a[], int n){
	for(int i=0;i<n-1;i++)
		swap_greaterup(a,i);
}

void sort_strings(char *a[], int n)
// By bubble sort
{
	for(int i=0; i < n-1 ; i++)
	    repeat_swap_greaterup(a,n); // do the repeated swap: (n-i, maybe?)
}



void main(){
    
}