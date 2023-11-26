def bpcalc(systolic, diastolic):
    if 70 <= systolic < 90: 
        if 40 <= diastolic < 60:
            return('low')
        elif 60 <= diastolic < 80:
            return('ideal')
        elif 80 <= diastolic < 90:
            return('pre-high')
        elif 90 <= diastolic <= 100:
            return('high')
        else:
            return('invalid')
    elif 90 <= systolic < 120:
        if 40 <= diastolic < 80:
            return('ideal')
        elif 80 <= diastolic < 90:
            return('pre-high')
        elif 90 <= diastolic <= 100:
            return('high')
        else:
            return('invalid')
    elif 120 <= systolic < 140:
        if 40 <= diastolic < 90:
            return('pre-high')
        elif 90 <= diastolic <= 100:
            return('high')
        else:
            return('invalid')
    elif 140 <= systolic <= 190:
        if 40 <= diastolic <= 100:
            return('high')
        else:
            return('invalid')
    else:
        return('invalid')