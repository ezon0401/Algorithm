/*
BOJ 28066 - Thanos hates Josephus (https://www.acmicpc.net/problem/28066)

There are N people. Thanos removes people as the following until only one person is left.

- If there are fewer than K people, all except the first person are removed.
- Otherwise, the first K people except the first person are removed.

Print the number of only person left.
*/


#include <iostream>
#include <deque>
#define endl '\n'

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    // 1. TO GET THE INPUT

    int squirrel_count, delete_num;
    cin >> squirrel_count >> delete_num;


    // 2. TO SOLVE THE PROBLEM
    
    deque<int> state;
    for (int num = 1; num <= squirrel_count; num++) {
        state.push_back(num);
    }

    while (true) {
        if (state.size() >= delete_num) {
            for (int rotate_count = 1; rotate_count <= delete_num; rotate_count++) {
                int deleted = state.front();
                state.pop_front();
                if (rotate_count == 1) {
                    state.push_back(deleted);
                }
            }
        } else {
            cout << state.front() << endl;
            break;
        }
    }

    return 0;

}