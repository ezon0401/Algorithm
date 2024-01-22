/*
BOJ 18258 - Queue 2 (https://www.acmicpc.net/problem/18258)

Implement an integer queue that takes the following orders:

push X: To enqueue integer X into the queue
pop: To dequeue the queue and print the deleted element
size: To print the size of the queue
empty: To determine whether the queue is empty
front: To print the first element of the queue
back: To print the last element of the queue
*/

#include <iostream>
#include <queue>
#include <string>
#define endl '\n' 

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    

    // 1. TO GET THE INPUT

    int order_count;
    cin >> order_count; 
    
    queue<int> queue;


    // 2. TO IMPLEMENT ORDERS
    
    for (int order = 0; order < order_count; order++) {
        
        string order_type;
        cin >> order_type;

        if (order_type == "push") {

            int num;
            cin >> num;
            queue.push(num);

        } else if (order_type == "pop") {
            
            if (queue.empty()) {
                cout << -1 << endl;
            } else {
                cout << queue.front() << endl;
                queue.pop();
            }

        } else if (order_type == "size") {

            cout << queue.size() << endl;

        } else if (order_type == "empty") {

            if (queue.empty()) {
                cout << 1 << endl;
            } else {
                cout << 0 << endl;
            }

        } else if (order_type == "front") {
            
            if (queue.empty()) {
                cout << -1 << endl;
            } else {
                cout << queue.front() << endl;
            }

        } else {

            if (queue.empty()) {
                cout << -1 << endl;
            } else {
                cout << queue.back() << endl;
            }

        } 

    }
    
    return 0;

}