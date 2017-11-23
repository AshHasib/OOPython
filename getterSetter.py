

class Student:
    def __init__(self):
        self.name=None
        self.id=None
        self.gpa=None
    def setName(self, name):
        self.name=name
    def setId(self, id):
        self.id=id
    def setGpa(self, gpa):
        self.gpa=gpa
    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getGpa(self):
        return self.gpa
        
st=Student()
st.setName('Hasib')
st.setId(54)
st.setGpa(2.00)

print('Name :',  st.getName())
print('ID:', st.getId())
print('GPA:', st.getGpa())
        
        
        
        
        
        
        
        
        
        
        
        
