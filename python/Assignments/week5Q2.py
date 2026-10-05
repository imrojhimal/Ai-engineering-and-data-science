class Book:
    title="Homomorphology"
    author="Imroj Ahasan Himal"
    def __init__(self):
         self.reviews=[]
    def addReviews(self,new):
        self.reviews.append(new)
        self.count=len(self.reviews)
    def counter(self):
        print(self.count)
    def allreview(self):
        for i in self.reviews:
            print(i)
b=Book()
b.addReviews("its nice")
b.addReviews("its sexy")
b.counter()
b.allreview()