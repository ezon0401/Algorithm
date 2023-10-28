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

* Be mindful of the order of points. 

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