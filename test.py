import os

STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET')
print(STRIPE_PUBLIC_KEY)
print(STRIPE_SECRET_KEY)
print(STRIPE_WH_SECRET)