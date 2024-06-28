import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
food = pd.read_csv('food1.csv')

# Display the column names to inspect for any issues
print("Column Names:")
print(food.columns)

# Strip whitespace from the column names to avoid KeyError
food.columns = food.columns.str.strip()

# Display the column names again after stripping whitespace
print("Column Names after stripping whitespace:")
print(food.columns)

# Function to get top 10 categories by a nutrient
def get_top_categories(nutrient):
    top_food = food.nlargest(10, nutrient)
    return top_food['Category'].tolist()

# Extract top 10 categories by different nutrients
Protein = get_top_categories('Protein')
Carbs = get_top_categories('Carbs')
Calcium = get_top_categories('Calcium')
Vitamin_B6 = get_top_categories('Vitamin B6')
Sugar = get_top_categories('Sugar')
Saturated_Fat = get_top_categories('Saturated Fat')
Vitamin_C = get_top_categories('Vitamin C')
Iron = get_top_categories('Iron')
Calories = get_top_categories('Calories')
Cholesterol = get_top_categories('Cholesterol')

# Create a DataFrame to display the top categories
out_df = pd.DataFrame({
    "Kilocalory": Calories,
    "Protein": Protein,
    "Carbohydrate": Carbs,
    "Sugar": Sugar,
    "Vitamin C": Vitamin_C,
    "Saturated Fat": Saturated_Fat,
    "Cholesterol": Cholesterol,
    "Iron": Iron,
    "Calcium": Calcium,
    "Vitamin B6": Vitamin_B6
})

# Save the DataFrame to a CSV file
# out_df.to_csv('out.csv', index=False)

# Descriptive statistics
desc_stats = food.describe()
print(desc_stats)

#---------------------------------------------------------------
print('================')
print('================')
print('================')

weight = int(input("Enter your weight (kg): "))
height = int(input("Enter your height (cm): "))
age = int(input("Enter your age: "))

bmi = weight / ((height / 100) ** 2)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are Underweight")
elif 18.5 <= bmi < 24.9:
    print("You have Normal Weight")
elif 25.0 <= bmi < 29.9:
    print("You are Overweight")
else:
    print("You are Obese")        

# Example of a personalized recommendation based on BMI
if bmi < 18.5:
    print("Consider foods high in protein and calories to gain weight.")
elif 25.0 <= bmi < 29.9:
    print("Consider foods low in sugar and saturated fats to manage weight.")

# Save the DataFrame to a CSV file if needed
# out_df.to_csv('nutrition_analysis.csv', index=False)

# Visualization: Top 10 foods by Protein content
plt.figure(figsize=(10, 6))
sns.barplot(x='Protein', y='Category', data=food.nlargest(10, 'Protein'))
plt.title('Top 10 Foods by Protein Content')
plt.xlabel('Protein (g)')
plt.ylabel('Category')
plt.show()

# Visualization: Top 10 foods by Vitamin C content
plt.figure(figsize=(10, 6))
sns.barplot(x='Vitamin C', y='Category', data=food.nlargest(10, 'Vitamin C'))
plt.title('Top 10 Foods by Vitamin C Content')
plt.xlabel('Vitamin C (g)')
plt.ylabel('Category')
plt.show()

# Visualization: Top 10 foods by Carbs content
plt.figure(figsize=(10, 6))
sns.barplot(x='Carbs', y='Category', data=food.nlargest(10, 'Carbs'))
plt.title('Top 10 Foods by Carbs Content')
plt.xlabel('Carbs (g)')
plt.ylabel('Category')
plt.show()

# Visualization: least 10 foods by Sugar content
plt.figure(figsize=(10, 6))
sns.barplot(x='Sugar', y='Category', data=food.nsmallest(10, 'Sugar'))
plt.title('Least 10 Foods by Sugar Content')
plt.xlabel('Sugar (g)')
plt.ylabel('Category')
plt.show()

# Visualization: least 10 foods by Saturated Fat content
plt.figure(figsize=(10, 3))
sns.barplot(x='Saturated Fat', y='Category', data=food.nsmallest(10, 'Saturated Fat'))
plt.title('Least 10 Foods by Saturated Fat Content')
plt.xlabel('Saturated Fat (g)')
plt.ylabel('Category')
plt.show()


# Diet Planner: Recommend foods based on user's calorie goal
daily_calories = int(input("Enter your daily calorie goal: "))
recommended_foods = food[food['Calories'] <= daily_calories].nlargest(10, 'Calories')
print("Recommended Foods based on your calorie goal:")
print(recommended_foods[['Category', 'Calories']])
