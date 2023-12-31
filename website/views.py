from flask import Blueprint, render_template, request, flash

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        systolic = request.form.get('systolic')
        diastolic = request.form.get('diastolic')
        try:
            systolic = int(systolic)
            diastolic = int(diastolic)
        except ValueError:
            flash('Values must be numbers', category='error')
        
        from .modules import bpcalc, log_inputs
        pressure = bpcalc(systolic, diastolic)
        log_inputs(pressure, systolic, diastolic)
        
        if pressure == 'low':
            flash('Low blood pressure', category='low')
        elif pressure == 'ideal':
            flash('Ideal blood pressure', category='ideal')
        elif pressure == 'pre-high':
            flash('Pre-High blood pressure', category='pre-high')
        elif pressure == 'high':
            flash('High blood pressure', category='high')
        elif pressure == 'invalid':
            flash('Submitted invalid values', category='high')
            
    return render_template("home.html")

@views.route('/logs')
def logs():
    from .modules import read_data_from_file
    log_data = read_data_from_file()
    return render_template("logs.html", log_data=log_data)