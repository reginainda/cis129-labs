class Pet:
     # main module 
    def __init__(self):
        self.__Pet_name = ""
        self.__Pet_type = ""
        self.__Pet_age = 0

    def setPet_name(self, Pet_name):
        self.__Pet_name = Pet_name
    def setPet_type(self, Pet_type):
        self.__Pet_type = Pet_type
    def setPet_age(self, Pet_age):
        self.__Pet_age = Pet_age
    
    def getPet_name(self):
        return self.__Pet_name
    def getPet_type(self):
        return self.__Pet_type
    def getPet_age(self):
        return self.__Pet_age
    
# main 
def main():
   Animal = Pet()
   # Get values for a pet
   inputPet_name = input("Enter a pet name: ")
   Animal.setPet_name(inputPet_name) 
   
   inputPet_type = input("Enter a pet type: ")
   Animal.setPet_type(inputPet_type)

   inputPet_age = input("Enter a pet age: ")
   Animal.setPet_age(inputPet_age)

   # show values for this pet
   print("\nThe pet name is:", Animal.getPet_name())
   print("The pet type is:", Animal.getPet_type())
   print("The pet age is:", Animal.getPet_age())

# run main function
if __name__ == "__main__":
    main()





    
        


     
     

