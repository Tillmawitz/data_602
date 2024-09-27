import math
# Q2: Create a class Box that has attributes length and width that takes values for length
# and width upon construction (instantiation via the constructor).
# In addition, create…
# ● A method called render() that prints out to the screen a box made with asterisks of
# length and width dimensions
# ● A method called invert() that switches length and width with each other
# ● Methods get_area() and get_perimeter() that return appropriate geometric calculations
# ● A method called double() that doubles the size of the box. Hint: Pay attention to return
# value here.
# ● Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if
# their respective lengths and widths are identical.
# ● A method print_dim() that prints to screen the length and width details of the box
# ● A method get_dim() that returns a tuple containing the length and width of the box
# ● A method combine() that takes another box as an argument and increases the length
# and width by the dimensions of the box passed in
# ● A method get_hypot() that finds the length of the diagonal that cuts through the middle
# ● Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1,
# box2 and box3 respectively
# ● Print dimension info for each using print_dim()
# ● Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the
# screen accordingly
# ● Combine box3 into box1 (i.e. box1.combine())
# ● Double the size of box2
# ● Combine box2 into box1

class Box():

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def render(self):
        end_lines = "*" * self.width
        middle_lines = "*" + " " * (self.width - 2) + "*"
        i = 1

        print(end_lines)
        while i < self.length - 1:
            print(middle_lines)
            i += 1
        print(end_lines)

    def invert(self):
        tmp = self.length
        self.length = self.width
        self.width = tmp

    def get_area(self):
        return self.length * self.width
    
    def get_perimeter(self):
        return self.length * 2 + self.width * 2

    def __str__(self) -> str:
        return f"length = {self.length} width = {self.width}"
    
    def double(self):
        self.length = self.length * 2
        self.width = self.width * 2

    # Tuples are evaluated positionally
    def __eq__(self, value) -> bool:
        return (self.get_dim() == value.get_dim())
    
    def print_dim(self):
        print(f"length = {self.length} width = {self.width}")

    def get_dim(self):
        return (self.length, self.width)
    
    def combine(self, other_box):
        self.length += other_box.length
        self.width += other_box.width

    def get_hypot(self) -> double:
        return math.pow((math.pow(self.length, 2) + math.pow(self.width, 2)), 0.5)

def main():
    box1 = Box(5, 10)
    box2 = Box(3, 4)
    box3 = Box(5, 10)

    box1.print_dim()
    box2.print_dim()
    box3.print_dim()

    print(box1 == box2)
    print(box1 == box3)

    box1.combine(box3)
    box2.double()
    box1.combine(box2)

    box1.print_dim()
    print(f"The hypotenuse of box1 is {box1.get_hypot()}")
    box1.render()

if __name__=="__main__":
    main()

