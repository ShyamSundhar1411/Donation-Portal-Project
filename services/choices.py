BLOOD_CHOICES=[
    ('O +ve', 'O +ve'),
    ('O -ve','O -ve',),
    ('A +ve', 'A +ve',),
    ('A -ve', 'A -ve',),
    ('B +ve','B +ve',),
    ('B -ve','B -ve',),
    ('AB +ve','AB +ve'),
    ('AB -ve', 'AB -ve')]
ROLE_CHOICES = [
    ("Admin","Admin"),
    ("Donor","Donor"),
    ("Unauthorized", "Unauthorized"),
]
COMPATIBLE_TYPES=[
    ("A +ve,AB +ve","A +ve,AB +ve"),
    ("O +ve,A +ve,;B +ve,AB +ve","O +ve,A +ve,B +ve,AB +ve"),
    (";B +ve,AB +ve","B +ve,AB +ve"),
    ("AB +ve","AB +ve"),
    ("A +ve,A -ve,AB -ve,AB +ve","A +ve,A -ve,AB -ve,AB +ve"),
    ("A +ve,A -ve,O -ve,O +ve,AB +ve,AB -ve,;B +ve,;B -ve","A +ve,A -ve,O -ve,O +ve,AB +ve,AB -ve,B +ve,B -ve"),
    (";B +ve,;B -ve,AB -ve,AB +ve","B +ve,B -ve,AB -ve,AB +ve"),
    ("AB +ve,AB -ve","AB +ve,AB -ve"), 
]