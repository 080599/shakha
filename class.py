#class Comment:
 #   def __init__(self,username, text, likes=0):
  #      self.username=username
   #     self.text=text
    #    self.likes=likes
class Car:
     def __init__(self, model, color, year):
         self.model=model
         self.color=color
         self.year=year
     def stop(self):
        print('mashina ostanonilas')
     def changecolor(self,newcolor):
        self.color=newcolor
gentra=Car('ravon','Black',2022)
gentra.changecolor('White')
gentra.color()

