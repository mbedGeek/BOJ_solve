//BOJ 10828 스택

#include <stdio.h>
#include <string.h>

int main() {
    int stack[10000];
    int N, i, s, top = 0;
    char cmd[30];
    
    scanf("%d", &N);
    
    for(i = 0; i < N; i++) {
        scanf("%s", cmd);
        
        if(strcmp(cmd, "push") == 0) {
            scanf("%d", &s);
            stack[top] = s;
            top++;
        } else if(strcmp(cmd, "pop") == 0) {
            if(top == 0) {
                printf("-1\n");
            } else {
                printf("%d\n", stack[top - 1]);
                top--;
            }
        } else if(strcmp(cmd, "size") == 0) {
            printf("%d\n", top);
        } else if(strcmp(cmd, "empty") == 0) {
            if(top == 0) {
                printf("1\n");
            } else {
                printf("0\n");
            }
        } else if(strcmp(cmd, "top") == 0) {
            if(top == 0) {
                printf("-1\n");
            } else {
                printf("%d\n", stack[top - 1]);
            }
        }
    }
    
    return 0;
}