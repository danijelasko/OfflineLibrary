import sqlite3
from datetime import datetime

def insert_books():
    conn = sqlite3.connect("library.db")
    c = conn.cursor()

    c.execute("DELETE FROM Books")  # Dodaj ovo prije c.executemany(...)


    books = [
        ('1', 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', '9780747532699', '1997', 'Bloomsbury', 'Fantasy', 'The first book in the Harry Potter series.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('2', 'The Hobbit', 'J.R.R. Tolkien', '9780345339683', '1937', 'George Allen & Unwin', 'Fantasy', 'A fantasy novel about a hobbit\'s adventure.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('3', '1984', 'George Orwell', '9780451524935', '1949', 'Secker & Warburg', 'Dystopian', 'A novel set in a dystopian future under a totalitarian regime.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('4', 'To Kill a Mockingbird', 'Harper Lee', '9780061120084', '1960', 'J.B. Lippincott & Co.', 'Fiction', 'A novel about racial injustice in the American South.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('5', 'The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', '1925', 'Charles Scribner\'s Sons', 'Fiction', 'A novel about the American dream and the decadence of the Jazz Age.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('6', 'Pride and Prejudice', 'Jane Austen', '9781503290563', '1813', 'T. Egerton', 'Romance', 'A classic novel about love and marriage in early 19th century England.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('7', 'Moby-Dick', 'Herman Melville', '9781853260087', '1851', 'Harper & Brothers', 'Adventure', 'A novel about Captain Ahab\'s obsessive quest to kill the white whale, Moby Dick.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('8', 'The Catcher in the Rye', 'J.D. Salinger', '9780316769488', '1951', 'Little, Brown and Company', 'Fiction', 'A novel about the teenage rebellion and alienation of Holden Caulfield.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('9', 'Brave New World', 'Aldous Huxley', '9780060850524', '1932', 'Chatto & Windus', 'Dystopian', 'A novel set in a world where society is engineered for maximum stability and happiness.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('10', 'War and Peace', 'Leo Tolstoy', '9780143039990', '1869', 'The Russian Messenger', 'Historical Fiction', 'A sweeping tale of Russian society during the Napoleonic Wars.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('11', 'The Odyssey', 'Homer', '9780143039952', '8th century BC', 'Penguin Classics', 'Epic', 'An ancient Greek epic poem about the hero Odysseus and his journey home after the Trojan War.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('12', 'The Divine Comedy', 'Dante Alighieri', '9780140448955', '1320', 'Penguin Classics', 'Epic Poetry', 'An epic poem about Dante\'s journey through Hell, Purgatory, and Heaven.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('13', 'Les Misérables', 'Victor Hugo', '9780140444308', '1862', 'A. Lacroix, Verboeckhoven & Cie', 'Historical Fiction', 'A novel about the struggles of various characters during the French Revolution.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('14', 'Crime and Punishment', 'Fyodor Dostoevsky', '9780140449136', '1866', 'The Russian Messenger', 'Psychological Fiction', 'A novel about a young man who commits a crime and struggles with guilt and redemption.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('15', 'The Brothers Karamazov', 'Fyodor Dostoevsky', '9780374528379', '1880', 'The Russian Messenger', 'Philosophical Fiction', 'A novel exploring morality, free will, and the nature of existence.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('16', 'Anna Karenina', 'Leo Tolstoy', '9780143035008', '1877', 'The Russian Messenger', 'Romance', 'A tragic novel about love, infidelity, and society in Imperial Russia.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('17', 'Dracula', 'Bram Stoker', '9780141439846', '1897', 'Archibald Constable and Company', 'Horror', 'A gothic novel about the infamous vampire Count Dracula.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('18', 'Frankenstein', 'Mary Shelley', '9780486282114', '1818', 'Lackington, Hughes, Harding, Mavor & Jones', 'Horror', 'A novel about a scientist who creates a living being, only to regret it.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('19', 'The Picture of Dorian Gray', 'Oscar Wilde', '9780141439570', '1890', 'Lippincott\'s Monthly Magazine', 'Gothic Fiction', 'A novel about a man whose portrait ages while he remains young, indulging in a life of decadence.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('20', 'Wuthering Heights', 'Emily Brontë', '9780141439556', '1847', 'Thomas Cautley Newby', 'Gothic Fiction', 'A novel about the tumultuous love affair between Heathcliff and Catherine Earnshaw.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('21', 'The Scarlet Letter', 'Nathaniel Hawthorne', '9780451531346', '1850', 'Ticknor, Reed, and Fields', 'Historical Fiction', 'A novel about a woman who commits adultery and the consequences she faces.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('22', 'A Tale of Two Cities', 'Charles Dickens', '9781853260100', '1859', 'Chapman and Hall', 'Historical Fiction', 'A novel set during the French Revolution, focusing on themes of resurrection and sacrifice.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('23', 'Great Expectations', 'Charles Dickens', '9780141439563', '1861', 'Chapman and Hall', 'Fiction', 'A novel about the life of an orphan named Pip and his aspirations to become a gentleman.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('24', 'The Call of the Wild', 'Jack London', '9780486264721', '1903', 'Macmillan', 'Adventure', 'A novel about a dog named Buck who is taken from his home and becomes a sled dog in the Yukon.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('25', 'The Road', 'Cormac McCarthy', '9780307387899', '2006', 'Alfred A. Knopf', 'Post-apocalyptic Fiction', 'A novel about a father and son surviving in a post-apocalyptic world.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('26', 'Siddhartha', 'Hermann Hesse', '9780553208849', '1922', 'New Directions', 'Philosophical Fiction', 'A novel about the journey of self-discovery of a man named Siddhartha.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('27', 'The Bell Jar', 'Sylvia Plath', '9780060837020', '1963', 'Harper & Row', 'Autobiographical Fiction', 'A semi-autobiographical novel about a woman\'s descent into mental illness.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('28', 'The Glass Menagerie', 'Tennessee Williams', '9780811214046', '1944', 'New Directions', 'Drama', 'A play about a family struggling to cope with their personal issues.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('29', 'The Catcher in the Rye', 'J.D. Salinger', '9780316769488', '1951', 'Little, Brown and Company', 'Fiction', 'A novel about the teenage rebellion and alienation of Holden Caulfield.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d')),
        ('30', 'Brave New World', 'Aldous Huxley', '9780060850524', '1932', 'Chatto & Windus', 'Dystopian', 'A novel set in a world where society is engineered for maximum stability and happiness.', None, datetime.now().strftime('%Y-%m-%d'), datetime.now().strftime('%Y-%m-%d'))
    ]

    c.executemany(''' 
        INSERT INTO Books (book_id, title, author, isbn, publication_date, publisher, genre, description, cover_image, added_date, modified_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', books)

    conn.commit()
    conn.close()

# Poziv funkcije
insert_books()
