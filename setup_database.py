import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MySQL configuration
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_DATABASE'),
}

# Connect to MySQL server without specifying a database
connection = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password']
)
cursor = connection.cursor()

# Create the database if it doesn't exist
create_database_query = f"CREATE DATABASE IF NOT EXISTS {db_config['database']}"
cursor.execute(create_database_query)
connection.commit()

# Close the connection without specifying a database
cursor.close()
connection.close()

# Connect to the specific database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create the 'products' table
create_table_query = '''
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    brand VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL
)
'''
cursor.execute(create_table_query)
connection.commit()

# Insert initial data into the 'products' table

insert_data_query = '''
INSERT INTO products (name, brand, type, price) VALUES
    ('Candy K', 'Kylie Cosmetics', 'Batom', 159.90),
    ('Color Sensational', 'Maybelline', 'Batom', 30.00),
    ('Dragon Girl', 'NARS', 'Batom', 110.50),
    ('Russian Red', 'Mac', 'Batom', 90.00),
    ('Lip Injection Plump', 'Too Faced', 'Gloss', 169.99),
    ('Diva', 'Mac', 'Batom', 95.90)
'''

cursor.execute(insert_data_query)
connection.commit()

# Close the database connection
cursor.close()
connection.close()
