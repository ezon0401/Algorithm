/*
BOJ 25918 - Polar bear tears parenthesis  (https://www.acmicpc.net/problem/25918)

You can put 'O' or 'X' as much as you want at night.
Then, a polar bear will convert 'O' to '()' and 'X' to ')(' during the day.
Determine the minimum number of days required to construct the given string S.
*/

#include <iostream>
#include <stack>
#include <string>
#define endl '\n'

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    // 1. TO GET THE INPUT
    
    int length;
    cin >> length;
    string parenthesis_string;
    cin >> parenthesis_string;
    
    
    // 2. TO SOLVE THE PROBLEM
    // The minimum number of days needed is equal to the maximum size of the stack.
    
    int ans = 0;
    stack<int> check;
    
    for (int index = 0; index < parenthesis_string.size(); index++) {
        char now_char = parenthesis_string[index];
        if (check.size() == 0) {
            check.push(now_char);
            ans = max(ans, (int) check.size());
        } else {
            if ((check.top() == '(' && now_char == ')') || (check.top() == ')' && now_char == '(')) {
                check.pop();
            } else {
                check.push(now_char);
                ans = max(ans, (int) check.size());
            }
        }
    }
    
    if (!check.empty()) {
        ans = -1;
    }
    cout << ans << endl;
    
    return 0;

}