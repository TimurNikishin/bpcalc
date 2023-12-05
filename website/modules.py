from datetime import datetime

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

def log_inputs(*inputs, file_path='log.txt'):
    # Get the current date and time
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Format and log all inputs on a single line
    log_entry = f'{current_datetime}: {" ".join(map(str, inputs))}\n'

    # Write the log entry to the file
    with open(file_path, 'a') as file:
        file.write(log_entry)
        
def read_data_from_file(file_path='log.txt'):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "No logs found."