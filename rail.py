class RailFareCalculator:
    def __init__(self, distance, service_type='commuter', fare_type='regular'):
        self.distance = distance
        self.service_type = service_type.lower()
        self.fare_type = fare_type.lower()

    def calculate_fare(self):
        base_fare = 5.00  # Example base fare for rail service
        additional_fare_per_mile = 0.75  # Example additional fare per mile

        if self.service_type == 'commuter':
            additional_fare_per_mile = 0.75  # Adjust for commuter rail
        elif self.service_type == 'express':
            additional_fare_per_mile = 1.25  # Adjust for express service
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

# Example usage:
distance_traveled = 20  # Example distance in miles
service_type = 'commuter'  # Example rail service type
fare_type = 'regular'  # Example fare type

rail_calculator = RailFareCalculator(distance_traveled, service_type, fare_type)
total_fare = rail_calculator.calculate_fare()

print(f"The rail fare for {distance_traveled} miles ({service_type} service, {fare_type} fare) is: ${total_fare}")
