import sqlite3

def main():
    #Connect to the books database
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    #Execute a query to select all data from the titles table
    cursor.execute("SELECT * FROM titles")

    #Retrieve column names from cursor.description
    column_names = [desc[0] for desc in cursor.description]

    #Retrieve all rows of data
    rows = cursor.fetchall()

    #Print column headers
    print("\t".join(column_names))
    print("-" * 60)

    #Print each row in tabular format
    for row in rows:
        print("\t".join(str(item) for item in row))

    #Close the connection
    connection.close()

if __name__ == "__main__":
    main()
