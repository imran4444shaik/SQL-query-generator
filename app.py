import re

def generate_sql():
    # Ask the user for input
    user_input = input("Enter your request (e.g., 'Show me all customers from New York'): ")
    
    # Step 1: Extract SELECT part (what to show)
    if "all" in user_input.lower():
        select_part = "*"  # If user says "all", select all columns
    else:
        # Look for phrases like "show me X, Y, Z"
        match = re.search(r'show me (.*?) from', user_input, re.IGNORECASE)
        if match:
            columns = match.group(1).replace(" and ", ", ").strip()
            select_part = columns
        else:
            select_part = "*"  # Default to "all"
    
    # Step 2: Extract FROM part (table name)
    from_match = re.search(r'from (\w+)', user_input, re.IGNORECASE)
    if from_match:
        from_part = from_match.group(1)
    else:
        from_part = "my_table"  # Default table name
    
    # Step 3: Extract WHERE part (filter)
    where_part = ""
    # Look for phrases like "from New York" or "where city is New York"
    where_match = re.search(r'(?:where|from)\s+(\w+)\s+(?:is|in|from|=)\s*[\'"]?([\w\s]+)[\'"]?', user_input, re.IGNORECASE)
    if where_match:
        column = where_match.group(1)
        value = where_match.group(2)
        # Add quotes if the value is text (not a number)
        if not value.isdigit():
            value = f"'{value}'"
        where_part = f"WHERE {column} = {value}"
    
    # Build the SQL query
    sql_query = f"SELECT {select_part} FROM {from_part} {where_part};".strip()
    # Remove extra spaces
    sql_query = ' '.join(sql_query.split())
    
    print(f"\nGenerated SQL Query:\n{sql_query}")

# Run the program
generate_sql()
