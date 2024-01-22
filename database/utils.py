from sqlite_module import SQLiteModule
from gui.utils import is_valid_email
from cryptography.fernet import Fernet
from core.settings import DATABASE_PATH, ENCRYPTION_KEY

def create_email_table():
    db = SQLiteModule(DATABASE_PATH)
    try:
        db.create_table("emails", "name TEXT, email TEXT, created_at TEXT, send_at TEXT, last_sent TEXT")
    except Exception as e:
        print(e)
        return False
    db.close()
    return True

def insert_email(name, email, send_at):
    db = SQLiteModule(DATABASE_PATH)
    if not is_valid_email(email):
        return False
    db.insert("emails", "name, email, created_at, send_at, last_sent", f"'{name}', '{email}', datetime('now'), '{send_at}', 'Never'")
    db.close()
    return True

def select_emails():
    db = SQLiteModule(DATABASE_PATH)
    emails = db.select("emails", "*")
    db.close()
    return emails

def select_email(email):
    db = SQLiteModule(DATABASE_PATH)
    email = db.select("emails", "*", f"email='{email}'")
    db.close()
    return email

def update_email(email, send_at, last_sent):
    db = SQLiteModule(DATABASE_PATH)
    try:
        db.update("emails", f"send_at='{send_at}', last_sent='{last_sent}'", f"email='{email}'")
    except Exception as e:
        print(e)
        return False
    db.close()
    return True

def delete_email(email):
    db = SQLiteModule(DATABASE_PATH)
    try:
        db.delete("emails", f"email='{email}'")
    except Exception as e:
        print(e)
        return False
    db.close()
    return True

def create_user_table():
    db = SQLiteModule(DATABASE_PATH)
    try:
        db.create_table("users", "email TEXT, password TEXT")
    except Exception as e:
        print(e)
        return False
    db.close()
    return True



def encrypt_password(password):
    key = ENCRYPTION_KEY.encode()
    f = Fernet(key)
    return f.encrypt(password.encode()).decode()

def decrypt_password(password):
    key = ENCRYPTION_KEY.encode()
    f = Fernet(key)
    return f.decrypt(password.encode()).decode()

def insert_user(email, password):
    db = SQLiteModule(DATABASE_PATH)
    if not is_valid_email(email):
        return False
    password = encrypt_password(password)
    db.insert("users", "email, password", f"'{email}', '{password}'")
    db.close()
    return True

def get_user(email):
    db = SQLiteModule(DATABASE_PATH)
    user = db.select("users", "*", f"email='{email}'")
    db.close()
    return user

def update_user(email, password):
    db = SQLiteModule(DATABASE_PATH)
    password = encrypt_password(password)
    db.update("users", f"password='{password}'", f"email='{email}'")
    db.close()
    return True

def delete_user(email):
    db = SQLiteModule(DATABASE_PATH)
    db.delete("users", f"email='{email}'")
    db.close()
    return True
