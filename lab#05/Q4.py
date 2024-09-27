loan = 5000
insurance = 500
gas = 15000
oil = 2000
tyres = 800
maintenance = 4500

# Calculate the monthly expence using function
def monthly_expence(loan , insurance , gas , oil , tyres , maintenance):
    monthly_cost = loan + insurance + gas + oil + tyres + maintenance
    print(f"Monthly cost is : {monthly_cost}")
    return monthly_cost #returning the monthly cost where the function call
    
monthly_cost = monthly_expence(loan , insurance , gas , oil , tyres , maintenance) #function call

#Calculate the yearly expence using function
def yearly_expence(monthly_cost):
    yearly_cost = monthly_cost * 12
    return yearly_cost #returning yearly function where the function call

yearly_cost = yearly_expence(monthly_cost) #calling yearly expence function
print(f"yearly cost is : {yearly_cost}")

