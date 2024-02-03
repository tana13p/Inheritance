class BusFareCalculator:
    def __init__(self, distance, fare_type='regular'):
        self.distance = distance
        self.fare_type = fare_type.lower()

    def calculate_fare(self):
        base_fare = 2.75  # NYC MTA base fare as of knowledge cutoff (2022)
        additional_fare_per_mile = 0.55  # Example additional fare per mile

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
distance_traveled = 5  # Example distance in miles
fare_type = 'regular'  # Example fare type

calculator = BusFareCalculator(distance_traveled, fare_type)
total_fare = calculator.calculate_fare()

print(f"The bus fare for {distance_traveled} miles ({fare_type} fare) is: ${total_fare}")
