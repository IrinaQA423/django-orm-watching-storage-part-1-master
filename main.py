import os

import django
from django.utils.timezone import localtime
from datetime import datetime, timedelta
from django.utils.dateformat import format
from django.db.models import Q

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit 


#print(owner_name[1])

def get_duration(visit):
    entered_time = localtime(visit.entered_at)
    
    if visit.leaved_at is None:
        current_time = localtime()
        duration = current_time - entered_time
    else:
        leaved_at = localtime(visit.leaved_at)  # теперь переменная объявлена
        duration = leaved_at - entered_time
    
    return duration

def format_duration(duration):
    total_seconds = duration.total_seconds()
    
    
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    
    return f"{hours}:{minutes}"

def get_visits_by_owner_name(owner_name):
    # Получаем все визиты для указанного владельца пропуска
    visits = Visit.objects.filter(passcard__owner_name=owner_name)
    
    # Дополнительно можно отсортировать по дате входа
    visits = visits.order_by('-entered_at')
    
    return visits



def get_long_visits(min_duration=60):
    # Получаем все визиты для указанного владельца
    visits = Visit.objects.filter(Q(leaved_at__isnull=False) | Q(leaved_at__isnull=True))
    
    long_visits = []
    for visit in visits:
        duration = get_duration(visit)
        duration_minutes = duration.total_seconds() / 60
        
        if duration_minutes > min_duration:
            formatted_duration = format_duration(duration)
            visit_info = {
                'owner_name': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at).strftime('%Y-%m-%d %H:%M:%S'),
                'duration': formatted_duration,
                'leaved_at': localtime(visit.leaved_at).strftime('%Y-%m-%d %H:%M:%S') if visit.leaved_at else 'still inside'
            }
            long_visits.append(visit_info)
    
    return long_visits

def get_long_visits_by_owner(owner_name, min_duration=60):
    # Получаем визиты только для указанного пользователя
    visits = Visit.objects.filter(passcard__owner_name=owner_name)
    
    long_visits = []
    for visit in visits:
        duration = get_duration(visit)
        duration_minutes = duration.total_seconds() / 60
        
        if duration_minutes > min_duration:
            formatted_duration = format_duration(duration)
            visit_info = {
                'entered_at': localtime(visit.entered_at).strftime('%Y-%m-%d %H:%M:%S'),
                'duration': formatted_duration,
                'leaved_at': localtime(visit.leaved_at).strftime('%Y-%m-%d %H:%M:%S') if visit.leaved_at else 'still inside'
            }
            long_visits.append(visit_info)
    
    return long_visits    

'''if __name__ == '__main__':
   
    #passcards = Passcard.objects.all()
    #some_passcard = passcards[0]

    #print(f"Всего пропусков {len(passcards)}")
    
    #active_passcards = Passcard.objects.filter(is_active=True)
    
    #print(f"Активных пропусков {len(active_passcards)}")
    visit = Visit.objects.all()
    #print(visit)

    #some_visit = visit[0]
    
    #print(some_visit)
    activ_visits = Visit.objects.filter(leaved_at=None)
    for visit in activ_visits:
        passcard = visit.passcard
        # Получаем локальное время для текущего часового пояса (Moscow)
       
        formatted_time = entered_time.strftime('%Y-%m-%d %H:%M:%S%z')

        # Вычисляем длительность пребывания
        

        # Форматируем длительность в HH:MM:SS
        hours, remainder = divmod(duration.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        duration_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
        
        print(passcard.owner_name)
        #print(f"Зашёл в хранилище, время по Москве:")
        #print(f"{formatted_time}")
        #print()
        #print("Находится в хранилище:")
        #print(f"{duration_str}")'''

   # 1. Все длительные визиты (больше 60 минут)

all_long_visits = get_long_visits()
for visit in all_long_visits:  # выводим первые 5 для примера
    print(f"{visit['owner_name']}: entered at {visit['entered_at']}, duration {visit['duration']}, leaved_at {visit['leaved_at']}")

    
'''if Passcard.objects.exists():
    some_owner = Passcard.objects.first().owner_name
    print(f"\nLong visits for {some_owner}:")
    owner_long_visits = get_long_visits_by_owner(some_owner)
    for visit in owner_long_visits:
        print(f"Entered at {visit['entered_at']}, duration {visit['duration']}")'''
