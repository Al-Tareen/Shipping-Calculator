#This program will calculate the shipping charges, based on weight of a package inputted by a user

print("""Hello user,

The Fast Freight Shipping Company charges the following rates:

Weight of Package                          Rate per Pound
---------------------------------------------------------
2 pounds or less                                 $1.50
Over  2 pounds but no more than 6 pounds         $3.00
Over 6 pounds but no more than 10 pounds         $4.00
Over 10 pounds                                   $4.75

""")

def shippingProgram():
    poundShipped = ''

    rateLessTwo = 1.50
    rateOverTwo = 3.00
    rateOverSix = 4.00
    rateOverTen = 4.75

    calculateAgain = 'MAGICKEY'

    while isinstance(poundShipped, float) == False or poundShipped <= 0:
        try:
            poundShipped = float(input('Please enter the weight of your package. (in pound/lb) \n'))

            while poundShipped <= 0:
                print('Sorry, number must be positive.')
                poundShipped = float(input('Please enter the weight of your package. (in pound/lb) \n'))

            if poundShipped > 0 and poundShipped < 2:
                totalShipCost = poundShipped * rateLessTwo
                totalShipCost = '%.2f' % totalShipCost
                print('Your total shipping cost for a package with a weight of: ' + str(poundShipped) + ' is: $' + str(totalShipCost))
                calculateAgain = input('\nWould you like to calculate shipping for another package? Type: yes/no \n').lower()

            if poundShipped > 2 and poundShipped < 6:
                totalShipCost = poundShipped * rateOverTwo
                totalShipCost = '%.2f' % totalShipCost
                print('Your total shipping cost for a package with a weight of: ' + str(poundShipped) + ' is: $' + str(totalShipCost))
                calculateAgain = input('\nWould you like to calculate shipping for another package? Type: yes/no \n').lower()
                
            if poundShipped > 6 and poundShipped < 10:
                totalShipCost = poundShipped * rateOverSix
                totalShipCost = '%.2f' % totalShipCost
                print('Your total shipping cost for a package with a weight of: ' + str(poundShipped) + ' is: $' + str(totalShipCost))
                calculateAgain = input('\nWould you like to calculate shipping for another package? Type: yes/no \n').lower()
                
            if poundShipped > 10:
                totalShipCost = poundShipped * rateOverTen
                totalShipCost = '%.2f' % totalShipCost
                print('Your total shipping cost for a package with a weight of: ' + str(poundShipped) + ' is: $' + str(totalShipCost))
                calculateAgain = input('\nWould you like to calculate shipping for another package? Type: yes/no \n').lower()

            while calculateAgain != 'yes' and calculateAgain != 'no' and calculateAgain != 'MAGICKEY':
                print('We\'re sorry, but we don\'t recognize your input. Please enter a \'yes\' or \'no\'')
                calculateAgain = input('\nWould you like to calculate shipping for another package? Type: yes/no \n').lower()
            
            if calculateAgain == 'yes':
                shippingProgram()

            if calculateAgain == 'no':
                print('Thank you for choosing Fast Freight Shipping. See you next time!')
                break
                exit()
    
        except ValueError:
            print('Please enter a number.')

shippingProgram()
