
import datetime

def convert_date_string(date_string):
	return datetime.datetime.strptime(date_string, "%Y-%m-%d").strftime("%d-%m-%Y")

def datetime_to_t_format(dt):
	return dt.strftime("%Y-%m-%dT00:00:00")
