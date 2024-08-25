# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker, name):
  estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
  print('The estimated insurance cost for ' + name + ' is ' + str(estimated_cost) + ' dollars.')
  return estimated_cost
  
# Create difference_between_insurance() function below to calculate the difference between insurance costs of any two individuals: 
def difference_between_insurance(first_person, second_person):
  if first_person > second_person:
    difference = first_person - second_person
  else:
    difference = second_person - first_person
  print('The difference in insurance cost is ' + str(difference) + ' dollars.')
  return difference

# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0, name ='Maria')

# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1, name ='Omar')

# Estimate your own insurance cost
ciara_insurance_cost = calculate_insurance_cost(24, 0, 24.2, 0, 0, name = 'Ciara')

# Estimates the difference between insurance costs
difference_insurance = difference_between_insurance(maria_insurance_cost, omar_insurance_cost)
