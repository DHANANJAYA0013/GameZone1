from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,timezone,timedelta
import hashlib, re
import pytz

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Dhananjaya/OneDrive/Desktop/GAmingWeb/website/instance/User.db'
app.config['SQLALCHEMY_BINDS'] = {
    'gamesession1': 'sqlite:///C:/Users/Dhananjaya/OneDrive/Desktop/GAmingWeb/website/instance/GameSession1.db',
    'gamesession2': 'sqlite:///C:/Users/Dhananjaya/OneDrive/Desktop/GAmingWeb/website/instance/GameSession2.db',
    'gamesession3': 'sqlite:///C:/Users/Dhananjaya/OneDrive/Desktop/GAmingWeb/website/instance/GameSession3.db',
    'gamesession4': 'sqlite:///C:/Users/Dhananjaya/OneDrive/Desktop/GAmingWeb/website/instance/GameSession4.db',
    'gamesession5': 'sqlite:///C:/Users/Dhananjaya/OneDrive/Desktop/GAmingWeb/website/instance/GameSession5.db',
    'gamesession6': 'sqlite:///C:/Users/Dhananjaya/OneDrive/Desktop/GAmingWeb/website/instance/GameSession6.db',
    'Feedback': 'sqlite:///C:/Users/Dhananjaya/OneDrive/Desktop/GAmingWeb/website/instance/Feedback.db'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)
    last_login = db.Column(db.DateTime)
    contact_number = db.Column(db.String(20), nullable=True) 


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    feedback = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Feedback {self.username}>'


class GameSession1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    login_time = db.Column(db.DateTime, default=datetime.now)
    total_time_spent = db.Column(db.Integer, nullable=False, default=0)  # Total time in seconds

    def __repr__(self):
        return f'<GameSession {self.username}, Time Spent {self.total_time_spent}>'

class GameSession2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_time_spent = db.Column(db.Integer, nullable=False, default=0)  # Total time in seconds

    def __repr__(self):
        return f'<GameSession {self.username}, Time Spent {self.total_time_spent}>'
    
class GameSession3(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_time_spent = db.Column(db.Integer, nullable=False, default=0)  # Total time in seconds

    def __repr__(self):
        return f'<GameSession {self.username}, Time Spent {self.total_time_spent}>'
    
class GameSession4(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_time_spent = db.Column(db.Integer, nullable=False, default=0)  # Total time in seconds

    def __repr__(self):
        return f'<GameSession {self.username}, Time Spent {self.total_time_spent}>'
    
class GameSession5(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_time_spent = db.Column(db.Integer, nullable=False, default=0)  # Total time in seconds

    def __repr__(self):
        return f'<GameSession {self.username}, Time Spent {self.total_time_spent}>'
    
class GameSession6(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), nullable=False)
    login_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total_time_spent = db.Column(db.Integer, nullable=False, default=0)  # Total time in seconds

    def __repr__(self):
        return f'<GameSession {self.username}, Time Spent {self.total_time_spent}>'




def create_db():
    with app.app_context():
        db.create_all()

create_db()

users = {'admin': 'password'}
# ADMIN_USERNAME = "admin"
# ADMIN_PASSWORD = "password"

@app.route('/admin')
def adminlog():
    return render_template('adminlog.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('admin'))
        else:
            return "Invalid credentials. Please try again."

@app.route('/details')
def admin():
    users = User.query.all()
    game_sessions1 = GameSession1.query.all()
    game_sessions2 = GameSession2.query.all()
    game_sessions3 = GameSession3.query.all()
    game_sessions4 = GameSession4.query.all()
    game_sessions5 = GameSession5.query.all()
    game_sessions6 = GameSession6.query.all()
    feedback=Feedback.query.all()
    return render_template('admin.html', users=users,game_sessions1=game_sessions1,game_sessions2=game_sessions2,game_sessions3=game_sessions3,game_sessions4=game_sessions4,game_sessions5=game_sessions5,game_sessions6=game_sessions6,feedback=feedback)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    db.drop_all()
    return "delete successful."

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    if 'user_email' in session:
        email = session['user_email']
        users = User.query.filter_by(email=email).first()
        if users:
            username = email.split('@')[0]  # Extract username dynamically
            username = re.sub(r'\d+', '', username) # remove digits
            return render_template('profile.html', users=users, username=username)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_email', None)
    return redirect(url_for('login'))

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        contact_number = request.form['contact-number']
        if not re.match(r'^\d{10}$', contact_number):
            return "Invalid contact number. It must be exactly 10 digits without any special characters." 

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Email already exists. Please choose a different one."

        hashed_password = hashlib.md5(password.encode()).hexdigest()[:10]
        username = email.split('@')[0]  # Extract username dynamically
        username = re.sub(r'\d+', '', username) # remove digits 
        new_user = User(email=email, password=hashed_password,contact_number=contact_number,username=username)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()
    if user and user.password == hashlib.md5(password.encode()).hexdigest()[:10]:
        user.last_login =datetime.now()
        db.session.commit()
        session['user_email'] = user.email
        return redirect(url_for('index'))
    else:
        return "Invalid email or password. Please try again."

@app.route('/puzzle')
def puzzle():
    if 'user_email' in session:
        email = session['user_email']
        user = User.query.filter_by(email=email).first()
        if user:
            session['username'] = re.sub(r'\d+', '', email.split('@')[0])

            session['login_time'] = datetime.now(timezone.utc)
            
            # Record login in GameSession
            game_session = GameSession1(username= re.sub(r'\d+', '', email.split('@')[0]), login_time=session['login_time'])
            db.session.add(game_session)
            db.session.commit()

            return render_template('puzzleG.html')
        else:
            return "Invalid credentials"

    return render_template('gamespage.html')
    

@app.route('/Gamelogout1')
def Gamelogout1():
    if 'username' in session:
        username = session['username']
        login_time = session['login_time']
        logout_time = datetime.now(timezone.utc)
        total_time_spent_seconds = logout_time - login_time
        total_time_spent=total_time_spent_seconds.total_seconds()
        # Update total time spent in GameSession
        game_session = GameSession1.query.filter_by(username=username).order_by(GameSession1.id.desc()).first()
        if game_session:
            game_session.total_time_spent += int(total_time_spent)
            db.session.commit()

        session.pop('username', None)
        session.pop('login_time', None)
    
    return redirect(url_for('games'))


@app.route('/word')
def word():
    if 'user_email' in session:
        email = session['user_email']
        user = User.query.filter_by(email=email).first()
        if user:
            session['username'] = re.sub(r'\d+', '', email.split('@')[0])
            session['login_time'] = datetime.now(timezone.utc)
            
            # Record login in GameSession
            game_session = GameSession2(username=re.sub(r'\d+', '', email.split('@')[0]), login_time=session['login_time'])
            db.session.add(game_session)
            db.session.commit()

            return render_template('wordG.html')
        else:
            return "Invalid credentials"

    return render_template('gamespage.html')

@app.route('/Gamelogout2')
def Gamelogout2():
    if 'username' in session:
        username = session['username']
        login_time = session['login_time']
        logout_time = datetime.now(timezone.utc)
        total_time_spent_seconds = logout_time - login_time
        total_time_spent=total_time_spent_seconds.total_seconds()
        # Update total time spent in GameSession
        game_session = GameSession2.query.filter_by(username=username).order_by(GameSession2.id.desc()).first()
        if game_session:
            game_session.total_time_spent += int(total_time_spent)
            db.session.commit()

        session.pop('username', None)
        session.pop('login_time', None)
    
    return redirect(url_for('games'))


@app.route('/tictak')
def tictak():
    if 'user_email' in session:
        email = session['user_email']
        user = User.query.filter_by(email=email).first()
        if user:
            session['username'] = re.sub(r'\d+', '', email.split('@')[0])
            session['login_time'] = datetime.now(timezone.utc)
            
            # Record login in GameSession
            game_session = GameSession3(username=re.sub(r'\d+', '', email.split('@')[0]), login_time=session['login_time'])
            db.session.add(game_session)
            db.session.commit()

            return render_template('tictak.html')
        else:
            return "Invalid credentials"

    return render_template('gamespage.html')

@app.route('/Gamelogout3')
def Gamelogout3():
    if 'username' in session:
        username = session['username']
        login_time = session['login_time']
        logout_time = datetime.now(timezone.utc)
        total_time_spent_seconds = logout_time - login_time
        total_time_spent=total_time_spent_seconds.total_seconds()
        # Update total time spent in GameSession
        game_session = GameSession3.query.filter_by(username=username).order_by(GameSession3.id.desc()).first()
        if game_session:
            game_session.total_time_spent += int(total_time_spent)
            db.session.commit()

        session.pop('username', None)
        session.pop('login_time', None)
    
    return redirect(url_for('games'))
    

@app.route('/2048')
def number():
    if 'user_email' in session:
        email = session['user_email']
        user = User.query.filter_by(email=email).first()
        if user:
            session['username'] = re.sub(r'\d+', '', email.split('@')[0])
            session['login_time'] = datetime.now(timezone.utc)
            
            # Record login in GameSession
            game_session = GameSession4(username=re.sub(r'\d+', '', email.split('@')[0]), login_time=session['login_time'])
            db.session.add(game_session)
            db.session.commit()

            return render_template('2048.html')
        else:
            return "Invalid credentials"

    return render_template('gamespage.html')

@app.route('/Gamelogout4')
def Gamelogout4():
    if 'username' in session:
        username = session['username']
        login_time = session['login_time']
        logout_time = datetime.now(timezone.utc)
        total_time_spent_seconds = logout_time - login_time
        total_time_spent=total_time_spent_seconds.total_seconds()
        # Update total time spent in GameSession
        game_session = GameSession4.query.filter_by(username=username).order_by(GameSession4.id.desc()).first()
        if game_session:
            game_session.total_time_spent += int(total_time_spent)
            db.session.commit()

        session.pop('username', None)
        session.pop('login_time', None)
    
    return redirect(url_for('games'))
    

@app.route('/tetris')
def tetris():
    if 'user_email' in session:
        email = session['user_email']
        user = User.query.filter_by(email=email).first()
        if user:
            session['username'] = re.sub(r'\d+', '', email.split('@')[0])
            session['login_time'] = datetime.now(timezone.utc)
            
            # Record login in GameSession
            game_session = GameSession5(username=re.sub(r'\d+', '', email.split('@')[0]), login_time=session['login_time'])
            db.session.add(game_session)
            db.session.commit()

            return render_template('tetris.html')
        else:
            return "Invalid credentials"

    return render_template('gamespage.html')

@app.route('/Gamelogout5')
def Gamelogout5():
    if 'username' in session:
        username = session['username']
        login_time = session['login_time']
        logout_time = datetime.now(timezone.utc)
        total_time_spent_seconds = logout_time - login_time
        total_time_spent=total_time_spent_seconds.total_seconds()
        # Update total time spent in GameSession
        game_session = GameSession5.query.filter_by(username=username).order_by(GameSession5.id.desc()).first()
        if game_session:
            game_session.total_time_spent += int(total_time_spent)
            db.session.commit()

        session.pop('username', None)
        session.pop('login_time', None)
    
    return redirect(url_for('games'))
    

@app.route('/sudoku')
def sudoku():
    if 'user_email' in session:
        email = session['user_email']
        user = User.query.filter_by(email=email).first()
        if user:
            session['username'] = re.sub(r'\d+', '', email.split('@')[0])
            session['login_time'] = datetime.now(timezone.utc)
            
            # Record login in GameSession
            game_session = GameSession6(username=re.sub(r'\d+', '', email.split('@')[0]), login_time=session['login_time'])
            db.session.add(game_session)
            db.session.commit()

            return render_template('sudoku.html')
        else:
            return "Invalid credentials"

    return render_template('gamespage.html')

@app.route('/Gamelogout6')
def Gamelogout6():
    if 'username' in session:
        username = session['username']
        login_time = session['login_time']
        logout_time = datetime.now(timezone.utc)
        total_time_spent_seconds = logout_time - login_time
        total_time_spent=total_time_spent_seconds.total_seconds()
        # Update total time spent in GameSession
        game_session = GameSession6.query.filter_by(username=username).order_by(GameSession6.id.desc()).first()
        if game_session:
            game_session.total_time_spent += int(total_time_spent)
            db.session.commit()

        session.pop('username', None)
        session.pop('login_time', None)
    
    return redirect(url_for('games'))
    

@app.route('/games')
def games():
    return render_template('gamespage.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/feedbacks')
def feedbacks():
    feedback=Feedback.query.all()
    return render_template('feedbacks.html',feedback=feedback)

@app.route('/submit_feedback', methods=['GET', 'POST'])
def submit_feedback():
    if request.method == 'POST':
        feedback = request.form['feedback']
        if 'user_email' in session:
            email = session['user_email']
            username= re.sub(r'\d+', '', email.split('@')[0])
            user = User.query.filter_by(email=email).first()
            if user:
                new_feedback = Feedback(username=username, email=email, feedback=feedback)
                db.session.add(new_feedback)
                db.session.commit()
                return redirect(url_for('feedback'))
        return redirect(url_for('index'))
    return render_template('feedback.html')
    


@app.template_filter('formatdatetime')
def format_datetime(value, format='%Y-%m-%d %H:%M:%S'):
    local_timezone = pytz.timezone('Asia/Kolkata')  # Indian Standard Time (IST)
    utc_dt = value.replace(tzinfo=timezone.utc)
    local_dt = utc_dt.astimezone(local_timezone)
    return local_dt.strftime(format)

if __name__ == '__main__':
    app.run(debug=True)
