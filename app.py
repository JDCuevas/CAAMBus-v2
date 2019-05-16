from flask import Flask, request, render_template, flash, redirect, url_for, session, logging
from functools import wraps
from passlib.hash import sha256_crypt
from forms import RegisterForm, LoginForm, ItineraryForm
from ApplicationLayer.userHandler import UserHandler
from ApplicationLayer.driverHandler import DriverHandler
from ApplicationLayer.routeHandler import RouteHandler
from ApplicationLayer.trolleyHandler import TrolleyHandler
from ApplicationLayer.itineraryHandler import ItineraryHandler

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'caambus'

# Check if user is logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, please log in.', 'danger')
            return redirect(url_for('login'))

    return wrap

def is_admin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session['admin']:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, must be admin.', 'danger')
            return redirect(url_for('home'))

    return wrap

# Home
@app.route('/')
def home():
    return render_template('home.html')

###################### Users ######################

# User Register
@app.route('/register', methods=['GET', 'POST'])
@is_logged_in
@is_admin
def register():
    handler = UserHandler()
    form = RegisterForm(request.form) 

    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        phone = form.phone.data
        admin = form.user_type.data
        license = form.license.data

        handler.register(username, password, first_name, last_name, phone, admin, license)

        flash(username + 'is now registered and can log in', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', form=form)    

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    handler = UserHandler()
    form = LoginForm(request.form) 

    if request.method == 'POST':
        # Get form fields
        username = form.username.data
        password_candidate = form.password.data

        user = handler.getUserByUsername(username)

        if user:
            # Get stored hash
            password = user['password']

            # Compare passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = user['username']
                session['user_id'] = user['user_id']
                session['admin'] = (user['admin'] == True)

                flash('You are now logged in.', 'success')
                return redirect(url_for('home'))
            else:
                error = 'Invalid login.'
            return render_template('login.html', form=form, error=error)
        else:
            error = 'Username not found.'
            return render_template('login.html', form=form, error=error)

    return render_template('login.html', form=form)

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash("You are now logged out.", "success")
    return redirect(url_for('login'))

###################### Drivers ######################

@app.route('/CAAMBus/drivers', methods=['GET'])
def drivers():
    drivers = DriverHandler().getAllDrivers()

    if drivers:
    	return render_template('drivers.html', drivers=drivers)

    msg="No Drivers Found"
    return render_template('drivers.html', msg=msg)

###################### Trolleys ######################

@app.route('/CAAMBus/trolleys', methods=['GET'])
def trolleys():
    trolleys = TrolleyHandler().getAllTrolleys()

    if trolleys:
        return render_template('trolleys.html', trolleys=trolleys)

    msg="No Trolleys Found"
    return render_template('trolleys.html', msg=msg)

@app.route('/CAAMBus/trolleys/add', methods=['GET', 'POST'])
@is_logged_in
@is_admin
def add_trolley():
    if request.method == 'POST':
        form = request.form
        plate = form['plate']
        capacity = form['capacity']
        mileage = form['mileage']

        trolley = TrolleyHandler().registerTrolley(plate, capacity, mileage)

        if trolley:
            flash('Trolley Added', 'success')
            return redirect(url_for('trolleys'))

    msg="Method Not Allowed"
    return render_template('trolleys.html', msg=msg)

@app.route('/CAAMBus/trolleys/delete/<int:trolley_id>', methods=['GET'])
@is_logged_in
@is_admin
def delete_trolley(trolley_id):
    trolley_id = TrolleyHandler().deleteTrolley(trolley_id)

    if trolley_id:
        flash('Trolley Deleted', 'success')
        return redirect(url_for('trolleys'))

    msg="No Trolley Found"
    return render_template('trolleys.html', msg=msg)

###################### Routes ######################

@app.route('/CAAMBus/routes', methods=['GET'])
def routes():
    routes = RouteHandler().getAllRoutes()

    if routes:
    	return render_template('routes.html', routes=routes)

    msg="No Routes Found"
    return render_template('routes.html', msg=msg)

@app.route('/CAAMBus/routes/create', methods=['GET', 'POST'])
@is_logged_in
@is_admin
def create_route():
    if request.method == 'POST':
        form = request.form
        route_name = form['route_name']

        route = RouteHandler().createRoute(route_name)

        if route:
            flash('Route Created', 'success')
            return redirect(url_for('routes'))

    msg="Method Not Allowed"
    return render_template('routes.html', msg=msg)

@app.route('/CAAMBus/routes/delete/<int:route_id>', methods=['GET'])
@is_logged_in
@is_admin
def delete_route(route_id):
    route_id = RouteHandler().deleteRoute(route_id)

    if route_id:
        flash('Route Deleted', 'success')
        return redirect(url_for('routes'))

    msg="No Route Found"
    return render_template('routes.html', msg=msg)

###################### Stops ######################

@app.route('/CAAMBus/routes/<int:route_id>/add/<int:stop_id>', methods=['GET', 'POST'])
@is_logged_in
@is_admin
def add_stop(route_id, stop_id):
    stop = RouteHandler().add_stop(route_id, stop_id)

    if stop:
        flash('Stop Added', 'success')
        return redirect(url_for('stops', route_id=route_id))

    flash('Stop Not Added', 'warning')
    return redirect(url_for('stops', route_id=route_id))

@app.route('/CAAMBus/routes/<int:route_id>/remove/<int:stop_id>', methods=['GET', 'POST'])
@is_logged_in
@is_admin
def remove_stop(route_id, stop_id):
    stop = RouteHandler().remove_stop(route_id, stop_id)

    if stop:
        flash('Stop Removed', 'success')
        return redirect(url_for('stops', route_id=route_id))

    flash('Stop Not Removed', 'warning')
    return redirect(url_for('stops', route_id=route_id))

@app.route('/CAAMBus/stops/<int:route_id>', methods=['GET'])
def stops(route_id):
    route_stops = RouteHandler().getRouteStops(route_id)
    all_stops = RouteHandler().getStopsNotInRoute(route_id)

    if stops:
    	return render_template('stops.html', stops=route_stops, allStops=all_stops, route_id=route_id)

    msg="No Stops Found"
    return render_template('stops.html', msg=msg)

###################### Stops ######################

@app.route('/CAAMBus/itineraries', methods=['GET'])
def itineraries():
    itineraries = ItineraryHandler().getAllItineraries()
    print(itineraries)
    if itineraries:
        return render_template('itineraries.html', itineraries=itineraries)

    msg="No Itineraries Found"
    return render_template('itineraries.html', msg=msg)

@app.route('/CAAMBus/itineraries/create', methods=['GET', 'POST'])
@is_logged_in
@is_admin
def create_itinerary():
    form = ItineraryForm(request.form)
    form.driver_id.choices = [(driver['driver_id'], driver['name']) for driver in DriverHandler().getAllDrivers()]
    form.trolley_id.choices = [(trolley['trolley_id'], trolley['plate']) for trolley in TrolleyHandler().getAllTrolleys()]
    form.route_id.choices = [(route['route_id'], route['route_name']) for route in RouteHandler().getAllRoutes()]

    if request.method == 'POST':
        date = form.date.data
        start_time = form.start_time.data
        end_time = form.end_time.data
        driver_id = form.driver_id.data
        trolley_id = form.trolley_id.data
        route_id = form.route_id.data

        print(date)
        print(start_time)
        print(end_time)
        print(driver_id)
        print(trolley_id)
        print(route_id)
        itinerary = ItineraryHandler().createItinerary(date, start_time, end_time, driver_id, trolley_id, route_id)

        if itinerary:
            flash('Itinerary Created', 'success')
            return redirect(url_for('itineraries'))

    elif request.method == 'GET':
        return render_template('create_itinerary.html', form=form)

    msg="Method Not Allowed"
    return render_template('create_itinerary.html', msg=msg)

@app.route('/CAAMBus/itineraries/delete/<int:itinerary_id>', methods=['GET'])
@is_logged_in
@is_admin
def delete_itinerary(itinerary_id):
    itinerary_id = ItineraryHandler().deleteItinerary(itinerary_id)

    if itinerary_id:
        flash('Itinerary Deleted', 'success')
        return redirect(url_for('itineraries'))

    msg="No Itinerary Found"
    return render_template('itineraries.html', msg=msg)

if __name__ == '__main__':
	app.run()