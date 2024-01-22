/*
BOJ 9012 - Parenthesis (https://www.acmicpc.net/problem/9012)

Determine whether a given string is a proper parenthesis string.
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

    int test_count;
    cin >> test_count;
    
    for (int test = 0; test < test_count; test++) {
        
        string parenthesis_string;
        cin >> parenthesis_string;
        

        // 2. TO CHECK THE STRING

        string ans = "YES";
        stack<int> check;
        
        for (int index = 0; index < parenthesis_string.size(); index++) {
            
            char now = parenthesis_string[index];
            if (now == '(') {
                check.push(now);
            } else {
                // If there is a no match for ')', the string is improper.
                if (check.empty()) {
                    ans = "NO";
                } else {
                    check.pop();
                }
            }
            
        }
        
        // If there is an unmatched parenthesis, the string is improper. 
        if (!check.empty()) {
            ans = "NO";
        }
        
        cout << ans << endl;
        
    }

    return 0;

}