class Person:
  """
  This class represents a person with height and weight properties
  and a method to calculate their BMI. It prompts the user for weight and height.
  """

  def __init__(self):
    """
    Initializes a new Person object by prompting the user for weight and height.
    """
    self.weight = float(input("Enter your weight in kilograms: "))
    self.height = float(input("Enter your height in meters: "))

  def BMI_Value(self):
    """
    Calculates and returns the BMI of the person.

    Returns:
      The BMI of the person as a decimal value.
    """
    if self.height == 0:
      return 0  # Avoid division by zero
    return self.weight / (self.height * self.height)

# Example usage
person = Person()
bmi = person.BMI_Value()
print(f"Your BMI is: {bmi:.2f}")