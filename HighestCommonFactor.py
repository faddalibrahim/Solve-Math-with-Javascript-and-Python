import math

def main():
    number1, number2 = inputing()
    number1_multiples = CM(number1)      #The structure of how these functions will be implemented
    number2_multiples = CM(number2)
    HCF(number1_multiples, number2_multiples)
    

def inputing():
    number1 = int(input("Enter the number: "))          
    number2 = int(input("Enter the other number: "))
    return number1, number2

def CM(number):
    multiples = []
    max_divisor = math.sqrt(number)                        #The factors of a number can be achieved at values below the sqrt of the number
    for multiple in range(1, math.floor(max_divisor) + 1):  #It is better to loop through the sqrt than actual number to save time
        if number%multiple == 0:                        #number must be a factor
            counterpart_multiple = number//multiple
            multiples.append(multiple)
            multiples.append(counterpart_multiple)
    multiples.sort()
    print(multiples)
    return multiples

def HCF(number1,number2):    #Use to find the common multiple between the two values
    HCF = []
    for value in number1:
        if value in number2:
            HCF.append(value)
    print("The HCF of", number1[-1],"and",number2[-1],"is", HCF[-1])
    return HCF

if __name__ == '__main__':main()
