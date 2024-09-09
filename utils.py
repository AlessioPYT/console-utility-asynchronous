import sys

def parse_arguments():
    try:
        days = int(sys.argv[1])
    except (IndexError, ValueError):
        raise ValueError("Please provide a valid number of days (1-10).")
    
    return days
