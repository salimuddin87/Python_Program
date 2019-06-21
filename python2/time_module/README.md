import time

Most of the functions defined in this module call platform C library functions 
with the same name. It may sometimes be helpful to consult the platform docume
-ntation, because the semantics of these functions varies among platforms.

epoch is the point where the time starts. On January 1st of that year, at 0 hours
For Unix the epoch is 1970. Functions in this module do not handle dates and times
before epoch or far in the future(i.e. 2038 for Unix)
>>> import time
>>> time.gmtime(0)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

Python depends on the platform’s C library, which generally doesn’t have year 
2000 issues, since all dates and times are represented internally as seconds 
since the epoch.

UTC is Coordinated Universal Time (formerly known as Greenwich Mean Time, or GMT). 
The acronym UTC is not a mistake but a compromise between English and French.


