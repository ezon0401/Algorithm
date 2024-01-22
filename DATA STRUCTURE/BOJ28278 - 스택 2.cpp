/*
BOJ 28278 - Stack 2 (https://www.acmicpc.net/problem/28278)

Implement an integer stack that takes the following orders:

1 X: To push integer X into the stack
2: To pop the stack and print the deleted element
3: To print the size of the stack
4: To determine whether the stack is empty
5: To print the element at the top
*/

#include <cstdio>
#include <stack>

using namespace std;

int main() {
    
    
    // 1. TO GET THE INPUT

    stack<int> stack;

    int order_count;
    scanf("%d", &order_count);
    

    // 2. TO IMPLEMENT ORDERS

    for (int order; order < order_count; order++) {
        
        int order_type;
        scanf("%d", &order_type);
        
        if (order_type == 1) {
            
            int num;
            scanf("%d", &num);
            stack.push(num);
            
        } else if (order_type == 2) {
            
            if (stack.empty()) {
                printf("%d\n", -1);
            } else {
                printf("%d\n", stack.top());
                stack.pop();
            }
            
        } else if (order_type == 3) {
            
            printf("%d\n", stack.size());
        
        } else if (order_type == 4) {
            
            if (stack.empty()) {
                printf("%d\n", 1);
            } else {
                printf("%d\n", 0);
            }
            
        } else {
            
            if (stack.empty()) {
                printf("%d\n", -1);
            } else {
                printf("%d\n", stack.top());    
            }
            
        }
    }
    
    return 0;
    
}