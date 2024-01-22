/*
BOJ 15552 - Fast A+B (https://www.acmicpc.net/problem/15552)

Given A and B, print A + B.
*/

#include <cstdio>

using namespace std;

int main() {

    // 1. TO GET THE INPUT AND SOLVE THE PROBLEM

    int test_count;
    scanf("%d", &test_count);
    
    for (int test = 0; test < test_count; test++) {
        int A, B;
        scanf("%d %d", &A, &B);
        printf("%d\n", A+B);
    }
    
}