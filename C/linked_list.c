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

struct student *read_new_student() {
  struct student *new_student = (struct student*)malloc(sizeof(struct student));
  if (!new_student) {
    printf("Error: unable to allocate memory for a new student\n");
    exit(1);
  }

  printf("Enter the name of the student: ");
  scanf("%s", new_student->name);

  printf("Enter the ID of the student: ");
  scanf("%d", &new_student->id);

  printf("Enter the marks of the student: ");
  scanf("%f", &new_student->marks);

  new_student->next = NULL;
  return new_student;
}

struct student *insert_student_byid(struct student *head, struct student *new) {
  struct student *cur = head;
  struct student *prev = NULL;

  while (cur && new->id > cur->id) {
    prev = cur;
    cur = cur->next;
  }

  if (prev) {
    prev->next = new;
  } else {
    head = new;
  }

  new->next = cur;
  return head;
}

struct student *delete_student(struct student *head, int id) {
  struct student *cur = head;
  struct student *prev = NULL;

  while (cur && cur->id != id) {
    prev = cur;
    cur = cur->next;
  }

  if (!cur) {
    return head;
  }

  if (prev) {
    prev->next = cur->next;
  } else {
    head = cur->next;
  }

  free(cur);
  return head;
}

void print_student_list(struct student *head) {
  struct student *cur = head;

  while (cur) {
    printf("%s %d %.2f\n", cur->name, cur->id, cur->marks);
    cur = cur->next;
  }
}

int main() {
  int n;
  scanf("%d", &n);

  struct student *head = NULL; // Initialize head to NULL

  for (int i = 0; i < n; i++) {
    struct student *new_student = read_new_student(); // Read data for a new student
    head = insert_student_byid(head, new_student); // Insert the new student in the linked list
  }

  print_student_list(head); // Print the linked list

  int id;
  while (1) {
    scanf("%d", &id); // Read the id of the student to be deleted
    if (id <= 0) {
      break; // Exit if id is 0 or negative
    }
    head = delete_student(head, id); // Delete the student with the given id
    print_student_list(head); // Print the updated linked list
  }

  return 0;
}
// The main function reads the number of students, calls read_new_student to read data for each student and insert them in the linked list using insert_student_byid. After reading all the students, the linked list is printed using print_student_list.

// Then, it enters a loop to repeatedly read the student id for deletion and calls delete_student to delete the student with the given id. After each deletion, it prints the updated linked list. The loop exits when a 0 or negative number is given as the student id.




