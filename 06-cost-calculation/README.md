# 💰 Task 6: Cost Calculation

Energy cost tracking system for SmartHomeHubDoeb.

## Rates

| Resource | Rate | Condition |
|----------|------|-----------|
| Electricity | 10 PLN/10s | Per active light |
| Gas | 5 PLN/10s | When heating ON |

## Calculation Examples

### Example 1: 2 lights + heating for 30 seconds
```
Electricity: 10 PLN × 2 lights × 3 intervals = 60 PLN
Gas: 5 PLN × 3 intervals = 15 PLN
Total: 75 PLN
```

### Example 2: All 3 lights for 1 minute
```
Electricity: 10 PLN × 3 lights × 6 intervals = 180 PLN
Gas: 0 PLN
Total: 180 PLN
```

## Files

| File | Description |
|------|-------------|
| `cost_calculator.py` | Cost calculation module |

## Usage

```python
from cost_calculator import CostCalculator

calc = CostCalculator()
result = calc.calculate_interval(active_lights=2, heating_enabled=True)
print(f"Total: {result['total']} PLN")
```

