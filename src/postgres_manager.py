import psycopg2
import pandas as pd
from psycopg2 import sql
from typing import Optional


class PostgresManager:
    def __init__(
        self, user: str, password: str, host: str = "localhost", port: str = "5432"
    ) -> None:
        """
        Initializes the PostgresManager with connection details.

        Args:
            user (str): The PostgreSQL user.
            password (str): The PostgreSQL user's password.
            host (str): The host of the PostgreSQL server. Defaults to 'localhost'.
            port (str): The port of the PostgreSQL server. Defaults to '5432'.
        """
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def _connect(self, dbname: str) -> psycopg2.extensions.connection:
        """
        Internal method to connect to a specific database.

        Args:
            dbname (str): The name of the database to connect to.

        Returns:
            psycopg2.extensions.connection: The connection object to the specified database.
        """
        return psycopg2.connect(
            dbname=dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )

    def check_and_create_database(self, dbname: str) -> None:
        """
        Checks if the database exists, and creates it if it doesn't.

        Args:
            dbname (str): The name of the database to check and create.
        """
        try:
            # Connect to the default postgres database
            conn = self._connect("postgres")
            conn.autocommit = True
            cursor = conn.cursor()

            # Check if the database exists
            cursor.execute(
                sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"),
                [dbname],
            )
            exists = cursor.fetchone()

            if not exists:
                # Create the database if it does not exist
                cursor.execute(
                    sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname))
                )
                print(f"Database '{dbname}' created successfully.")
            else:
                print(f"Database '{dbname}' already exists.")

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except Exception as error:
            print(f"Error: {error}")

    def check_and_create_table(
        self, dbname: str, table_name: str, create_table_sql: str
    ) -> None:
        """
        Checks if the table exists, and creates it if it doesn't.

        Args:
            dbname (str): The name of the database to connect to.
            table_name (str): The name of the table to check and create.
            create_table_sql (str): The SQL statement to create the table if it does not exist.
        """
        try:
            # Connect to the specified database
            conn = self._connect(dbname)
            conn.autocommit = True
            cursor = conn.cursor()

            # Check if the table exists
            cursor.execute(
                sql.SQL(
                    """
                SELECT EXISTS (
                    SELECT 1
                    FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = %s
                )
            """
                ),
                [table_name],
            )
            exists = cursor.fetchone()[0]
            if not exists:
                # Create the table if it does not exist
                cursor.execute(create_table_sql)
                print(f"Table '{table_name}' created successfully.")
            else:
                print(f"Table '{table_name}' already exists.")

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except Exception as error:
            print(f"Error: {error}")

    def drop_table(self, dbname: str, table_name: str) -> None:
        """
        Drops a table if it exists.

        Args:
            dbname (str): The name of the database containing the table.
            table_name (str): The name of the table to drop.
        """
        try:
            # Connect to the specified database
            conn = self._connect(dbname)
            conn.autocommit = True
            cursor = conn.cursor()

            # Drop the table if it exists
            cursor.execute(
                sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(table_name))
            )
            print(f"Table '{table_name}' dropped successfully.")

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except Exception as error:
            print(f"Error: {error}")

    def convert_to_postgres_sql(self, create_table_sql: str) -> str:
        """
        Converts MySQL SQL commands to PostgreSQL-compatible SQL.

        Args:
            create_table_sql (str): The MySQL SQL command to convert.

        Returns:
            str: The PostgreSQL-compatible SQL command.
        """
        # Replace ENUM with VARCHAR
        postgres_sql = create_table_sql.replace("ENUM", "VARCHAR")

        # Replace backticks with double quotes
        postgres_sql = postgres_sql.replace("`", '"')

        # Replace float with real (if needed, depending on MySQL to PostgreSQL type mapping)
        postgres_sql = postgres_sql.replace("float", "real")

        # Replace AUTO_INCREMENT with SERIAL
        postgres_sql = postgres_sql.replace("AUTO_INCREMENT", "SERIAL")

        # Add IF NOT EXISTS clause
        if postgres_sql.startswith("CREATE TABLE"):
            postgres_sql = postgres_sql.replace(
                "CREATE TABLE", "CREATE TABLE IF NOT EXISTS", 1
            )

        return postgres_sql

    def run_query(self, dbname: str, query: str) -> pd.DataFrame:
        try:
            conn = self._connect(dbname)
            cursor = conn.cursor()

            cursor.execute(query)
            columns = [desc[0] for desc in cursor.description]
            result = cursor.fetchall()

            cursor.close()
            conn.close()

            return pd.DataFrame(result, columns=columns)

        except Exception as error:
            print(f"Error: {error}")

    def get_table_schema(self, dbname: str, table_name: str) -> pd.DataFrame:
        """
        Retrieves the schema of the specified table.

        Args:
            dbname (str): The name of the database to connect to.
            table_name (str): The name of the table whose schema is to be retrieved.

        Returns:
            pd.DataFrame: DataFrame containing the schema information of the table.
        """
        try:
            conn = self._connect(dbname)
            cursor = conn.cursor()

            query = sql.SQL(
                """
                SELECT 
                    column_name, 
                    data_type, 
                    character_maximum_length, 
                    numeric_precision, 
                    is_nullable 
                FROM 
                    information_schema.columns 
                WHERE 
                    table_schema = 'public' 
                    AND table_name = %s;
            """
            )

            cursor.execute(query, [table_name])
            columns = [desc[0] for desc in cursor.description]
            result = cursor.fetchall()

            cursor.close()
            conn.close()

            return pd.DataFrame(result, columns=columns)

        except Exception as error:
            print(f"Error: {error}")
