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
        
        from .modules import bpcalc
        pressure = bpcalc(systolic, diastolic)
        
        if pressure == 'low':
            flash('Low blood pressure', category='low')
        elif pressure == 'ideal':
            flash('Ideal blood pressure', category='ideal')
        elif pressure == 'pre-high':
            flash('Pre-High blood pressure', category='pre-high')
        elif pressure == 'high':
            flash('High blood pressure', category='high')
            
    return render_template("home.html")

