def menu(prompt, choices):
    print '\n\n{0}\n'.format(prompt)
    count = len(choices)
    for i in range(count):
        print '({0}) {1}'.format(i + 1, choices[i])
    response = 0
    while response < 1 or response > count:
        response = raw_input('    Type a number (1-{0}): '.format(count))
        if response.isdigit():
            response = int(response)
        else:
            response = 0
    return response

def buy(stockamount, bondamount):
    response = menu('What to buy?', ['Stocks', 'Bonds', 'Nevermind'])
    # Do something

def sell(stockamount, bondamount):
    response = menu('What to sell?', ['Stocks', 'Bonds', 'Nevermind'])
    # Do something

# ======================================================================
# Main program starts here
# ======================================================================
stockamount=10000
bondamount=10000

main_menu_response = 0
while main_menu_response != 3:
    main_menu_response = menu('What to do?', ['Buy', 'Sell', 'End'])
    if main_menu_response == 1:
        buy(stockamount, bondamount)
    elif main_menu_response == 2:
        sell(stockamount, bondamount)