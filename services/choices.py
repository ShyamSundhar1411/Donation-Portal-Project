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
State_Choices = [("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry")]

APPROVAL_STATUS=[
    ("Pending","Pending"),
    ("Rejected","Rejected"),
    ("Approved","Approved"),
    ("Completed","Completed"),
]

REQUEST_STATUS=[
    ("Pending","Pending"),
    ("Completed","Completed"),
]