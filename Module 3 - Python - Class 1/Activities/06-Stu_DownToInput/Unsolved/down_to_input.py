# Take input of you and your neighbor
my_name = input("What is your name? ")
my_coding = int(input(f"{my_name}, how many months have you been coding? "))

# Take how long each of you have been coding
neighbor_name = input ("What is your neighbor's name? ")
neighbor_coding = int(input(f"How many months has {neighbor_name} been coding? "))
# Add total month
total_months = my_coding + neighbor_coding
# Print results
print(f"In total, {my_name} and {neighbor_name} have been coding for {total_months} months")

