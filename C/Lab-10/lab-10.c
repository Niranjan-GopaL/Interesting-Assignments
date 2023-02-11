/*
    It seems that Proff told that he'd test only with integers so , the output
    is formatted as int otherwise the output would have been:
    Ram 1729 100.000000
    Maha 2718 90.000000
    Manju 3141 95.000000

*/



#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LENGTH 20
#define MAX_STUDENTS 100


// Since we are having marks field as float 
// It's helpful to know these techniques while trying to print:
/*
        scanf("%0.2f", &students[i].marks);

the 0 represents the minimum width of the output field, and the 
.4 indicates that 4 characters should be displayed after the decimal point 
for floating-point numbers.
*/

struct student {
    char name[MAX_NAME_LENGTH + 1];
    int id;
    float marks;
};

void sort_students_by_id(struct student* students, int _n) {
  for (int i = 0; i < _n - 1; i++) {
    for (int j = 0; j < _n - i - 1; j++) {
      if (students[j].id > students[j + 1].id) {
        // We can create a temporary student structure
        // that will hold all the contents of students[j]
        //REMEMBER THIS TECHNIQUE!! 
        struct student temp = students[j];
        students[j] = students[j + 1];
        students[j + 1] = temp;
      }
    }
  }
}

/*
I changed `struct student* students` from `struct student students[]`
to get the string passed , char array is used  but we now know that:
    `char *file_name` is equivelent to `char file_name[]`
    USE THIS TECHNIQUE TO get the string passed EVRYTIME
*/
void read_students_from_file(char *file_name, struct student* students, int *_n) {
    //fp is a file pointer
    FILE *fp; 
    fp = fopen(file_name, "r");

    /*
    Sometimes fopen() can return an empty file pointer , which causes an error , 
    so we could handle it by below block:-

    if (fp == NULL) {
        printf("Error opening file.\_n");
        exit(1);
    }*/

    /*    
    since first line is number of students, _
    n will store how many times we need to loop over
    _n is made a pointer cuz we need to store the first line (which is the 
    number of students) 
    */
    fscanf(fp, "%d", _n);
    for (int i = 0; i < *_n; i++) {
        fscanf(fp, "%s %d %f", students[i].name, &students[i].id, &students[i].marks);
    }
    fclose(fp);
}

void write_students_to_file(char *file_name, struct student students[], int _n) {
    FILE *fp;
    fp = fopen(file_name, "w");
    //Should write the block to handle empty file
    for (int i = 0; i < _n; i++) {
        fprintf(fp, "%s %d %d\n", students[i].name, students[i].id, (int)(students[i].marks));
    }
    fclose(fp);
}

void main() {
    // declares a array students where each element is a 'struct student' 
    // there are MAX_STUDENTS students in the array
    struct student students[MAX_STUDENTS];
    int n;

    read_students_from_file("input_file.txt", students, &n);
    sort_students_by_id(students, n);
    write_students_to_file("output_file.txt", students, n);

}
