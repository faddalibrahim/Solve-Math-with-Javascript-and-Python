#LeastcommonMultiple.py: Calculates the LCM of two numbers

def main():
    number1, number2 = LCM()   #Structure of integrated functions
    method(number1, number2)


def LCM():
    message = "Enter number: "
    number1 = int(input(message))
    number2 = int(input(message))       #Takes two numbers 
    return number1, number2

def method(number1, number2):
    counter = 1
    nO1_intersection = []     
    nO2_intersection = []
    
    while number1 != number2:
        nO1_intersection.append(number1 * counter)  #stores values and check familiarity later on
        nO2_intersection.append(number2 * counter)
        counter += 1
        
        if nO1_intersection[-1] in nO2_intersection:
            print("The LCM of", number1,"and", number2,"is", nO1_intersection[-1])   # Multiples for number 1 is comapred to those of number 2
            return nO1_intersection[-1]  #The LCM Value
        elif nO2_intersection[-1] in nO1_intersection:
            print("The LCM of", number1,"and", number2,"is", nO2_intersection[-1])  # Multiples for number 2 is comapred with those of number 1
            return nO2_intersection[-1]  #The LCM value
        
    
    
if __name__ == '__main__':main()
