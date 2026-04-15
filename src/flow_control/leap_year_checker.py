def is_leap_year(year: int) -> bool:
    """
    Checks if a given year is a leap year.
    
    Logic:
    - Divisible by 4 AND not divisible by 100 OR (divisible by 400).
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    print('--- Leap Year Checker ---')
    try:
        year = int(input('Enter a year: '))
        if is_leap_year(year):
            print(f'{year} is a leap year.')
        else:
            print(f'{year} is not a leap year.')
    except ValueError:
        print("Please enter a valid integer for the year.")

if __name__ == "__main__":
    main()
