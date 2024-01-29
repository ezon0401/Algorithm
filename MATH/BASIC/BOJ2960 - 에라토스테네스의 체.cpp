/*
BOJ 2960 - Sieve of Eratosthenes (https://www.acmicpc.net/problem/2960)

Print the K-th deleted number when executing the sieve of Eratosthenes on N.
*/

#include <iostream>

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);


    // 1. TO GET THE INPUT

    int num_count, target;
    cin >> num_count >> target;
    

    // 2. SIEVE OF ERATOSTHENES 

    bool prime[num_count+1];
    for (int index = 2; index <= num_count; index++) {
        prime[index] = true;
    }
    
    int count = 1;
    
    for (int num = 2; num <= num_count; num++) {
        if (prime[num] == true) {
            for (int multiple = num; multiple <= num_count; multiple += num) {
                if (prime[multiple] == true) {
                    prime[multiple] = false;
                    if (count == target) {
                        cout << multiple << "\n";
                        return 0;
                    }
                    count++;
                }
            }   
        }
    }

}