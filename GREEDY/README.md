# Greedy

As the name suggests, the greedy algorithm greedily chooses a seemingly optimal option as much as possible. 

For example, consider paying 57 cents with only 10-cent, 5-cent, and 1-cent coins. Then, the minimum number of coins needed is 8: 10 X 5 + 5 X 1 + 1 X 2. You greedily choose coins of high value as much as possible. The approach is optimal because it is guaranteed that one 10-cent coin can be replaced with two 5-cent coins, and one 5-cent coin can be replaced with five 1-cent coins. The greedy approach may not provide an optimal solution otherwise. 

*Application*

* The meeting room scheduling problem is a well-known greedy algorithm problem. If you greedily choose a meeting that ends first, it will maximize the number of meetings. 

*Tip*

* It is important not to blindly use the greedy approach. Always prove why the greedy approach can lead to the optimal solution.