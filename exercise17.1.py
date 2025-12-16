import sqlite3

def main():
    connection = sqlite3.connect("books.db")
    cursor = connection.cursor()

    print("\n=== 17.1(a) Authors' Last Names (Descending Order) ===")
    cursor.execute("SELECT last FROM authors ORDER BY last DESC")
    for row in cursor.fetchall():
        print(row[0])

    print("\n=== 17.1(b) Book Titles (Ascending Order) ===")
    cursor.execute("SELECT title FROM titles ORDER BY title ASC")
    for row in cursor.fetchall():
        print(row[0])

    print("\n=== 17.1(c) Books for a Specific Author (INNER JOIN) ===")
    #Change the author's last name here if you want a different one
    author_last_name = "Deitel"

    cursor.execute("""
        SELECT titles.title, titles.copyright, titles.isbn
        FROM titles
        INNER JOIN author_ISBN ON titles.isbn = author_ISBN.isbn
        INNER JOIN authors ON authors.id = author_ISBN.id
        WHERE authors.last = ?
        ORDER BY titles.title ASC
    """, (author_last_name,))

    for row in cursor.fetchall():
        print(row)

    print("\n=== 17.1(d) Insert a New Author ===")
    new_first = "John"
    new_last = "Smith"

    cursor.execute("INSERT INTO authors (first, last) VALUES (?, ?)",
                   (new_first, new_last))
    connection.commit()
    print(f"Inserted author: {new_first} {new_last}")

    print("\n=== 17.1(e) Insert a New Title for the New Author ===")
    #Example new book
    new_isbn = "9999999999"
    new_title = "Python for Everyone"
    new_edition = 1
    new_copyright = 2025

    #Insert into titles table
    cursor.execute("""
        INSERT INTO titles (isbn, title, edition, copyright)
        VALUES (?, ?, ?, ?)
    """, (new_isbn, new_title, new_edition, new_copyright))

    #Get the ID of the author we just inserted
    cursor.execute("SELECT id FROM authors WHERE last = ? AND first = ?",
                   (new_last, new_first))
    author_id = cursor.fetchone()[0]

    #Insert into author_ISBN table
    cursor.execute("""
        INSERT INTO author_ISBN (id, isbn)
        VALUES (?, ?)
    """, (author_id, new_isbn))

    connection.commit()
    print(f"Inserted new title '{new_title}' for author {new_first} {new_last}")

    connection.close()

if __name__ == "__main__":
    main()
