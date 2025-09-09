Database Structure & Data Models
================================

Data Models
-----------

Address
~~~~~~~
- **street**: CharField (255 chars)
- **city**: CharField (64 chars)
- **state**: CharField (2 chars, US states)
- **zip_code**: CharField (5 chars)
- **country**: CharField (64 chars)

Letting
~~~~~~~
- **title**: CharField (256 chars)
- **address**: OneToOneField to Address

Profile
~~~~~~~
- **user**: OneToOneField to User
- **favorite_city**: CharField (64 chars, blank=True)
