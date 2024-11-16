from datetime import datetime

def seconds_since_birth(day, month, year):
    """
    Calculate seconds lived from birth date until now
    
    Args:
        day (int): Day of birth
        month (int): Month of birth 
        year (int): Year of birth
        
    Returns:
        float: Total seconds lived
    """
    # Create datetime object for birth date
    birth_date = datetime(year, month, day)
    
    # Get current date and time
    current_date = datetime.now()
    
    # Calculate time difference
    time_lived = current_date - birth_date
    
    # Convert to total seconds
    seconds_lived = time_lived.total_seconds()
    
    return seconds_lived


seconds = seconds_since_birth(7, 7, 2005)
print(f"You have lived {int(seconds)} seconds")
