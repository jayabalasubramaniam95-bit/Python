class SubfieldsInAI():
    def Subfields():
        Lists=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are: ")
        for i in Lists:
          print(i)

class OddEven():
     def OddEven():
      num=int(input("Enter the number: "))
      if(num%2==0):
        Msg= str(num)+" is Even Number"
      else:
        Msg=str(num)+" is Odd Number"
      return Msg

class ElegiblityForMarriage():
    def Elegible():
        gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(gender=='M'):
            if(Age>20):
              Msg= 'ELIGIBLE'
            else:
              Msg= 'NOT ELIGIBLE'
        else:
           if(Age>17):
              Msg= 'ELIGIBLE'
           else:
              Msg= 'NOT ELIGIBLE'
        return Msg

class FindPercent():
     def percentage():
         Sub1=int(input("Subject1: "))
         Sub2=int(input("Subject2: "))
         Sub3=int(input("Subject3: "))
         Sub4=int(input("Subject4: "))
         Sub5=int(input("Subject5: "))
         Total =int(Sub1+Sub3+Sub3+Sub4+Sub5)
         print("Total:", Total)
         perc= (Total/5)
         print("Percentage: ", perc)
         return perc

class triangle():
    def triangle():
       Height=float(input("Height: "))
       Breadth=float(input("Breadth: "))
       AreaTri=float((Height*Breadth)/2)
       print("Area of Triangle: ", AreaTri)
       Height1=float(input("Height1: "))
       Height2=float(input("Height2: "))
       PBreadth=float(input("Breadth: "))
       PTri=float(Height1+Height2+PBreadth)
       print("Perimeter of Triangle: ", PTri)


    