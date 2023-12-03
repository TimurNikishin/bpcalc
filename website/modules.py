def bpcalc(systolic, diastolic):
    if 70 <= systolic < 90 and 40 <= diastolic < 60:
        return 'low'
    elif 70 <= systolic < 90 and 60 <= diastolic < 80:
        return 'ideal'
    elif 70 <= systolic < 90 and 80 <= diastolic < 90:
        return 'pre-high'
    elif 70 <= systolic < 90 and 90 <= diastolic <= 100:
        return 'high'
    elif 90 <= systolic < 120 and 40 <= diastolic < 80:
        return 'ideal'
    elif 90 <= systolic < 120 and 80 <= diastolic < 90:
        return 'pre-high'
    elif 90 <= systolic < 120 and 90 <= diastolic <= 100:
        return 'high'
    elif 120 <= systolic < 140 and 40 <= diastolic < 90:
        return 'pre-high'
    elif 120 <= systolic < 140 and 90 <= diastolic <= 100:
        return 'high'
    elif 140 <= systolic <= 190 and 40 <= diastolic <= 100:
        return 'high'
    else:
        return 'invalid'