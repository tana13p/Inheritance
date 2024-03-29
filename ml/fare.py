from flask import Flask, request, jsonify

#Bus Fare
class BusFareCalculator:
    def __init__(self, distance, fare_type='regular'):
        self.distance = distance
        self.fare_type = fare_type.lower()

    def calculate_fare(self):
        base_fare = 2.75  
        additional_fare_per_mile = 0.55  
        if self.fare_type == 'regular':
            fare = base_fare + additional_fare_per_mile * self.distance
        elif self.fare_type == 'student':
            fare = base_fare * 0.8 + additional_fare_per_mile * self.distance
        elif self.fare_type == 'senior':
            fare = base_fare * 0.5 + additional_fare_per_mile * self.distance
        else:
            raise ValueError("Invalid fare type. Available types: regular, student, senior")

        return round(fare, 2)


#CitiBike Fare
class CitiBikeFareCalculator:
    def __init__(self, membership_type, usage_time_minutes):
        self.membership_type = membership_type.lower()
        self.usage_time_minutes = usage_time_minutes

    def calculate_fare(self):

        membership_fees = {
            'single_ride': 4.95,
            'day_pass': 12.95,
            'monthly_membership': 24.95,  
            'annual_membership': 179.00  
        }

        free_time = {
            'single_ride': 0,
            'day_pass': 30,
            'monthly_membership': 45,
            'annual_membership': 45
        }

        base_fee = membership_fees.get(self.membership_type, 0.0)
        additional_fee_per_minute = max(0, self.usage_time_minutes - free_time.get(self.membership_type, 0)) * 0.18
        fare = base_fee + additional_fee_per_minute

        return round(fare, 2)


#Ferry Fare
class FerryFareCalculator:
    def __init__(self, distance, service_type='standard', fare_type='regular'):
        self.distance = distance
        self.service_type = service_type.lower()
        self.fare_type = fare_type.lower()

    def calculate_fare(self):
        base_fare = 10.00  
        additional_fare_per_mile = 1.50  

        if self.service_type == 'standard':
            additional_fare_per_mile = 1.50  
        elif self.service_type == 'express':
            additional_fare_per_mile = 2.50  
        else:
            raise ValueError("Invalid ferry service type. Available types: standard, express")

        if self.fare_type == 'regular':
            fare = base_fare + additional_fare_per_mile * self.distance
        elif self.fare_type == 'child':
            fare = base_fare * 0.75 + additional_fare_per_mile * self.distance 
        else:
            raise ValueError("Invalid fare type. Available types: regular, child")

        return round(fare, 2)


#Rail Fare
class RailFareCalculator:
    def __init__(self, distance, service_type='commuter', fare_type='regular'):
        self.distance = distance
        self.service_type = service_type.lower()
        self.fare_type = fare_type.lower()

    def calculate_fare(self):
        base_fare = 5.00
        additional_fare_per_mile = 0.75  
        if self.service_type == 'commuter':
            additional_fare_per_mile = 0.75
        elif self.service_type == 'express':
            additional_fare_per_mile = 1.25  
        else:
            raise ValueError("Invalid rail service type. Available types: commuter, express")

        if self.fare_type == 'regular':
            fare = base_fare + additional_fare_per_mile * self.distance
        elif self.fare_type == 'student':
            fare = base_fare * 0.8 + additional_fare_per_mile * self.distance
        elif self.fare_type == 'senior':
            fare = base_fare * 0.5 + additional_fare_per_mile * self.distance
        else:
            raise ValueError("Invalid fare type. Available types: regular, student, senior")

        return round(fare, 2)


#Subway Fare
class SubwayFareCalculator:
    def __init__(self, fare_type='regular'):
        self.fare_type = fare_type.lower()

    def calculate_fare(self):
        base_fare = 2.75 

        if self.fare_type == 'regular':
            fare = base_fare
        elif self.fare_type == 'student':
            fare = base_fare * 0.8
        elif self.fare_type == 'senior':
            fare = base_fare * 0.5
        else:
            raise ValueError("Invalid fare type. Available types: regular, student, senior")

        return round(fare, 2)



app = Flask(__name__)

@app.route('/api' , methods = ['GET'])
def returnascii():
    d = {}
    inputchr = str(request.args['query'])
    answer = str(ord(inputchr))
    d['output'] = answer
    return d



if __name__ == "__main__":
    app.run()
