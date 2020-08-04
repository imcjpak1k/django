from datetime import datetime, date
from pytz import timezone, utc
import sys
import caldav
from caldav.elements import dav, cdav

def get_vevent_data(event, event_type='VEVENT'):
    '''
    VEVENT반환
    '''
    data = {}
    for component in event.load().icalendar_instance.walk():  
        if component.name != event_type: continue
        for key in component.keys():
            # icalendar.prop.vDDDTypes . dt // 날짜
            data[key.lower()] = component.get(key)
    return data
    # >>> componentd.keys()
    # odict_keys(['DTSTAMP', 'X-NAVER-REGISTERER', 'X-NAVER-STICKER', 'DTSTART', 'DTEND', 'CREATED', 'PRIORITY', 'LAST-MODIFIED', 'X-NAVER-LAST-MODIFIER', 'UID', 'summary', 'SEQUENCE'])




# url = 'https://caldav.calendar.naver.com:443'
url = 'https://caldav.calendar.naver.com'
username='아이디'
password='비밀번호'

 

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
# if calendars:
#     ## Some calendar servers will include all calendars you have
#     ## access to in this list, and not only the calendars owned by
#     ## this principal.  TODO: see if it's possible to find a list of
#     ## calendars one has access to.
#     print("your principal has %i calendars:" % len(calendars))
#     for c in calendars:
#         print("    Name: %-20s  URL: %s" % (c.name, c.url))
# else:
#     print("your principal has no calendars")


# regExp_dtstart = re.compile('(0-9){8}') 
# regExp_dtstart = re.compile('(20100729)')  
# DTSTART;TZID=Asia/Seoul:20100729T100000
# DTEND;TZID=Asia/Seoul:20100729T110000

KST = timezone('Asia/Seoul')
now = utc.localize(datetime.utcnow()).astimezone(KST).strftime('%Y%m%d')

if len(calendars) > 0:
    for calendar in calendars:
        properties = calendar.get_properties([dav.DisplayName(), ])
        display_name = properties['{DAV:}displayname']
        # 캘린더명 가져오기
        # print(properties)
        if display_name != '내 캘린더':continue
            # all_events = calendar.events()
        for event in calendar.events():
            data = get_vevent_data(event)
            dtstart = data.get('dtstart').dt.strftime('%Y%m%d')
            dtend = data.get('dtend').dt.strftime('%Y%m%d')
            # if type(dtstart.dt) == type(date.today()) :continue
            # print(type(dtstart.dt))
            # print(dtend.dt)
            print(display_name, dtstart, now, dtend)
            if not dtstart <= now <= dtend: continue
            print(display_name, data, '===============>', data.get('summary'))
            
                

>>> events[0].load().data
'BEGIN:VCALENDAR\r\nPRODID:Works Mobile Calendar\r\nVERSION:2.0\r\nBEGIN:VEVENT\r\nDTSTAMP:20180708T022919Z\r\nX-NAVER-REGISTERER;X-WORKSMOBILE-WID=cinema76;CUTYPE=INDIVIDUAL:1596542664163\r\nX-NAVER-STICKER;X-WORKSMOBILE-POS=0:001\r\nDTSTART;TZID=Asia/Seoul:20100803T160000\r\nDTEND;TZID=Asia/Seoul:20100803T170000\r\nCREATED:20100728T041418Z\r\nPRIORITY:1\r\nLAST-MODIFIED:20100728T041429Z\r\nX-NAVER-LAST-MODIFIER;X-WORKSMOBILE-WID=cinema76;CUTYPE=INDIVIDUAL:1596542664163\r\nUID:349ef944d655ed2e6dbbc7ed42ddf95174a51c56f4aaf3b68c49824266a9ddfa@naver.com\r\nSUMMARY:SW 아키텍처 구현교육\\, 대회의실(청명)\r\nSEQUENCE:0\r\nBEGIN:VALARM\r\nACTION:DISPLAY\r\nTRIGGER:-PT10M\r\nEND:VALARM\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n'
.

events = this_cal.events() 
data = events[0].load().data
r = re.compile('[^\s]*')
r.findall(data)

LAST-MODIFIED:20100728T041429Z



componentd= None
summary = None
dtstart = None
dtend = None
dtstamp = None
for component in e.icalendar_instance.walk(): 
    if component.name != "VEVENT": continue
    componentd = component 
    # icalendar.prop.vDDDTypes . dt
    summary = component.get('summary')
    dtstart = component.get('dtstart')
    dtend = component.get('dtend')
    dtstamp = component.get('dtstamp')



c = None
for component in this_cal.events()[0].load().icalendar_instance.walk(): 
    print(component.name)
    if component.name != "VEVENT": continue
    c = component
    # icalendar.prop.vDDDTypes . dt
    summary = component.get('summary')
    dtstart = component.get('dtstart')
    dtend = component.get('dtend')
    dtstamp = component.get('dtstamp')





 dir(e.icalendar_instance)
['__bool__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__delitem__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
  '__len__',
  '__lt__',
  '__module__',
  '__ne__',
  '__new__',
  '__nonzero__',
  '__reduce__',
  '__reduce_ex__',
  '__repr__',
  '__reversed__',
  '__setattr__',
  '__setitem__',
  '__sizeof__',
  '__str__',
  '__subclasshook__',
  '_decode',
  '_encode',
  '_walk',
   'add',
   'add_component',
   'canonical_order',
   'clear',
   'content_line',
   'content_lines',
   'copy',
   'decoded',
   'errors',
   'exclusive',
   'from_ical',
   'fromkeys',
   'get',
   'get_inline',
   'has_key',
   'ignore_exceptions',
    'inclusive',
    'is_broken',
    'is_empty',
    'items',
    'keys',
    'move_to_end',
    'multiple',
    'name',
    'pop',
    'popitem',
    'property_items',
    'required',
    'set_inline',
    'setdefault',
    'singletons',
    'sorted_items',
    'sorted_keys',
    'subcomponents', 'to_ical', 'update', 'values', 'walk']



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