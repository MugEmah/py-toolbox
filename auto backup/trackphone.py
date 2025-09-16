import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+256758602343")
phone_number2 = phonenumbers.parse("+256780351918")
phone_number3 = phonenumbers.parse("+256755004133")
phone_number4 = phonenumbers.parse("+256772684447")

print("\nPhone number Location\n")

print(geocoder.description_for_number(phone_number1, "en"));
print(geocoder.description_for_number(phone_number2, "en"));
print(geocoder.description_for_number(phone_number3, "en"));
print(geocoder.description_for_number(phone_number4, "en"));

#LETS TRACK PHONE NUMBERS
