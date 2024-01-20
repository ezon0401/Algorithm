# Geometry

This repository contains algorithms related to geometry.

## CCW

CCW is the foundational algorithm to solve geometry problems. By vector product, the algorithm determines the location of a point in relation to a segment.

<p align="center">
    <img
        src = ".\img\CCW.png"
        width = "360"
        height = "190"
    />
</p>

*Application*

* The area of a triangle is half of its vector product.
* Two segments intersect when, for each segment, the CCW direction of two points on the other segment are different.
* The points in a polygon have the same CCW direction for all segments. 

*Tip*

1. Be mindful of the order of points. 

*Sample Code*

```python
def ccw(x1, y1, x2, y2, x3, y3):
    
    ccw_value = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3

    if ccw_value > 0:
        return "counter-clockwise"
    elif ccw_value < 0:
        return "clockwise"
    else:
        return "straight"
```

## Convex Hull

Given a simple polygon, its convex hull is a convex polygon that includes all the coordinates. 

There are two well-known algorithms to get a convex hull. Graham scan uses sorting by angles, while Monotone Chain gets the upper hull and lower hull to combine them. 

*Application*

* The rotating calipers algorithm gets the closest two points on a 2D plane. The idea is to start from the leftmost point from the upper hull and the rightmost point from the lower hull and rotate the point with a steeper slope.

*Sample Code*
```Python
# Graham Scan

points.sort()

def slope(point1, point2):

    x1, y1 = point1
    x2, y2 = point2

    if x1 == x2:
        return float('inf')
    else:
        return (y1 - y2) / (x1 - x2)

start = points.pop()
convex_hull = [start]

points.sort(key = lambda x : (slope(start, x), x[0], x[1]))

for point in points:
    while len(convex_hull) > 1 and ccw(convex_hull[-2], convex_hull[-1], point) <= 0:
        convex_hull.pop()
    convex_hull.append(point)

# Monotone Chain

points.sort()

upper_hull = []
for point in points:
    while len(upper_hull) > 1 and ccw(upper_hull[-2], upper_hull[-1], point) >= 0:
        upper_hull.pop()
    upper_hull.append(point)

lower_hull = []
for point in points:
    while len(lower_hull) > 1 and ccw(lower_hull[-2], lower_hull[-1], point) <= 0:
        lower_hull.pop()
    lower_hull.append(point)

convex_hull = upper_hull + lower_hull[-2:0:-1]
```