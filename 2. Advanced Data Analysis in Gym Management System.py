from connect_mysql import connect_database 

def get_members_in_age_range(start_age, end_age):
    conn = connect_database()
    cursor = conn.cursor()
    #Search Members between the specified ages
    search_query = 'SELECT * FROM Members WHERE age BETWEEN %s AND %s'
    cursor.execute(search_query, (start_age, end_age))
    print(f'Members between the age {start_age} and {end_age}')
    for member in cursor.fetchall():
        print(member)

