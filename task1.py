from datetime import datetime, timedelta

num_days = int(input("Enter the number of days from today: "))

# Get today's date
today = datetime.today()

# Add the number of days to today's date
future_date = today + timedelta(days=num_days)

# Format the date as desired
formatted_date = future_date.strftime('%A, %B %d, %Y')

print(formatted_date)