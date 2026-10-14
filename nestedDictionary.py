customer = {
    "Name": "Sathish",
    "EmailID": ["satish@gmail.com","sathish13@gmail.com"],
    "mobileNumber": 312312,
    "address": {
        "state": "TN",
        "City": "Chennai",
        "coordinates": {
            "lat": 20.001,
            "lng": 34.2232
        }
    }
}

print(customer["EmailID"])
print(customer["address"]["City"])
print(customer["address"]["coordinates"]["lat"])
print(customer["EmailID"][1])

print(customer["EmailID"].append("sathish313@gmail.com"))

print(customer)