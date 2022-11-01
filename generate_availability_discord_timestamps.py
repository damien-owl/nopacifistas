from typing import List
from dateutil import tz
from datetime import date, time, datetime, timedelta

FROM_YEAR = 2022
FROM_MONTH = 11
FROM_DAY = 5
TILL_YEAR = 2022
TILL_MONTH = 12
TILL_DAY = 17
MIN_HOUR = 9
MAX_HOUR = 17
AEDT_TZ = tz.gettz("Australia/Sydney")
ELIGIBLE_DAYS = [6, 7]  # 6: Saturday, 7: Sunday
ISO_DAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
ISO_MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def print_hourly_discord_datetimes(from_date: date, till_date: date, min_hour: time, max_hour: time, timezone: tz,
                                   eligible_days: List[int]) -> None:
    print(f'print_hourly_discord_datetimes(from={from_date}, till={till_date}, min_hour={min_hour}, max_hour={max_hour}'
          f', eligible_days={eligible_days})')
    one_day_delta = timedelta(days=1)
    one_hour_delta = timedelta(hours=1)
    if from_date <= till_date and min_hour <= max_hour:
        current_date = from_date
        while current_date <= till_date:
            if current_date.isoweekday() in eligible_days:
                print(f"\n{ISO_DAYS[current_date.isoweekday()]} {current_date.day} {ISO_MONTHS[current_date.month]}"
                      f" {current_date.year}")
                current_dt = datetime.combine(current_date, min_hour, tzinfo=timezone)
                while current_dt.hour <= max_hour.hour:
                    print(f"<t:{int(current_dt.timestamp())}:f>")
                    current_dt = current_dt + one_hour_delta
            current_date = current_date + one_day_delta


if __name__ == '__main__':
    print_hourly_discord_datetimes(
        from_date=date(FROM_YEAR, FROM_MONTH, FROM_DAY),
        till_date=date(TILL_YEAR, TILL_MONTH, TILL_DAY),
        min_hour=time(MIN_HOUR),
        max_hour=time(MAX_HOUR),
        timezone=AEDT_TZ,
        eligible_days=ELIGIBLE_DAYS
    )

