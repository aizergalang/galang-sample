salary= int(input("enter salary"))

if (salary>=30000):
    print('You are elligible to for a loan')
    loan= int(input('enter the amount of loan you want to request'))
    loan_amount= salary* 10
    if(loan<=loan_amount):
        print ('You are elligible for a loan')
        months= int(input('how many months you want to pay?')) 
        interest= loan* .10
        new_loan_amount= loan + interest
        payable_amount_monthly= new_loan_amount / months
        print("your total loan to be payed is", new_loan_amount)
        payable_amount_monthly= new_loan_amount / months
        print('payable loan to be payed monthly for',months ,'months is', round(payable_amount_monthly))
    else: print ('sorry, you are not elligible for a loan, your requested loan is too high')
else: 
    print('Sorry, you are not elligable for a loan for. your salary is too low.')
