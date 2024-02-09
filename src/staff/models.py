from flask_user import UserManager, UserMixin

from staff.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    AUTHY_STATUSES = (
        'unverified',
        'onetouch',
        'sms',
        'token',
        'approved',
        'denied'
    )

    # User authentication information (required for Flask-User)
    email = db.Column(db.Unicode(255), nullable=False, server_default=u'', unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0')
    profile = db.Column(db.Unicode(50), nullable=False, server_default=u'default')

    # User information
    first_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    last_name = db.Column(db.Unicode(50), nullable=False, server_default=u'')
    twofa_enabled = db.Column(db.Boolean(), nullable=False, server_default='0')
    country_code = db.Column(db.Integer)
    phone = db.Column(db.String(30))
    authy_id = db.Column(db.Integer)
    authy_status = db.Column(db.Enum(*AUTHY_STATUSES, name='authy_statuses'))
    failed_login_attempts = db.Column(db.Integer)

    # Address information
    address1 = db.Column(db.String(50))
    address2 = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    zipcode = db.Column(db.String(16))
    country = db.Column(db.String(50))

    # Relationships
    roles = db.relationship('Role', secondary='users_roles',
                            backref=db.backref('users', lazy='dynamic'))
    def has_role(self, role):
        for item in self.roles:
            if item.name == role:
                return True
        return False

    def role(self):
        for item in self.roles:
            return item.name

    def name(self):
        if self.first_name or self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.email

# Define the Role data model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(50), nullable = False, server_default = u'', unique = True)  # for @roles_accepted()
    label = db.Column(db.Unicode(255), server_default = u'')  # for display purposes


# Define the UserRoles association model
class UsersRoles(db.Model):
    __tablename__ = 'users_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))
