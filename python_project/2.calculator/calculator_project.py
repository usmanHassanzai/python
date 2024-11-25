import mysql.connector

while True:
    # Getting user input for values a and b
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    
    
    try:
        # Establishing the connection to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="CALCULATOR"
        )
        
        if connection.is_connected():
            print("CONNECTED TO MYSQL DATABASE")
            option = input("Which operation you want to perform (+,-,/,*) : ")
            
            
            if(option == '+'):
                result = a + b
                cursor = connection.cursor()
                query = "INSERT INTO ADDITION (A, B, RESULT) VALUES (%s, %s, %s)"
                cursor.execute(query, (a, b, result))  # Pass values as a tuple
            elif(option == '-'):
                result = a - b
                cursor = connection.cursor()
                query = "INSERT INTO SUBTRACTION (A , B , RESULT) VALUES (%s, %s, %s)"
                cursor.execute(query , (a , b , result))
            elif(option == '/'):
                result = a / b
                cursor = connection.cursor()
                query = "INSERT INTO DIVISION (A , B , RESULT) VALUES (%s, %s, %s)"
                cursor.execute(query, (a,b,result))
            elif(option == '*'):
                result = a * b
                cursor = connection.cursor()
                query = "INSERT INTO MULTIPLICATION (A , B , RESULT) VALUES (%s, %s, %s)"
                cursor.execute(query , (a,b,result))
            else:
                print("Invalid option please select a correct option")
            connection.commit()  # Commit the changes
            print("Data inserted successfully")
    
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():            
            cursor.close()  # Close the cursor
            connection.close()  # Close the connection
            print("MySQL connection is closed")
    
    # Ask the user if they want to continue or exit
    continue_input = input("Do you want to continue? (yes/no): ").strip().lower()
    if continue_input not in ['y' , 'yes' , 'Y' , 'YES'] :
        print("Exiting the program.")
        break