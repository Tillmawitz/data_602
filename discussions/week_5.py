import math
from string import Template

class Reverser:

    def __init__(self, sentence) -> None:
        self.sentence = sentence

    def reverse_sentence(self):
        temp = self.sentence.split()
        temp.reverse()
        return ' '.join(temp)
    
class Circle:

    def __init__(self, rad):
        self.radius = rad

    def area(self):
        return math.pi * pow(self.radius, 2)
    
    def perimeter(self):
        return 2 * math.pi * self.radius

    
def main():
    test_string_1 = "hello .py"
    test_string_2 = "Sphinx of black quartz hear my vow"

    reverser_1 = Reverser(test_string_1)
    reverser_2 = Reverser(test_string_2)

    print(reverser_1.reverse_sentence())
    print(reverser_2.reverse_sentence())

    small_circle = Circle(2)
    big_circle = Circle(20)

    template = Template("A circle with radius $radius has an area of $area and perimeter $perim.")

    print(template.substitute(radius = small_circle.radius, area = small_circle.area(), perim = small_circle.perimeter()))
    print(template.substitute(radius = big_circle.radius, area = big_circle.area(), perim = big_circle.perimeter()))

if __name__=="__main__":
    main()