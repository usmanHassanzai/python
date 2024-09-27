
number_of_pages = int(input("Enter the number of pages : "))

def international_fax(number_of_pages) :
    service_charge = 3.00
    cost_per_page = 0.20 #for first 10 pages rate per page
    cost_additional_page = 0.10 #for each additional page after 10 pages charge
    
    if(number_of_pages <= 10) :
        cost_of_international_fax = (number_of_pages * cost_per_page) + service_charge
        return cost_of_international_fax
    elif(number_of_pages > 10) :
        
        cost_of_international_fax = (10 * cost_per_page) + ((number_of_pages - 10) * cost_additional_page) + service_charge
        return cost_of_international_fax
    
#calling function
total_amount = international_fax(number_of_pages) 
print(f"Total amount of sending international fax : {total_amount}$")
