import gspread as gs
credentials = {
    "type": "service_account",
    "project_id": "dj001-328314",
    "private_key_id": "d00112549798508f8f0e0d489055dc73b4a5ae58",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDFpjnJE9ADF8S1\nAG7BblYd9P8yQYdRpjsSg2orq5+X4d+dVuXFzD6rXOiMW+8vpflJ44dBnAaKNLva\nU1hg2AZIGmQ+nL67bzi0QLXQTzc+hmmAUSpmlZGSpspMZQpEDNprgFzvNGsrVkeE\n2UTESXkI8bioJRouSrnEdyvWewURFfQ4aRlEhTB7kM5brqeUIR9TPyiETJG2bZgI\nc3aRhCBVhlVhx02B6KPiMAlpzxbMjN82S4Max+GezLCijoirP7LvuuPUvFrvKWSL\nDLXRSUP12l2Ae6RvK5u1YdkTefDnRdKHdo6YpXObsEb/acB2dpqTWmtSZoXw71NQ\nMYJ4yDRHAgMBAAECggEAFoMC1Oi5Sgjkgjss4kI3c80KXgaBq6aT1t1588Rl9o4n\nAow5uogzYSBBam80NIiidqyAJNRpGEe+V7UjfVBNktvSrCD9Rmr6Gem+652CLNBx\nZsiX3DxP6tStePsPKsYOAK2LqEEfrb1zgumeP/8gVoj1n80uCLTBKOPr7c9wOcxD\nLtNTNgJdPLaYu5njzAyHH7ckfLf8GhX1NNBRPwQ6lYVFVbPnnD+OmZmkyO6Zrxbt\n7mrEtNS8wblehr7YNqIChQg4Nbf6KTQhPRSZ93cP5IBPvxf0enTqZ4ibp8RfKV9V\neLCfdKnDbiu9N+flN2aq5wEWVJirmU0f1pBidE6f/QKBgQD/hX58bdNptKfpLZ1x\nCTQ6/5ySe4HIMG8dnrToMaFgDkL9y0qyRavYWFj7dJfb+0dQI1CzFq3GELYI4n4o\nmYs8ZlNq3N+oH6gEbQhRH6NOEwSZIBwFn2hTfIBEoqqeXZ4K9RAXVzlgyAoOLreC\nMbQdkX6KTt5vWyllzSK4SlgInQKBgQDGBPxXnlgVuRO/4Grqt5EyToQSuJNWVsi1\nrw4aV0Lg3itBIAVz12ts3B/ITP/a/SYteVQLr+QSYdwjZjsb7Khv6o48SL303/3a\nguLeIfLOCEdltN8CVzM19iQxVJnKER+YyrF/8JAHgu27cUPBbBVsBmdHhGool1w5\nSCFTcXdhMwKBgQCOK0hlEvY+KjYCl06yRdy5tt724aEkMU6hvFwLlRGk0EqVyzaU\nWg9zIDTiM80KqJTVEdEk08l8GnAuIVbwX/4IbSacnqgScwqY69Fk0aWbGxnD2Qm+\nVyNE0FDN33PvCUeV8SQy2GUkZCi0G2ofFmiQyxMNATTh4Gb4LVrUDwlMQQKBgQC7\nuapInlK/dU/lzalOj2xVFt5aqST06x0oMKbcDfHXIIg9G1BP+99Zum1fBLBiOS/i\nWG13Du7XBnMeFCLhXEBqqSDiwctjxJ3yc7cEA4ceD/cv0oLAw05HT+wL4DpTuFwO\nC8quka7ZkCQ0WTJ0wjSkzoVG5Z+Gj8fcficp5h3YxQKBgQDyGcRTjLUgC0FkDDp6\nI6OMn2MpKJ75idbKC0cYEzZx06i3TAKH2WwsK6qnOzYXOUbGOJRvaxrFr6I1vgU6\npM5LxyhpNp+NKxz73CUYeaSgnyz2WteA+Yvd6tmw8rf8bTsL6XVQ+ereqS20CiGw\noBb8xWKo4+eXNk/TAmpxD4Shsg==\n-----END PRIVATE KEY-----\n",
    "client_email": "dj001-554@dj001-328314.iam.gserviceaccount.com",
    "client_id": "108226103335567990988",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/dj001-554%40dj001-328314.iam.gserviceaccount.com"
}
def get_access(sheetid):
    sheetId = sheetid
    project = gs.service_account_from_dict(credentials)
    sheet = project.open_by_key(sheetId)
    data = sheet.worksheet("data")
    
    return data