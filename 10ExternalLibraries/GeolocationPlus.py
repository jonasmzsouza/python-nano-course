from pygeocoder import Geocoder

address = input("Enter an address. Ex.: Avenida Paulista, 100 São Paulo:")
result = Geocoder('Place_your_API_key_here').geocode(address)

if result.valid_address:
    print("Address...........: ", result)
    print("Coordinates.......: ", result.coordinates)
    print("Number............: ", result.street_number)
    print("Postal Code.......: ", result.postal_code)

print(result.count, "address found.")
for r in result:
    print("City......: ", r.state)
    print("Country........: ", r.country)
    print("Street name..: ", r.route)
    print(".....................................")

