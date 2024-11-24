import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='VOTING_SYSTEM'
        )
        if connection.is_connected():
            print("Connected to MySQL database.")
            return connection
    except Error as e:
        print(f"Error: {e}")
    return None

def format_cnic(cnic):
    """Format CNIC with hyphens to ensure it is 15 characters long."""
    if len(cnic) == 13 and cnic.isdigit():
        return f"{cnic[:5]}-{cnic[5:12]}-{cnic[12]}"
    return None

def is_valid_cnic(cnic):
    """Check if the CNIC is valid (13 digits and numeric)."""
    return len(cnic) == 13 and cnic.isdigit()

def register_user(connection, username, cnic):
    """Register a new user in the USERS table and return the user ID."""
    cursor = connection.cursor()
    try:
        # Format CNIC and validate
        formatted_cnic = format_cnic(cnic)
        if not is_valid_cnic(cnic):
            print("CNIC must be 13 digits long. Please enter a valid CNIC.")
            return None
        
        # Check for duplicate CNIC
        cursor.execute('SELECT USER_ID FROM USERS WHERE CNIC = %s', (formatted_cnic,))
        if cursor.fetchone() is not None:
            print(f"Duplicate CNIC found for {username}. This user will not be registered.")
            return None
        
        # Insert new user if CNIC is unique
        cursor.execute('''
            INSERT INTO USERS (USER_NAME, CNIC)
            VALUES (%s, %s)
        ''', (username, formatted_cnic))
        connection.commit()
        
        # Fetch the last inserted user ID
        cursor.execute('SELECT USER_ID FROM USERS WHERE CNIC = %s', (formatted_cnic,))
        user_id = cursor.fetchone()[0]
        print(f"User {username} registered successfully with User ID: {user_id}.")
        return user_id
    except Error as e:
        print(f"Error: {e}")
        return None

def display_candidates(connection):
    """Display all candidates in the CANDIDATE table without showing their votes."""
    cursor = connection.cursor()
    cursor.execute('SELECT CANDIDATE_ID, NAME, PARTY_NAME FROM CANDIDATE')
    candidates = cursor.fetchall()
    print("Candidates:")
    for candidate in candidates:
        print(f"{candidate[0]}: {candidate[1]} (Party: {candidate[2]})")

def is_valid_candidate(connection, candidate_id):
    """Check if the candidate ID is valid."""
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM CANDIDATE WHERE CANDIDATE_ID = %s', (candidate_id,))
    return cursor.fetchone()[0] > 0

def cast_vote(connection, user_id):
    """Cast a vote for a candidate and store the timestamp of the vote."""
    cursor = connection.cursor()
    cursor.execute('SELECT HAS_VOTED FROM USERS WHERE USER_ID = %s', (user_id,))
    has_voted = cursor.fetchone()

    if has_voted and has_voted[0]:
        print("You have already voted.")
        return

    while True:
        candidate_id = int(input("Enter the candidate ID you want to vote for: "))
        
        # Check if the candidate ID is valid
        if not is_valid_candidate(connection, candidate_id):
            print(f"Candidate ID {candidate_id} is invalid. Please select a valid candidate ID.")
            continue  # Prompt for candidate ID again

        try:
            # Insert the vote
            cursor.execute('''
                INSERT INTO VOTES (USER_ID, CANDIDATE_ID)
                VALUES (%s, %s)
            ''', (user_id, candidate_id))
            
            # Update the user's voting status
            cursor.execute('''
                UPDATE USERS SET HAS_VOTED = TRUE WHERE USER_ID = %s
            ''', (user_id,))
            
            # Update the candidate's vote count
            cursor.execute('''
                UPDATE CANDIDATE SET VOTES = VOTES + 1 WHERE CANDIDATE_ID = %s
            ''', (candidate_id,))
            
            connection.commit()
            print("Vote cast successfully.")
            break  # Exit the loop after a successful vote
        except Error as e:
            print(f"Error: {e}")

def print_results(connection):
    """Print voting results."""
    cursor = connection.cursor()
    cursor.execute('''
        SELECT NAME, VOTES FROM CANDIDATE
    ''')
    results = cursor.fetchall()
    print("Voting Results:")
    for result in results:
        print(f"{result[0]}: {result[1]} votes")

def main():
    connection = create_connection()
    
    if connection:
        # Register the first user
        username = input("Enter your username: ")
        
        while True:
            cnic = input("Enter your CNIC (13 digits): ")
            if is_valid_cnic(cnic):
                break
            print("Invalid CNIC. It must be 13 digits long. Please try again.")
        
        user_id = register_user(connection, username, cnic)

        if user_id is not None:
            # Display candidates
            display_candidates(connection)

            # First user casts their vote
            cast_vote(connection, user_id)

        # Loop to add more users
        while True:
            add_another = input("Do you want to add another user? (y/n): ").strip().lower()
            if add_another not in ['y', 'yes']:
                break
            
            # Register another user
            username = input("Enter the new user's username: ")
            
            while True:
                cnic = input("Enter the new user's CNIC (13 digits): ")
                if is_valid_cnic(cnic):
                    break
                print("Invalid CNIC. It must be 13 digits long. Please try again.")
                
            user_id = register_user(connection, username, cnic)

            # If user registration was successful, allow them to vote
            if user_id is not None:
                # Display candidates again for the new user
                display_candidates(connection)

                # New user casts their vote
                cast_vote(connection, user_id)

        # Ask if the user wants to see the results
        view_results = input("Do you want to see the voting results? (y/n): ").strip().lower()
        if view_results in ['y', 'yes']:
            print_results(connection)

        # Close the connection
        connection.close()

if __name__ == "__main__":
    main()