# Carbon Footprint Calculator

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calculate_transportation_emissions():
    print("Transportation:")
    car_km = get_float_input("Enter the number of kilometers you drive per week: ")
    fuel_efficiency = get_float_input("Enter your car's fuel efficiency (km per liter): ")
    emission_factor_car = 2.31  # kg CO2 per liter of gasoline
    car_emissions = (car_km / fuel_efficiency) * emission_factor_car * 52

    public_transport_km = get_float_input("Enter the number of kilometers you travel by public transport per week: ")
    emission_factor_public_transport = 0.1  # kg CO2 per km
    public_transport_emissions = public_transport_km * emission_factor_public_transport * 52

    return car_emissions + public_transport_emissions

def calculate_energy_emissions():
    print("\nEnergy Use:")
    electricity_kwh = get_float_input("Enter your monthly electricity consumption (kWh): ")
    emission_factor_electricity = 0.527  # kg CO2 per kWh (varies by region)
    electricity_emissions = electricity_kwh * emission_factor_electricity * 12

    natural_gas_therms = get_float_input("Enter your monthly natural gas consumption (therms): ")
    emission_factor_natural_gas = 5.3  # kg CO2 per therm
    natural_gas_emissions = natural_gas_therms * emission_factor_natural_gas * 12

    return electricity_emissions + natural_gas_emissions

def calculate_diet_emissions():
    print("\nDiet:")
    meat_servings_per_week = get_float_input("Enter the number of meat servings you consume per week: ")
    emission_factor_meat = 7.2  # kg CO2 per serving
    meat_emissions = meat_servings_per_week * emission_factor_meat * 52

    plant_based_servings_per_week = get_float_input("Enter the number of plant-based meals you consume per week: ")
    emission_factor_plant = 1.5  # kg CO2 per serving
    plant_emissions = plant_based_servings_per_week * emission_factor_plant * 52

    return meat_emissions + plant_emissions

def main():
    print("Welcome to the Carbon Footprint Calculator!\n")
    
    transport_emissions = calculate_transportation_emissions()
    energy_emissions = calculate_energy_emissions()
    diet_emissions = calculate_diet_emissions()
    
    total_emissions = transport_emissions + energy_emissions + diet_emissions
    
    print(f"\nYour estimated annual carbon footprint is: {total_emissions:.2f} kg CO2")

if __name__ == "__main__":
    main()
