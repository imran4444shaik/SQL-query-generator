# SQL-query-generator

Purpose:
Convert a natural language request (entered by the user) into a basic SQL query.

How It Works:

User Input:
The program prompts the user to enter a request (e.g., "Show me all customers from New York").

Extracting the SELECT Part:
If the word "all" is detected:
It sets the SELECT clause to *, meaning all columns.
Otherwise:
It uses a regular expression to capture a list of columns mentioned after the phrase "show me" and before "from".
The captured columns are cleaned (e.g., converting "name and age" into "name, age").

Extracting the FROM Part:
A regular expression searches for the table name following the word "from".
If no table is found, it defaults to "my_table".

Extracting the WHERE Part:
The code uses another regular expression to look for a condition in the input (e.g., "from New York" or "where city is New York").
It extracts both the column name and its value.
If the value isn’t a digit, it wraps the value in quotes.
The condition is then formatted into a WHERE clause (e.g., WHERE city = 'New York').

Building the SQL Query:
The SELECT, FROM, and (if available) WHERE parts are concatenated into a complete SQL query.
Extra spaces are removed to ensure the query is cleanly formatted.

Output:
The generated SQL query is printed to the console.
