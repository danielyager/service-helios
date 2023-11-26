from helios_app.routes import bpAccount
from helios_app.models.user_account import UserAccount
from helios_app.extensions import db
import uuid
from flask import request
import datetime

@bpAccount.route('/create-user/', methods=['POST'])
def create_user():
    request_data = request.get_json()
    request_email = request_data['email']
    request_password = request_data['password']
    user_id = uuid.uuid4()
    
    user = db.session.execute(db.select(UserAccount).filter_by(email=request_email)).first()

    if (user == None):
        current_time = datetime.datetime.now()
        user = UserAccount(id=user_id,
                            email=request_email,
                            email_confirmed=False,
                            password=request_password,
                            create_timestamp=current_time,
                            update_timestamp=current_time,
                            last_login=current_time)
        db.session.add(user)
        db.session.commit()
        return f'Created User with id={user_id} and email={request_email}', 200
    else:
        return f'User with email {request_email} already exists!', 400