#main file created

class Symbol:
    def __init__(self,color: str, icon:str): 
        
        self.color = color
         # it is a string
        self.icon =icon
         # icon is string

    def __str__(self):
    
        return f"{self.icon}, {self.color}"
    
class card(symbol):
    def __init__(self, color: str, icon: str, value: str):
        super().__init__(color: str, icon: str)
        self.value=value
        
     def __str__(self):
        return f"{self.value}{self.icon}"   

   
               
        
        
       

