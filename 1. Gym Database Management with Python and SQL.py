from connect_mysql import connect_database 

#Task 1: Add a Member

def add_member(id, name, age):
    conn = connect_database()
    cursor = conn.cursor()
    try:
        new_member = (id, name, age)
        #Adds a new member into the Members Table
        query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, new_member)
        conn.commit()
        print("New member has joined the gym!")
    except Exception as e:
        if "Duplicate entry" in str(e):
            print(f'Error: A member with ID {id} already exists.')
        else:
            print(f'An error occured: {e}')
    finally:
        cursor.close()
        conn.close()

#Task 2: Add a Workout Session


def add_workout_session(member_id, date, duration_minutes, calories_burned):
    conn = connect_database()
    cursor = conn.cursor()
    try:
        new_workout =  (member_id, date, duration_minutes, calories_burned)
        # Updates the new workout for specified member
        query = "INSERT INTO workoutsessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, new_workout)
        conn.commit()
        print("The workout has been added!")

    except Exception as e:
        if 'foreign key constraint' in str(e).lower():
            print(f'Error: the {member_id} you entered is invalid!')
        else:
            print(f'An error has occured: {e}')
    finally:
        cursor.close()
        conn.close()

#Task 3: Updating Member Information

def update_member_age(member_id, new_age):
    conn = connect_database()
    cursor = conn.cursor()
    try:
        # Check if member exists
        check_query = "SELECT COUNT(*) FROM Members WHERE id = %s"
        cursor.execute(check_query, (member_id,))
        result = cursor.fetchone()
        
        if result[0] == 0:
            print(f'Error: The member with ID {member_id} does not exist.')
        
        # Update age if member exists
        update_query = "UPDATE Members SET age = %s WHERE id = %s"
        cursor.execute(update_query, (new_age, member_id))
        conn.commit()
        print("The member's age has been updated.")
    
    except Exception as e:
        print(f'An error has occurred: {e}')
    
    finally:
        cursor.close()
        conn.close()

#Task 4: Delete a Workout Session

def delete_workout_session(session_id):
    conn = connect_database()
    cursor = conn.cursor()
    try:
        #Checks to see if session actually exists
        check_query = "SELECT COUNT(*) FROM workoutsessions WHERE session_id = %s"
        cursor.execute(check_query, (session_id,))
        result = cursor.fetchone()

        if result[0] == 0:
            print(f'Error: The Session with ID {session_id} does not exist.')
        
        #Deletes specified session from the workout listings
        delete_query = "DELETE FROM workoutsessions WHERE session_id = %s"
        cursor.execute(delete_query, (session_id,))
        conn.commit()
        print('The session has been deleted')


    except Exception as e:
        print(f'An error has occured: {e}')
    
    finally:
        cursor.close()
        conn.close()
