from psycopg2 import connect
from environs import Env

env = Env()
env.read_env()

def get_connect():
    return connect(
        database=env.str("DATABASE"),
        user=env.str("USER"),
        password=env.str("PASSWORD"),
        host=env.str("HOST"),
        port=env.str("PORT")
    )

def create_table():
    sql = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            chat_id BIGINT NOT NULL UNIQUE,
            name VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            phone VARCHAR(255) NOT NULL,
            is_admin BOOLEAN default false
        );
        
        CREATE TABLE IF NOT EXISTS books (
            id BIGSERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            description VARCHAR(255) NOT NULL,
            genre VARCHAR(255) NOT NULL,
            price VARCHAR(255) NOT NULL,
            quantity VARCHAR(255) NOT NULL 
        );
        
        CREATE TABLE IF NOT EXISTS orders (
            id BIGSERIAL PRIMARY KEY,
            book_id BIGINT REFERENCES books(id),
            user_id BIGINT REFERENCES users(id),
            price BIGINT NOT NULL,
            quantity BIGINT NOT NULL default 1,
            status VARCHAR(255) default 'new',
            created_at TIMESTAMP default now()
        );
    """
    with get_connect() as db:
        with db.cursor() as dbc:
            dbc.execute(sql)
            db.commit()

create_table()
