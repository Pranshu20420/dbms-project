import mysql.connector

# Establishing a connection to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aita1234",
    database="db"
)

# Create a cursor object to execute queries
mycursor = mydb.cursor()

# Add a new record
def add_record():
    # Print the table names
    print('''TABLE NAMES
    CAR
    DRIVER
    OWNER
    POLICY
    CLAIM
    WORKSHOP''')

    # Prompt the user to choose a table to add a new record
    table_name = input("Enter the name of the table to add a new record: ").upper()

    # Prompt the user to enter the field values for the new record
    if table_name == "CAR":
        car_ID = input("Enter the car ID: ")
        chassis_no = input("Enter the chassis number: ")
        engine_no = input("Enter the engine number: ")
        make = input("Enter the make: ")
        model = input("Enter the model: ")
        year = input("Enter the year: ")
        values = (car_ID, chassis_no, engine_no, make, model, year)
        query = "INSERT INTO CAR VALUES (%s, %s, %s, %s, %s, %s)"
    elif table_name == "DRIVER":
        driver_id = input("Enter the driver ID: ")
        name = input("Enter the name: ")
        address = input("Enter the address: ")
        phone = input("Enter the phone number: ")
        values = (driver_id, name, address, phone)
        query = "INSERT INTO DRIVER VALUES (%s, %s, %s, %s)"
    elif table_name == "OWNER":
        owner_id = input("Enter the owner ID: ")
        car_ID = input("Enter the car ID: ")
        name = input("Enter the name: ")
        address = input("Enter the address: ")
        phone = input("Enter the phone number: ")
        values = (owner_id, car_ID, name, address, phone)
        query = "INSERT INTO OWNER VALUES (%s, %s, %s, %s, %s)"
    elif table_name == "POLICY":
        policy_ID = input("Enter the policy ID: ")
        car_ID = input("Enter the car ID: ")
        owner_id = input("Enter the owner ID: ")
        start_date = input("Enter the start date: ")
        end_date = input("Enter the end date: ")
        values = (policy_ID, car_ID, owner_id, start_date, end_date)
        query = "INSERT INTO POLICY VALUES (%s, %s, %s, %s, %s)"
    elif table_name == "CLAIM":
        claim_id = input("Enter the claim ID: ")
        policy_ID = input("Enter the policy ID: ")
        car_ID = input("Enter the car ID: ")
        workshop_id = input("Enter the workshop ID: ")
        driver_id = input("Enter the driver ID: ")
        date = input("Enter the date of incident: ")
        location = input("Enter the location of incident: ")
        severity = input("Enter the severity of incident: ")
        amount = input("Enter the amount of claim: ")
        values = (claim_id, policy_ID, car_ID, workshop_id, driver_id, date, location, severity, amount)
        query = "INSERT INTO CLAIM VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    elif table_name == "WORKSHOP":
        workshop_id = input("Enter the workshop ID: ")
        name = input("Enter the name: ")
        address = input("Enter the address: ")
        phone = input("Enter the phone number: ")
        values = (workshop_id, name, address, phone)
        query = '''INSERT INTO WORKSHOP (workshop_id, name, address, phone_number) VALUES (%s, %s, %s, %s)'''
    else:
        print("Invalid table name")
        return

    # Execute the INSERT query with the values provided by the user
    mycursor.execute(query, values)
    # Commit the changes to the database
    mydb.commit()
    # Print a success message
    print(f"New record added to {table_name}!")

# Update an existing record
def update_record():
    table_names = {
        "CAR": ("car_ID", "chassis_no", "engine_no", "make", "model", "year"),
        "DRIVER": ("driver_ID", "name", "address", "phone"),
        "OWNER": ("owner_ID", "car_ID", "name", "address", "phone"),
        "POLICY": ("policy_ID", "car_ID", "owner_ID", "start_date", "end_date"),
        "CLAIM": ("claim_ID", "policy_ID", "car_ID", "workshop_ID", "driver_ID", "date", "location", "severity", "amount"),
        "WORKSHOP": ("workshop_ID", "name", "address", "phone")
    }

    # Print the table names
    print("TABLE NAMES\n" + "\n".join(table_names.keys()))

    # Prompt the user to choose a table to update a record
    table_name = input("Enter the name of the table to update a record: ").upper()

    if table_name not in table_names:
        print("Invalid table name")
        return

    # Prompt the user to enter the primary key ID of the record to update
    pk_name = table_names[table_name][0]
    pk_value = input(f"Enter the {pk_name} of the record to update: ")

    # Prompt the user to enter the new field values for the record
    field_names = table_names[table_name][1:]
    new_values = [input(f"Enter the new {field_name}: ") for field_name in field_names]

    # Construct the UPDATE query with the new field values and primary key ID
    set_clause = ", ".join([f"{field_name} = %s" for field_name in field_names])
    query = f"UPDATE {table_name} SET {set_clause} WHERE {pk_name} = %s"

    # Execute the UPDATE query with the new values provided by the user
    mycursor.execute(query, tuple(new_values) + (pk_value,))
    # Commit the changes to the database
    mydb.commit()
    # Print a success message
    print(f"Record with {pk_name} {pk_value} updated in {table_name}!")

# Make queries
def make_queries():
    while True:
        # Prompt the user to enter a query
        query = input("Enter a SQL query (or 'quit' to exit): ")

        # If the user enters 'quit', exit the function
        if query.lower() == "quit":
            break

        try:
            # Execute the query
            mycursor.execute(query)

            # If the query is a SELECT query, print the results
            if query.upper().startswith("SELECT"):
                results = mycursor.fetchall()
                for row in results:
                    print(row)

            # Commit the changes to the database
            mydb.commit()
            # Print a success message
            print("Query executed successfully!")
        except mysql.connector.Error as e:
            # If there is an error, print the error message
            print("Error executing query:", e)

# Main Menu
option = ""
while option != "4":
    print('''MAIN MENU
    1. Add a new record
    2. Update an existing record
    3. Search for a record (Make queries)
    4. Exit''')

    # Prompt the user to choose an option
    option = input("Enter your choice: ")

    # Call the appropriate function based on the user's choice
    if option == "1":
        add_record()
    elif option == "2":
        update_record()
    elif option == "3":
        make_queries()
