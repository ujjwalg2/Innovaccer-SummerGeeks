# Innovaccer-SummerGeeks

This project is made to complete the Innovaccer Summer Intern Hiring challenge. The project is hosted on https://entry-management.herokuapp.com/

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip3 install -r requirements.txt
```

You'll need to update your database details in `settings.py` - 
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

Then you'll have to update the email host user and password in `settings.py` -
```py
EMAIL_HOST_USER = 'email_id@host.com'
EMAIL_HOST_PASSWORD = 'your password'
```

And finally, update the twilio SID and token in `settings.py` so that sms function works properly -
```py
TWILIO_ACCOUNT_SID = 'your sid'
TWILIO_AUTH_TOKEN = 'your token'
```

## Usage

You can use the product at https://entry-management.herokuapp.com/
- To register as a host, click on `HOST` in navbar and fill the info correctly.
- To check in as a visitor, click on `CHECK IN` in the navbar and fill the details. Once the visitor fills his/her details, a mail and a sms is sent out to the host.
- To check out as a visitor, click on `CHECK OUT` in the navbar and fill the email and contact info. Once the visitor checks out, a mail is sent out to the visitor with details of his visit.
