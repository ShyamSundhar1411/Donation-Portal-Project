


BLOOD_MATCHING_TYPES=[
    ("A +ve","A +ve,AB +ve"),
    ("O +ve","O +ve,A +ve,;B +ve,AB +ve"),
    ("B +ve",";B +ve,AB +ve"),
    ("AB +ve","AB +ve"),
    ("A -ve","A +ve,A -ve,AB -ve,AB +ve"),
    ("O -ve","A +ve,A -ve,O -ve,O +ve,AB +ve,AB -ve,;B +ve,;B -ve"),
    ("B -ve",";B +ve,;B -ve,AB -ve,AB +ve"),
    ("AB -ve","AB +ve,AB -ve"), 
]

def find_compatible_match(blood_type):
    for i in BLOOD_MATCHING_TYPES:
        if i[0] == blood_type:
            return i[-1]

def is_authorized(user):
    status = False
    if user.donor.role == "Admin" or user.is_superuser:
        status = True
    return status