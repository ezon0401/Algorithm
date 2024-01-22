/*
BOJ 28279 - Deque 2 (https://www.acmicpc.net/problem/28279)

Implement an integer deque that takes the following orders:

1 X: To enqueue integer X into the deque
2 X: To push integer X into the deque 
3: To dequeue the deque and print the deleted element
4: To pop the deque and print the deleted element
5: To print the size of the deque
6: To determine whether the deque is empty
7: To print the first element of the deque
8: To print the last element of the deque
*/

#include <iostream>
#include <deque>
#define endl '\n'

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    // 1. TO GET THE INPUT
    
    int order_count;
    cin >> order_count;
    
    deque<int> deque;


    // 2. TO IMPLEMENT ORDERS
    
    for (int order = 0; order < order_count; order++) {
        
        int order_type;
        cin >> order_type;
        
        if (order_type == 1) {
            
            int num;
            cin >> num;
            deque.push_front(num);
            
        } else if (order_type == 2) {
            
            int num;
            cin >> num;
            deque.push_back(num);
            
        } else if (order_type == 3) {
            
            if (deque.empty()) {
                cout << -1 << endl;
            } else {
                cout << deque.front() << endl;
                deque.pop_front();
            }
            
        } else if (order_type == 4) {
            
            if (deque.empty()) {
                cout << -1 << endl;
            } else {
                cout << deque.back() << endl;
                deque.pop_back();
            }
            
        } else if (order_type == 5) {
            
            cout << deque.size() << endl;
            
        } else if (order_type == 6) {
            
            if (deque.empty()) {
                cout << 1 << endl;
            } else {
                cout << 0 << endl;
            }
            
        } else if (order_type == 7) {
            
            if (deque.empty()) {
                cout << -1 << endl;
            } else {
                cout << deque.front() << endl;    
            }
            
        } else {
            
            if (deque.empty()) {
                cout << -1 << endl;
            } else {
                cout << deque.back() << endl;
            }
            
        }

    }

    return 0;

}