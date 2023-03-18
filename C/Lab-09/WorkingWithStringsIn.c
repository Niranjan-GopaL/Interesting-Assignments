  #include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRING_LEN 20
#define MAX_IN_LINE 10

//_n is MAX_IN_LINE 
int read_strings(char *a[], int _n)
{
  char buffer[MAX_STRING_LEN + 1];//the array to store each word
  int count = 0;
  // scanf("20s") means that it'll read at most 20 characaters which is the maximum len on string
  // since buffer is a character array scanfing or strcpying buffer is eqvt to &buffer[0]
  while (count < _n && scanf("%20s", buffer) == 1 && strcmp(buffer, "finish")) {
    a[count] = (char*)malloc(strlen(buffer) + 1);
    strcpy(a[count++], buffer);
  }
  return count;
}

void sort_strings(char *a[], int _n) 
{
  for (int i = 0; i < _n - 1; i++) 
  {
    for (int j = i + 1; j < _n; j++) 
    {
      if (strcmp(a[i], a[j]) > 0) 
      {
        char *temp = a[i];
        a[i] = a[j];
        a[j] = temp;
      }
    }
  }
}

int main() 
{
  char *strings[MAX_IN_LINE];
  int count = read_strings(strings, MAX_IN_LINE );
  printf("\n");

  for (int i = 0; i < count; i++) 
    printf("%s\n", strings[i]);
  
  printf("\n");

  sort_strings(strings, count);
  for (int i = 0; i < count; i++) 
    printf("%s\n", strings[i]);

  return 0;
}


/*
SAMPLE SESSION:
Jack and Jill    went up    the    hill.   finish // This is the input (it will have the "finish" word at the end. 
Jack       // This is the print of the input
and
Jill
went
up
the
hill.
          // This is the extra line
Jack      // This is printing the strings but after sorting.
Jill
and
hill.
the
up
went
*/