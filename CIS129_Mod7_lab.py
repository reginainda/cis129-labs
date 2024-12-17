# ticket prices and seat sec = section
price_A = 20
price_B = 15
price_C = 10

sec_A = 300
sec_B = 500
sec_C = 200

def get_tickets_bought(sec, available_seats):
        """Ask the user for the number of tickets being bought in a section and validate the input"""
        while True:
                try:
                      tickets_bought = int(input(f"Input the number of tickets sold in section {sec} (0-{available_seats}): "))
                      if 0 <= tickets_bought <= available_seats:
                        return tickets_bought
                      else:
                            print(f'Purchase cannot be made. Please enter a number between 0 and {available_seats}. ')
                except ValueError:
                      print('Input is invalid. Enter an integer.')

def main():
       # number of tickets bought in each section
    tickets_bought_sec_A = get_tickets_bought('A', sec_A)
    tickets_bought_sec_B = get_tickets_bought('B', sec_B)
    tickets_bought_sec_C = get_tickets_bought('C', sec_C)

    # calculate income
    income_A = tickets_bought_sec_A * price_A
    income_B = tickets_bought_sec_B * price_B
    income_C = tickets_bought_sec_C * price_C
    total_income = income_A + income_B + income_C

    print(f'Money made from section A: ${income_A} ')
    print(f'Money made from section B: ${income_B} ')
    print(f'Money made from section C: ${income_C} ')

if __name__ == '__main__':
    main()



