import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  

if __name__ == '__main__':
   
    passcards = Passcard.objects.all()
    some_passcard = passcards[0]

    print(f"Всего пропусков {len(passcards)}")
    
    active_passcards = Passcard.objects.filter(is_active=True)
    
    print(f"Активных пропусков {len(active_passcards)}")