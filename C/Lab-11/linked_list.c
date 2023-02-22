#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LEN 20

struct student {
  char name[MAX_NAME_LEN + 1];
  int id;
  float marks;
  struct student *next;
};

// Generates a new student struct and returns the pointer to it
struct student *read_new_student() {
  struct student *new_student = (struct student*)malloc(sizeof(struct student));
  //These are best practices to be followed in order to deal with malloc error
  /*  
  if (!new_student) {
    printf("Error: unable to allocate memory for a new student\n");
    exit(1);
  }
  */
  // USE THIS TECHNIQUE 
  scanf("%s %d %f", &new_student->name, &new_student->id, &new_student->marks);
  new_student->next = NULL;

  return new_student;
}

// Upon recieving the pointer to head and the pointer of the struct whose to be inserted,
struct student *insert_student_byid(struct student *head, struct student *new) {
  struct student *head_pointer = head;
  struct student *prev_pointer = NULL;

  while (head_pointer && new->id > head_pointer->id) {
    prev_pointer = head_pointer;
    head_pointer = head_pointer->next;
  }

  if (prev_pointer) {
    prev_pointer->next = new;
  } else {
    head = new;
  }

  new->next = head_pointer;
  return head;
}


// 
struct student *delete_student(struct student *head, int id) {
  struct student *head_pointer = head;
  struct student *prev_pointer = NULL;

  while (head_pointer && head_pointer->id != id) {
    prev_pointer = head_pointer;
    head_pointer = head_pointer->next;
  }

  if (!head_pointer) {
    return head;
  }

  if (prev_pointer) {
    prev_pointer->next = head_pointer->next;
  } else {
    head = head_pointer->next;
  }

  free(head_pointer);
  return head;
}

// Prints the linked list of students line by line STARTING FROM HEAD
void print_student_list(struct student *head) {
  struct student *head_pointer = head;

  // Since head_pointer would be yield NULL otherwise
  while (head_pointer) {
    printf("%s %d %.2f\n", head_pointer->name, head_pointer->id, head_pointer->marks);
    head_pointer = head_pointer->next;
  }
}




int main() {
  int n;
  scanf("%d", &n);

  struct student *head = NULL; // Initialize head to NULL

  for (int i = 0; i < n; i++) {

    // Read data for a new student struct and the function will return a pointer to the struct
    struct student *new_student = read_new_student();  
    // Insert the new student struct at the beginning of the linked list
    // We are passing a pointer to head and pointer to the new struct and it
    head = insert_student_byid(head, new_student); 
  }

  // Print the linked list
  print_student_list(head); 

  int id;
  while (1) {
     // Read the id of the student to be deleted
    scanf("%d", &id);
    // Delete the student with the given id
    head = delete_student(head, id); 
    // Print the updated linked list
    print_student_list(head); 
  }

  return 0;
}




