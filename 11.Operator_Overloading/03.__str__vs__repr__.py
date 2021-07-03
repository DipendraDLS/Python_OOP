'''
The goal of __repr__ is to be unambiguous.
The goal of __str__ is to be readable.

'''

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
b = str(a)

print ('str(a): {}'.format(str(a)))
print ('str(b): {}'.format(str(b)))

print("\n")

# repr() is used for unambiguous developer haruko lagi use huncha ra testo readable format ma ni aundaina but str() chai readable format ma auncha ani normal userko lagi sajilo ho.
print ('repr(a): {}'.format(repr(a)))
print ('repr(b): {}'.format(repr(b)))

print("\n")
