/*
BOJ 11866 - Josephus Problem 0 (https://www.acmicpc.net/problem/11866)

There are N people, and a positive integer K is given.
We will repeatedly remove a K-th person until no one is left.
Print the order of deletion.
*/

#include <iostream>
#include <deque>
#define endl '\n'

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    

    // 1. TO GET THE INPUT

    int people_count, delete_num;
    cin >> people_count >> delete_num;


    // 2. TO SOLVE THE PROBLEM
    
    deque<int> arr;
    for (int num = 1; num <= people_count; num++) {
        arr.push_back(num);
    }
    
    deque<int> ans;
    while (!arr.empty()) {
        for (int rotate_num = 1; rotate_num <= delete_num; rotate_num++) {
            int deleted = arr.front();
            arr.pop_front();
            if (rotate_num != delete_num) {
                arr.push_back(deleted);
            } else {
                ans.push_back(deleted);
            }
        }
    }

    cout << "<";
    while (!ans.empty()) {
        int now_num = ans.front();
        ans.pop_front();
        if (ans.empty()) {
            cout << now_num << ">" << endl;
        } else {
            cout << now_num << ", ";
        }
    }

    return 0;

}