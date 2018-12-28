#올해 경과된 날짜 수를 계산하는 프로그램
from time import localtime
t = localtime()
start_day = "%d-01-01"%t.tm_year
elapsed_day=t.tm_yday

print("오늘은 [%s]이후 [%d]일 째 되는 날입니다."%(start_day,elapsed_day))