def calculate_honey(volume_gal, target_og):
    honey_lb = volume_gal * ((target_og - 1) / 0.035)
    return honey_lb

def calculate_og(honey_lb, volume_gal):
    og = 1 + (honey_lb / (volume_gal * 8.345))
    return og

def calculate_potential_abv(og):
    potential_abv = 131.25 * (og - 1)
    return potential_abv

def calculate_actual_abv(og, fg):
    abv = 131.25 * (og - fg)
    return abv

def calculate_dilution_og(original_og, original_volume, added_volume, dilution_og=1.000):
    new_og = ((original_og * original_volume) + (dilution_og * added_volume)) / (original_volume + added_volume)
    return new_og

def main():
    print("Mead Calculator")
    print("================")
    
    ## advanced = bool(input("Do you want to use advanced features? (yes/no): "))     It's a Surprise Tool That Will Help Us Later
    volume_gal = float(input("Enter the volume of mead in gallons: "))
    target_og = float(input("Enter the target Original Gravity (OG): "))
    
    honey_needed = calculate_honey(volume_gal, target_og)
    print(f"Amount of honey needed: {honey_needed:.2f} lb")
    
    actual_og = calculate_og(honey_needed, volume_gal)
    print(f"Calculated Original Gravity (OG): {actual_og:.3f}")
    
    potential_abv = calculate_potential_abv(target_og)
    print(f"Potential Alcohol By Volume (ABV): {potential_abv:.2f}%")
    
    fg = float(input("Enter the Final Gravity (FG) after fermentation: "))
    actual_abv = calculate_actual_abv(target_og, fg)
    print(f"Actual Alcohol By Volume (ABV): {actual_abv:.2f}%")


if __name__ == "__main__":
    main()
