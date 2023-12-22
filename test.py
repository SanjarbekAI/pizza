from datetime import datetime, date

# Example date string
date_string = "2023-01-01"

# Parse the date string to a datetime object
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d")
print(parsed_datetime)