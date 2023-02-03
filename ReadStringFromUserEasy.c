#include <stdio.h>

int main() {
    char buffer[100];

    printf("Enter a string: ");
    fgets(buffer, sizeof(buffer), stdin);

    printf("The input string is: %s", buffer);
    return 0;
}