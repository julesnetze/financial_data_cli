from datetime import datetime, timezone


def convert_to_unix_date(date):
    date_list = date.split('-')
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])
    date = int(datetime(year, month, day, 0, 0, tzinfo=timezone.utc).timestamp())
    return date