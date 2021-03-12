def main():

    quarter = .25
    dime = .10
    nickel = .5
    penny = .1
    cost = float("How much did the item cost?: ")
    paid = float("Enter how much money given: ")
    change = cost - paid
    
    qch= change % quarter
    qtotal = moneyback - qch * quarter 
    dch = qtotal / dime
    dtotal = qtotal - dch * dime
    nch = dtotal / nickel
    ntotal = dtotal - nch * nickel
    pch = ntotal / penny
    ptotal = ntotal - pch * penny

  
    print("You need %s quarters, %s dimes, %s nickels, %s pennies." % (qch, dch, nch, pch))

if __name__ == "__main__":
    main()