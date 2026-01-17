class operasbass:
    
    num1=0
    num2=0
    res=0

    def __init__(self):
        self.num1=0
        self.num2=0
    
    def suma(self):
        self.num1=self.a
        self.num2=self.b
        self.res=self.num1+self.num2
        print("la suma de {} mas {} es {}".format(self.num1, self.num2, self.res))
        
    def resta(self):
        self.res=self.num1-self.num2
        print("la resta de {} menos {} es {}".format(self.num1, self.num2, self.res))
        
        
def main():
    obj.operasbass()
    obj.suma()
    
if __name__ == "__main__":
    main()