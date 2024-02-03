class SubwayFareCalculator:
    def __init__(self, fare_type='regular'):
        self.fare_type = fare_type.lower()

    def calculate_fare(self):
        base_fare = 2.75  # NYC MTA subway base fare as of knowledge cutoff (2022)

        if self.fare_type == 'regular':
            fare = base_fare
        elif self.fare_type == 'student':
            fare = base_fare * 0.8
        elif self.fare_type == 'senior':
            fare = base_fare * 0.5
        else:
            raise ValueError("Invalid fare type. Available types: regular, student, senior")

        return round(fare, 2)

# Example usage:
fare_type = 'regular'  # Example fare type

subway_calculator = SubwayFareCalculator(fare_type)
total_fare = subway_calculator.calculate_fare()

print(f"The subway fare ({fare_type} fare) is: ${total_fare}")
