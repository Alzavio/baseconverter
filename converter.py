def to_base(number, resulting_base):
    nums = "0123456789ABCDEF"
    bits = ""
    while number:
        print("While number", number, number % resulting_base, nums[number % resulting_base], bits)
        remainder = number % resulting_base
        bits = nums[remainder] + bits
        number //= resulting_base
    return bits

def main(number, original_base, resulting_base):

    if original_base == resulting_base:
        return number

    # Catch invalid values
    if original_base < 2 or original_base > 16 or resulting_base < 2 or resulting_base > 16:
        print("Invalid base number")
        return ''

    try:
        number = float(number)
        if not number.is_integer() or number < 0:
            print("Invalid number")
            return ''
        number = int(number)
        print(number)
    except:
        # If it fails, it's not a number at all, which is expected for high bases
        print("Not a number, continuing")
        pass

    if str(number).isdigit() and number <= 0:
        print("Invalid number")
        return ''

    # Convert to base 10 for re-conversion
    number = int(str(number), base=original_base)

    # If the desired result is base 10, return number
    if resulting_base == 10:
        print(number)
        return number

    print("Converting")
    new_number = to_base(number, resulting_base)
    print(new_number)

    return new_number


number = input("Enter number: ")
original_base = int(input("Enter original base number (2-16): "))
resulting_base = int(input("Enter resulting base number (2-16): "))
print(main(number, original_base, resulting_base))