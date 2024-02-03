class FerryFareCalculator:
    def __init__(self, distance, service_type='standard', fare_type='regular'):
        self.distance = distance
        self.service_type = service_type.lower()
        self.fare_type = fare_type.lower()

    def calculate_fare(self):
        base_fare = 10.00  # Example base fare for ferry service
        additional_fare_per_mile = 1.50  # Example additional fare per mile

        if self.service_type == 'standard':
            additional_fare_per_mile = 1.50  # Adjust for standard ferry service
        elif self.service_type == 'express':
            additional_fare_per_mile = 2.50  # Adjust for express ferry service
        else:
            raise ValueError("Invalid ferry service type. Available types: standard, express")

        if self.fare_type == 'regular':
            fare = base_fare + additional_fare_per_mile * self.distance
        elif self.fare_type == 'child':
            fare = base_fare * 0.75 + additional_fare_per_mile * self.distance  # Example child fare discount
        else:
            raise ValueError("Invalid fare type. Available types: regular, child")

        return round(fare, 2)

# Example usage:
distance_traveled = 15  # Example distance in miles
service_type = 'standard'  # Example ferry service type
fare_type = 'regular'  # Example fare type

ferry_calculator = FerryFareCalculator(distance_traveled, service_type, fare_type)
total_fare = ferry_calculator.calculate_fare()

print(f"The ferry fare for {distance_traveled} miles ({service_type} service, {fare_type} fare) is: ${total_fare}")
