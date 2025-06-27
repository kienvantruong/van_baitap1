# Định nghĩa class
class Dog:
    def __init__(self, name, age, loaicho):  # Hàm khởi tạo
        self.beo = name  # Thuộc tính (attribute)
        self.age = age
        self.giongcho = loaicho

    def bark(self):  # Phương thức (method)
        print(f"{self.beo} says: Woof!")
class Xe:
    def __init__(self, ten_xe, mau_xe, toc_do):
        self.ten_xe = ten_xe
        self.mau_xe = mau_xe
        self.toc_do = toc_do
    
    def run(self):
        print(f"{self.ten_xe} có 6 chỗ ngồi")
    
# Tạo object
dog1 = Dog("Buddy", 3, "congi") 
dog2 = Dog("Max", 5, "bull")
kiki = Dog("ki ki", 4, "alaska")

xe1 = Xe("")



# Truy cập thuộc tính và phương thức
print(dog1.beo, dog1.age)  # Buddy 3
dog1.bark()  # Buddy says: Woof!
dog2.bark()  # Max says: Woof!
kiki.bark()