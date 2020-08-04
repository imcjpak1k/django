from datetime import datetime
import sys
import caldav
from caldav.elements import dav, cdav

# url = 'https://caldav.calendar.naver.com:443'
url = 'https://caldav.calendar.naver.com'
username='cinema76'
password=')windy76'

 

# [CalDAV 설정 정보]
# - 서버: caldav.calendar.naver.com
# - 사용자이름: 네이버 id
# - 암호: 네이버 비밀번호
# - 설명: 사용자가 원하는 텍스트
# - 고급 설정값: SSL 사용(on). 포트(443)

client = caldav.DAVClient(url=url, username=username, password=password, ssl_verify_cert=True)
## You may list up the calendars you own through the principal-object
my_principal = client.principal()
calendars = my_principal.calendars()
if calendars:
    ## Some calendar servers will include all calendars you have
    ## access to in this list, and not only the calendars owned by
    ## this principal.  TODO: see if it's possible to find a list of
    ## calendars one has access to.
    print("your principal has %i calendars:" % len(calendars))
    for c in calendars:
        print("    Name: %-20s  URL: %s" % (c.name, c.url))
else:
    print("your principal has no calendars")



this_cal = None
if len(calendars) > 0:
    for calendar in calendars:
        properties = calendar.get_properties([dav.DisplayName(), ])
        display_name = properties['{DAV:}displayname']
        # 캘린더명 가져오기
        # print(properties)
        if display_name == '내 캘린더':
            this_cal = calendar
            all_events = calendar.events()
            for e in all_events:
                print(e.load().data)
        #     break


all_events[0].data

# https://caldav.calendar.naver.com/caldav/cinema76/calendar/974967/
# https://caldav.calendar.naver.com/caldav/cinema76/calendar/2506846/
# https://caldav.calendar.naver.com/caldav/cinema76/calendar/25981363/

caldav.Calendar(client=client, url='https://caldav.calendar.naver.com/caldav/cinema76/calendar/974967')


each_calendar = caldav.Calendar(client=client, url=calendars[0].url)
all_events = each_calendar.events()


# >>> calendars[0].name
# '내 캘린더'
# >>> calendars[0].search
# <bound method Calendar.search of Calendar(https://caldav.calendar.naver.com/caldav/cinema76/calendar/974967/)>
# >>> dir(calendars[0].search)
# ['__call__', '__class__', '__delat

# events_fetched = calendars[0].date_search(start=datetime(2020, 8, 4), end=datetime(2024, 1, 1), compfilter='VEVENT', expand=True)



## Let's try with a task list.  Some servers cannot combine events and todos in the same calendar.
# my_new_tasklist = my_principal.make_calendar( supported_calendar_component_set=['VEVENT'])