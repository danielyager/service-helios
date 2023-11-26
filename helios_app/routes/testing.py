from helios_app.routes import bpTest
from helios_app.models.user_account import UserAccount
from helios_app.extensions import db
import uuid
import datetime

@bpTest.route('/')
def index():
    return '<h1>Testing the home page!</h1>'

@bpTest.route('/hello-test/')
def hello_world_test():
    return '<h1>Hello, World!</h1>'

@bpTest.route('/create-user-test/')
def create_user_test():
    current_time = datetime.datetime.now()
    user = UserAccount(id=uuid.uuid4(),
                        first_name='John',
                        last_name='Glenn',
                        email='fakeemail@gmail.com',
                        email_confirmed=False,
                        password='password',
                        phone_number='5555555555',
                        phone_confirmed=False,
                        create_timestamp=current_time,
                        update_timestamp=current_time,
                        last_login=current_time)
    db.session.add(user)
    db.session.commit()
    return '<h1>Successfully Posted a New User!</h1>'