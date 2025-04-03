# Fix the naming convention issues in the following code block:

def convert_temperature(temp, from_unit, to_unit):

    conversion_factor = {
        'celsius_to_fahrenheit': lambda t: (t * 9/5) + 32,
        'fahrenheit_to_celsius': lambda t: (t - 32) * 5/9,
        'celsius_to_kelvin': lambda t: t + 273.15,
        'kelvin_to_celsius': lambda t: t - 273.15
    }
    
    conversion_key = f"{from_unit}_to_{to_unit}".lower()
    
    if conversion_key in conversion_factor:
        return conversion_factor[conversion_key](temp)
    else:
        return "Unsupported conversion"

class TemperatureTracker:
    MAX_TEMP = 100
    
    def __init__(self, current_temp):
        self.current_temp = current_temp
    
    def is_over_max(self):
        return self.current_temp > self.MAX_TEMP