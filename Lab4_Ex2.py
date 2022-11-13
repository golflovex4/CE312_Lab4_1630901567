class Pyramid():
    Base_Length = ""
    Base_Width = ""
    Pyramid_Height = ""
    
    def calculate(self):
        self.Measure = (self.Base_Length.Length*self.Base_Width.Width*self.Pyramid_Height.Height)/3
        return self.Measure 

class Length():
    Length = ""
    
class Width():
    Width = ""
    
class Height():
    Height = ""

Pyramid_1 = Pyramid()

PyramidLength = Length()
PyramidWidth = Width()
PyramidHeight = Height()

PyramidLength.Length = 10
PyramidWidth.Width = 7
PyramidHeight.Height = 17

Pyramid_1.Base_Length = PyramidLength
Pyramid_1.Base_Width = PyramidWidth
Pyramid_1.Pyramid_Height = PyramidHeight


print("Pyramid Volume is = " +str(Pyramid_1.calculate()))
