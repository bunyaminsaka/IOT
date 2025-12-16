"""
SmartHomeHubDoeb - Cost Calculator Module
Calculates energy costs based on device usage

Rates:
- Electricity: 10 PLN per 10 seconds per active light
- Gas: 5 PLN per 10 seconds when heating enabled
"""

class CostCalculator:
    """Energy cost calculator for SmartHomeHubDoeb"""
    
    def __init__(self, electricity_rate=10, gas_rate=5):
        self.electricity_rate = electricity_rate  # PLN per 10s per light
        self.gas_rate = gas_rate                  # PLN per 10s for heating
        self.electricity_total = 0
        self.gas_total = 0
    
    def calculate_interval(self, active_lights: int, heating_enabled: bool):
        """Calculate costs for one 10-second interval"""
        electricity_cost = self.electricity_rate * active_lights
        gas_cost = self.gas_rate if heating_enabled else 0
        
        self.electricity_total += electricity_cost
        self.gas_total += gas_cost
        
        return {
            "electricity_interval": electricity_cost,
            "gas_interval": gas_cost,
            "electricity_total": self.electricity_total,
            "gas_total": self.gas_total,
            "total": self.electricity_total + self.gas_total
        }
    
    def reset(self):
        """Reset cost counters"""
        self.electricity_total = 0
        self.gas_total = 0
    
    def get_totals(self):
        """Get current totals"""
        return {
            "electricity_total": self.electricity_total,
            "gas_total": self.gas_total,
            "total": self.electricity_total + self.gas_total
        }


# Example usage
if __name__ == "__main__":
    calc = CostCalculator()
    
    # Simulate 1 minute with 2 lights + heating
    for i in range(6):  # 6 intervals = 60 seconds
        result = calc.calculate_interval(active_lights=2, heating_enabled=True)
        print(f"Interval {i+1}: +{result['electricity_interval']} elec, +{result['gas_interval']} gas")
    
    print(f"\nTotal: {calc.get_totals()['total']} PLN")

