import datetime

from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello Bitcoin!')

def get_time(request, tz='X'):

    if tz=='X':
        tz = request.GET.get('tz', 'CET') #ifnot tz --> CET

    time_data = {
        'CET': 0,
        'BRT': -4,
        'CDT': -5,
        'GMT': -1,
    }

    data = time_data.get(tz, 0)
    uhrzeit = datetime.datetime.now() + datetime.timedelta(hours=data)

    return HttpResponse(f'''
    <!DOCTYPE>
    <html>
    <body>
    {uhrzeit} ({tz})
    </body>
    </html>
    
    
    
    
    
    ''')
