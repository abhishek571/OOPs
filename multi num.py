class ABC:
    def abhi(self,a,b,c=None):
        if c is not None:
            return a * b * c 
        else:
            return a + b  
    
y=ABC()
result=y.abhi(1,2,3)
result2=y.abhi(1,2)

print(result)
print(result2)

