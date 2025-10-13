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

    if number < 0:
        print("Invalid number")
        return ''

    if number == 0:
        print("0")
        return ''

    # Convert to base 10 for re-conversion
    if original_base != 10:
        number = int(number, base=original_base)

    # If the desired result is base 10, return number
    if resulting_base == 10:
        print(number)
        return number

    print("Converting")
    new_number = to_base(number, resulting_base)
    print(new_number)

    return new_number


number = int(input("Enter number: "))
original_base = int(input("Enter original base number (2-16): "))
resulting_base = int(input("Enter resulting base number (2-16): "))
main(number, original_base, resulting_base)