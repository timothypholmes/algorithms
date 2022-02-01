#include <stdio.h>

main() {
    int list[] = {1,3,5,7,8};
    int item = 10, k = 3, n = 5;
    int i = 0, j = n;
    printf("The original array elements are :\n");
    for (i = 0; i < n; i++) {
        printf("list[%d] = %d \n", i, list[i]);
    }
}
