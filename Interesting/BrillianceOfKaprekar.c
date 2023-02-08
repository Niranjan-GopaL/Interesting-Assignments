// IMT2022543

#include <stdio.h>
#include <math.h>



// Returns 1 if the k digits of n are all the same, 0 otherwise.
int isRepNum(int n, int k) {
  int first_digit = n / (int)pow(10, k - 1);
  if(n<10){
    return 1;
    }
  else{
    return n%10==first_digit && isRepNum(n/10,k-1);
  }
}


int main() {
  int n;
  while (1) {
    printf("Enter a 3-digit number: ");
    scanf("%d", &n);

    // Check if n is a repnumber.
    if (isRepNum(n, 3)) {
      printf("Exiting program.\n");
      break;
    }

    int b, s, iterations = 0;
    do {
      // Rearrange digits of n to form b and s by using an array
      int digits[3];
      for (int i = 0; i < 3; i++) {
        digits[i] = n / (int)pow(10, 2 - i) % 10;
      }

      // Sort digits
      for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
          if (digits[i] < digits[j]) {
            int temp = digits[i];
            digits[i] = digits[j];
            digits[j] = temp;
          }
        }
      }

      b = digits[0] * 100 + digits[1] * 10 + digits[2];
      s = digits[2] * 100 + digits[1] * 10 + digits[0];
      
      // Compute new value of n
      n = b - s;
      printf("%d - %d = %d\n", b, s, n);
      iterations++;
    } while (n != 495);

    printf("Repeated after %d iterations.\n", iterations);
  }

  return 0;
}
