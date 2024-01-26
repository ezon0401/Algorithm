/*
BOJ 1026 - Treasure (https://www.acmicpc.net/problem/1026)

There are two arrays: A and B.
It is defined that S = A[0] X B[0] + ... + A[N-1] X B[N-1].
If it is possible to rearrange A, print the minimum value of S.
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // 1. TO GET INPUT

    int vec_size;
    cin >> vec_size;
    
    vector<int> vecA, vecB;
    for (int index = 0; index < vec_size; index++) {
        int element;
        cin >> element;
        vecA.push_back(element);
    }
    for (int index = 0; index < vec_size; index++) {
        int element;
        cin >> element;
        vecB.push_back(element);
    }

    // 2. TO SOLVE THE PROBLEM

    sort(vecA.begin(), vecA.end());
    sort(vecB.begin(), vecB.end(), greater<>());
    
    int ans = 0;
    for (int index = 0; index < vec_size; index++) {
        ans += vecA[index] * vecB[index];
    }
    cout << ans;
    
}