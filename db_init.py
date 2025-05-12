import sqlite3

def init_db():
    # Povezivanje na SQLite bazu (baza će biti stvorena ako ne postoji)
    conn = sqlite3.connect("library.db")
    c = conn.cursor()

    print("Kreiram tablice...")

    # Kreiranje tablice Books
    c.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            book_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT,
            isbn TEXT,
            publication_date TEXT,
            publisher TEXT,
            genre TEXT,
            description TEXT,
            cover_image BLOB,
            added_date TEXT NOT NULL,
            modified_date TEXT NOT NULL,
            sync_status INTEGER DEFAULT 0
        )
    ''')
    print("Tablica Books stvorena.")

    # Kreiranje tablice Collections
    c.execute('''
        CREATE TABLE IF NOT EXISTS Collections (
            collection_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            created_date TEXT NOT NULL,
            modified_date TEXT NOT NULL,
            sync_status INTEGER DEFAULT 0
        )
    ''')
    print("Tablica Collections stvorena.")

    # Kreiranje tablice BookCollections (poveznica između knjiga i kolekcija)
    c.execute('''
        CREATE TABLE IF NOT EXISTS BookCollections (
            book_id TEXT,
            collection_id TEXT,
            added_date TEXT NOT NULL,
            PRIMARY KEY (book_id, collection_id),
            FOREIGN KEY (book_id) REFERENCES Books(book_id),
            FOREIGN KEY (collection_id) REFERENCES Collections(collection_id)
        )
    ''')
    print("Tablica BookCollections stvorena.")

    # Kreiranje tablice ReadingProgress
    c.execute('''
        CREATE TABLE IF NOT EXISTS ReadingProgress (
            progress_id TEXT PRIMARY KEY,
            book_id TEXT,
            user_id TEXT,
            page_number INTEGER,
            percentage REAL,
            last_read_date TEXT NOT NULL,
            notes TEXT,
            sync_status INTEGER DEFAULT 0,
            FOREIGN KEY (book_id) REFERENCES Books(book_id)
        )
    ''')
    print("Tablica ReadingProgress stvorena.")

    # Kreiranje tablice LoanRecords
    c.execute('''
        CREATE TABLE IF NOT EXISTS LoanRecords (
            loan_id TEXT PRIMARY KEY,
            book_id TEXT,
            borrower_name TEXT NOT NULL,
            borrower_contact TEXT,
            loan_date TEXT NOT NULL,
            due_date TEXT,
            return_date TEXT,
            status TEXT NOT NULL,
            sync_status INTEGER DEFAULT 0,
            FOREIGN KEY (book_id) REFERENCES Books(book_id)
        )
    ''')
    print("Tablica LoanRecords stvorena.")

    # Kreiranje tablice SyncLog
    c.execute('''
        CREATE TABLE IF NOT EXISTS SyncLog (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            entity_type TEXT NOT NULL,
            entity_id TEXT NOT NULL,
            action_type TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    print("Tablica SyncLog stvorena.")

    # Spremanje promjena i zatvaranje konekcije
    conn.commit()
    conn.close()

    print("Baza podataka uspješno inicijalizirana.")

# Pozivanje funkcije za inicijalizaciju baze
init_db()
