def calculate_rectangle_area(x1, y1, x2, y2):
    return abs((x2 - x1) * (y2 - y1))

def calculate_overlap_area(x1, y1, x2, y2, x5, y5, x6, y6):
    # Find overlap coordinates
    left = max(x1, x5)
    right = min(x2, x6)
    bottom = max(y1, y5)
    top = min(y2, y6)
    
    # Check if rectangles overlap
    if left < right and bottom < top:
        return calculate_rectangle_area(left, bottom, right, top)
    return 0 #There is no overlap

# Parse input
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

# Calculate total grass area
grass1_area = calculate_rectangle_area(x1, y1, x2, y2)
grass2_area = calculate_rectangle_area(x3, y3, x4, y4)
total_grass_area = grass1_area + grass2_area

# Calculate overlap with fence
overlap1 = calculate_overlap_area(x1, y1, x2, y2, x5, y5, x6, y6)
overlap2 = calculate_overlap_area(x3, y3, x4, y4, x5, y5, x6, y6)

print(total_grass_area - overlap1 - overlap2)