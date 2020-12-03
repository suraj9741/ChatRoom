

from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_socketio import SocketIO, join_room, leave_room

from database import get_user, check_user

app = Flask(__name__)
# declare secret key
app.secret_key = "1234"
# creating object of socketio and its create web sockets of app
socketio = SocketIO(app)
# create object od login manager of flask-login
login_manager = LoginManager()
# creating login view
login_manager.login_view = 'login'
login_manager.init_app(app)

@app.route('/')
@login_required
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():

    message = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password_input = request.form.get('password')
        user = get_user(email)
        print(user)
        if check_user(email, password_input):
            print('TTTTTTT')
            login_user(user)
            return redirect(url_for('home'))
        else:
            print('FFFFFFF')
            message = 'Failed to login!'
    return render_template('login.html', message=message)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/chat')
@login_required
def chat():
    # request.args is library that contain url and data
    username = request.args.get('username')
    room = request.args.get('room')

    if username and room:
        return render_template('chat.html', username=username, room=room)
    else:
        return redirect(url_for('home'))


@socketio.on('join_room')
def handle_join_room_event(data):
    app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_announcement', data, room=data['room'])


@socketio.on('send_message')
def handle_send_message_event(data):
    app.logger.info("{} has sent message to the room {}: {}".format(data['username'], data['room'], data['message']))
    socketio.emit('receive_message', data, room=data['room'])


@socketio.on('leave_room')
def handle_leave_room_event(data):
    app.logger.info("{} has left the room {}".format(data['username'], data['room']))
    leave_room(data['room'])
    socketio.emit('leave_room_announcement', data, room=data['room'])

@login_manager.user_loader
def load_user(name):
    return get_user(name)

if __name__ == '__main__':
    socketio.run(app, debug=True)