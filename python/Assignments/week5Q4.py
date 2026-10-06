class Shape:
    def area(self):
       l=50
       r=5
       area=3.1416*r*r*l
       return area
class circle(Shape):
    def area(self):
        pi=3.1416
        r=4
        area=pi*r*r
        return area
class triangle(Shape):
    def area(self):
        b=10
        h=40
        area=0.5*b*h
        return area
class rectangle(Shape):
   def area(self):
       a=4
       b=5
       area=a*b
       return area
a=circle()
print(a.area())