def insurance_expiry(details):
    for i in details:
        # print(specific_detail)
        year = (i.insurance_expiry).year
        day = (i.insurance_expiry).day
        month = i.insurance_expiry.strftime("%b")
    string = str(str(month)+","+str(day)+","+str(year))
    return string


def fitness_certificate_expiry(details):
    for i in details:
        # print(specific_detail)
        year1 = (i.fitness_certificate_expiry).year
        day1 = (i.fitness_certificate_expiry).day
        month1 = (i.fitness_certificate_expiry).strftime("%b")
    nextstring = str(str(month1)+","+str(day1)+","+str(year1))
    return nextstring
