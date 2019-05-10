import sqlite3

def main():
    conn = sqlite3.connect('pc.db')
    curs = conn.cursor()

    for row in curs.execute("SELECT * FROM pc",):
        print(row)
    

    conn.commit()
    conn.close()
if __name__=='__main__':
    main()
