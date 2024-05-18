#include <stdio.h>
#include <stdlib.h>



int main(int argc, char *argv[]) {
    char *a  = argv[1];
    int num  = atoi(a);
    if (num>5 && num < 10){
        if(num==6){
            printf("it is 6");
        }
        printf("%d",num);
        printf("Number is greater than 5");

    }
    if(num<=4){
        printf("%d",num);
        printf("Hello");
    }
    
}


