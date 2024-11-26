import phonenumbers
from phonenumbers import carrier, geocoder

def track_phone_number(phone_number):
    try:
        # Parse the phone number
        phone = phonenumbers.parse(phone_number)
        
        # Basic information
        print(f"Country Code: +{phone.country_code}")
        print(f"National Number: {phone.national_number}")
        
        # Carrier information
        carrier_name = carrier.name_for_number(phone, 'en')
        if carrier_name:
            print(f"Carrier: {carrier_name}")
        else:
            print("Carrier information not available")
        
        # Geographical information (Country)
        country = geocoder.description_for_number(phone, 'en')
        if country:
            print(f"Country: {country}")
        else:
            print("Country information not available")
        
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    phone_number = input("Enter phone number to track (with country code, e.g., +254xxxxxxxxx): ")
    track_phone_number(phone_number)
