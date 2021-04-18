import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
print('''

  _   _                 _                 _                     
 | \ | |               | |               | |                    
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |     ___   ___ __ _ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | |    / _ \ / __/ _` |
 | |\  | |_| | | | | | | |_) |  __/ |    | |___| (_) | (_| (_| |
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|    |______\___/ \___\__,_|
                                                                
                                                                
''')
print('format: +3311111111')                                                                
number_tel = input('Entrez le numéro: ')
print()
print('-----------------------------------------')
print('Information from Number ', number_tel,' !')
contry_number = phonenumbers.parse(number_tel)
print(geocoder.description_for_number(contry_number, 'fr'))

service_number = phonenumbers.parse(number_tel)
print(carrier.name_for_number(service_number, 'fr'))
print('-----------------------------------------')