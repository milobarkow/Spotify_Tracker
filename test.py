#https://accounts.spotify.com/authorize?client_id=7a9404710e8b4fcea7f0e5634f000c96&scope=playlist-read-private&redirect_uri=http://localhost:8888/callback&response_type=code
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
# account_credentials = {
#   "type": "service_account",
#   "project_id": "spotify-298001",
#   "private_key_id": "a37c938d0504199768ba45365e7edcaaaf263cbb",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCrPt9kvN36X4BV\nxiDnKdhFmlhMdjJK3pnceUlmgXm6bg2XeGW/bW5XRwAgedXc/wGS2uaEYkQ+0XzX\nzL6gQA92OIEZwyn0+4dlheOD8JuKg4Klguy7orw1u6OTjC2qGw3+XCSECR16V3rI\nxahnUk4pSLRWHmSpbaj0qyu8v1KYpfeNsY2yF6tjutNUeBv0H3zO2MP0L45buBq7\nCFsCPVHY/DBoJ16vqL7bjifII65UiO6zR6u0d7CSfmyiy3Pp028VhZfHyMLkVwB4\ngty0dEFYVAg/AnFyhRgVbNzAz7rZZQf+DSRelCqoAOLSKxCl9XJsOVyQQLicCX04\nAUXo+e4VAgMBAAECggEAPEE/MZ8TLEn2SjgQ08Xxh2wrrZvZTmbNFLrIjPz57BNV\nTPrcMmM69BLThJnaGozP7PCBNAuvn7ruhrBQUuq3hg2Tv5DgbociuSJHT+GVmUN0\n8PAEhHFacD257OziFHy4i8u4PY1HhgjJ92M1QkW/ot8mNTc0jDk9vfmMxjk7wuHv\njCq4Gepzy5ZejaVwgF1Zt1+A8bki0bKJ/Q5/xNLBBOf1G7IKocc1hl+EbTXiqldH\noi4CKena1zY0c2W1UFTIDMAmY9Lzt6+HM/qnKefUsjm8CHN5iyuFg5NV0X6b2sW5\nyc7YstsqVRVz0Q1/ClboKAUMP+JpHt5j/uZ6lvzY8QKBgQDdJVwzoSIdOfNaEdK3\noCNCobVwXno+KBQQEtpYavWuc3OgtOfQxkMhOWTiliQcVqjvWGyBT0q3RT6Fm8IM\nrdLW2IksWMYYAi7laUIUL91DpXcvhDCWcoao08hC4lOxTyQPGIl7kWPyPiUQMENH\nWgKAPdMddxVUT7udBUvzarLnBwKBgQDGPCs1KGvsJdjyIg1d3oLXw8stYdGuwTxy\nN0tlzR2+OLeQl5fDVYE+dDvjwrxismhj9mRJhk1hu4rRpoTMooMkz2837E8YW+0O\n5did1nDoAXqBwj2x++WPSHjYhD87CYxHRzNBwsyEFBGh+uy23ru4xr4fbTNI7gkx\nRNfDwaW/AwKBgG7A5TpeOq2UdlHnlzarlr0qK6pJRsOWYuXh60RY3Q4vd/tGXsrq\nYHhlPCdWtmMS66xjBoSEZ5D9tuBHL5oV+//pllmFZEBl54KxgoyFpDTay6QaehL+\n7H3lAuisXOnyDscYrNIb8IhDo2BGK4uygoojbHXXS/FbtURggLc5+rtFAoGBALnQ\ntpOacyclBulYf/0IUM9dKTs94OWVHkrVh+hBz2p6EZ8IaepgYMig/W5uIFXHc9CX\nqcO9jxVYTTRdiUej4ZgElPTvnehwapI3Ysf4tVbT4/hzkY8fVjvrq9MQi5CUT5iU\npfgzV69KfIjAA1kbCQ2XxakBnDv1XEqBhFprTyjvAoGAU49ic4T1zWMHwAGSqMMV\nJQvXXG1uSFJkRdfd78LV0zTatACFV4/Dp8w4ANT2KkWhadUuTEiR3B1C+NjRRLXS\nTZRJ/W0ua33f4lhwPKuqM940rdL0/G4jkC8j7Qs4o0U9gzB3FfrLHtN+hQohuByS\nLV3QGUkLrgeTU/bq0vZFZz0=\n-----END PRIVATE KEY-----\n",
#   "client_email": "playlist@spotify-298001.iam.gserviceaccount.com",
#   "client_id": "105016417345840723075",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/playlist%40spotify-298001.iam.gserviceaccount.com"
# }


credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/12158/client_secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.open('https://docs.google.com/spreadsheets/d/10IfZeWRpzfYpbaJ236dgy-r_jNTPRhUe5E4MvPbDKYU/edit#gid=1080567132')

# with open('final.csv', 'r') as file_obj:
#     content = file_obj.read()
#     client.import_csv(spreadsheet.id, data=content)