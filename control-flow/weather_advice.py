# weather_advice.py

# Prompt User for Weather Input
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide Clothing Recommendations
if weather == "sunny":
    recommendation = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    recommendation = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    recommendation = "Make sure to wear a warm coat and a scarf."
else:
    recommendation = "Sorry, I don't have recommendations for this weather."

# Output the Recommendation
print(f"\nWhat's the weather like today? (sunny/rainy/cold): {weather}")
print(recommendation)

