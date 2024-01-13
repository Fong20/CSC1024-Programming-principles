#Rate (speed of light)
Rate = 3 * 10 ** 8

#convert 1 year to seconds
seconds = 365 * 24 * 60 ** 2

#calculate distance (Light year)
Distance = Rate * seconds

#f string displays answer in scientific format, it uses {}, .2 means 2 decimal place, 
print(f"Light travels {Distance:.2e} meters in a year.")
