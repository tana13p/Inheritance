class CitiBikeFareCalculator:
    def __init__(self, membership_type, usage_time_minutes):
        self.membership_type = membership_type.lower()
        self.usage_time_minutes = usage_time_minutes

    def calculate_fare(self):
        # Citi Bike membership plans and their respective fees
        membership_fees = {
            'single_ride': 4.95,     # Single ride without membership
            'day_pass': 12.95,       # 24-hour pass
            'monthly_membership': 24.95,  # Monthly membership
            'annual_membership': 179.00  # Annual membership
        }

        # Additional fee for exceeding free time (in minutes) for membership plans
        free_time = {
            'single_ride': 0,
            'day_pass': 30,
            'monthly_membership': 45,
            'annual_membership': 45
        }

        # Calculate the base fee based on the membership type
        base_fee = membership_fees.get(self.membership_type, 0.0)

        # Calculate additional fee for exceeding free time
        additional_fee_per_minute = max(0, self.usage_time_minutes - free_time.get(self.membership_type, 0)) * 0.18

        # Calculate total fare
        fare = base_fee + additional_fee_per_minute

        return round(fare, 2)

# Example usage:
membership_type = 'single_ride'  # Example membership type
usage_time_minutes = 45  # Example usage time in minutes

citi_bike_calculator = CitiBikeFareCalculator(membership_type, usage_time_minutes)
total_fare = citi_bike_calculator.calculate_fare()

print(f"The Citi Bike fare for {membership_type} membership and {usage_time_minutes} minutes is: ${total_fare}")
