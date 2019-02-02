from .views import *
from .tasks import *


def notigene(details):
    insurance = []
    fitness_certi = []
    noti = {}
    today = datetime.date.today()
    datetime.timedelta(7)
    # printer.delay(10)

    for i in details:
        if(((i.insurance_expiry-today).days) <= 15 or ((i.insurance_expiry-today).days) == 30):
            if(((i.insurance_expiry-today).days) < 0):
                string = str(i)+" "+"insurance has expired.Please renew it!!"
            else:
                string = str(i)+" "+"insurance expires in:- " + \
                    str((i.insurance_expiry-today).days)+"days"
            noti[string] = i.truck_number
            if(len(Notifications.objects.filter(truck_number=i.truck_number, insurance_id=i.insurance_number, boolean=True)) == 0):
                obj, notif = Notifications.objects.get_or_create(
                    truck_number=i.truck_number, insurance_id=i.insurance_number, data=string)
                if notif is True:
                    obj.save()
                    
        if(((i.fitness_certificate_expiry-today).days) <= 15 or ((i.fitness_certificate_expiry-today).days) == 30):
            if(((i.fitness_certificate_expiry-today).days) < 0):
                string = str(i)+" " + \
                    "fitness certificate has expired.Please renew it!!"
            else:
                string = str(i)+" "+"fitness certificate expires in:- " + \
                    str((i.fitness_certificate_expiry-today).days)+"days"
            noti[string] = i.truck_number
            if(len(Notifications.objects.filter(truck_number=i.truck_number, fitness_id=i.fitness_certificate_id, boolean=True)) == 0):
                obj, notif = Notifications.objects.get_or_create(
                    truck_number=i.truck_number, fitness_id=i.fitness_certificate_id, data=string)
                if notif is True:
                    obj.save()
