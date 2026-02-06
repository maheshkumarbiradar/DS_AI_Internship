def calc_rectangle(length, width):
    area = length * width
    perimeter = 2*(length+width)
    return area, perimeter
print(f"Area and Perimeter of Rectangle:",calc_rectangle(5,3))
