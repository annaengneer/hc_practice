import datetime
import sys
import argparse


class Calendar:

    def __init__(self, month, year):
        self.month = month
        self.year = year

    def get_days(self, year, month):
        if month == 12:
            next_month = 1
            next_year = year + 1
        else:
            next_month = month + 1
            next_year = year
        last_date = (datetime.date(next_year, next_month, 1)- datetime.timedelta(days=1)).day
        return last_date

    def get_week(self, year, month):
        return datetime.date(year, month, 1).weekday()
        

    def print_calendar(self):
        last_date = self.get_days(self.year, self.month)
        first_day = self.get_week(self.year, self.month)


        print(  f" {self.month}月 {self.year}")

        print("月 火 水 木 金 土 日")

        print(" " * 3 * first_day, end="")

        for day in range(1, last_date + 1):
            print(f"{day:2d} ", end="")
            if (day + first_day) % 7 == 0:
                print()
        print()
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m',   type=int, required=True)
    args = parser.parse_args()
    month = args.m
    if not 1 <= month <=12:
        print(f'{month} is neither a month number (1..12) nor a name')
        sys.exit(1)

    dt = datetime.datetime.now()
    cal = Calendar(month, dt.year)
    cal.print_calendar()
    

if __name__ == "__main__":
   main()
