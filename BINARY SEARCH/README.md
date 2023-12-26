# Binary Search

When there is a sorted array and a decision problem, a problem that can be answered as either true or false when given an element, the binary search algorithm provides the largest (or smallest) solution that satisfies the decision problem.

Consider we try to choose the largest value below 20 in the array A = [1, 2, 5, 8, 15, 21, 22]. Then the decision problem would be "Is an element below 20?" The answer is true for [1, 2, 5, 8, 15] and false for the others. 

The binary search algorithm repeatedly checks the answer for the value in the middle. In the example, the answer for the middle value 8 is true. Then, we can reduce the array to [8, 15, 21, 22].

Next, consider we chose 15. The answer is still true. Again, we reduce the array to [15, 21, 22].

The value at the middle is 21. Since it is false, we can find that the largest element that satisfies the decision problem is 15.

Since we reduce the size of the array to half at each step, the time complexity is O(log n).

*Tip*

* Python has the module 'bisect' that performs a basic binary search operation. 
* The answer for the decision problem may be unanimously true or false for all elements. 

*Sample Code*

```python
low = 0
high = len(arr) - 1

while low + 1 < high:
    mid = (low + high) // 2
    if arr[mid] <= target:
        low = mid
    if arr[mid] > target:
        high = mid

print(arr[low])
```