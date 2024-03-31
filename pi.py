import math

# biggest common denominator
def bcd(a, b):
    a, b = max(a, b), min(a,b)
    while True:
        c = a % b
        a, b = max(b, c), min(b, c)
        if b == 0:
            return a

def remove_bcd(a, b):
    denominator = bcd(a, b)
    return a // denominator, b // denominator

# returns a3, b3 such that:
# arctan (a1 / b1) + arctan (a2, b2) = arctan (a3, b3)
def arctan_add(a1, b1, a2, b2):
    a3 = (a1 * b2 + a2 * b1)
    b3 = (b1 * b2 - a1 * a2)
    return (a3, b3)

# returns a3, b3 such that:
# arctan (a1 / b1) - arctan (a2, b2) = arctan (a3, b3)
def arctan_subtract(a1, b1, a2, b2):
    a3 = (a1 * b2 - a2 * b1)
    b3 = (b1 * b2 + a1 * a2)
    return (a3, b3)

def find_max_coefficient(N):
    a = 0
    b = 1
    coefficient = 0
    while True:
        (new_a, new_b) = arctan_add(a,b, 1, N)
        if new_a >= new_b:
            # cannot even add a single 1/N, so we've found the max coefficient
            return coefficient, a, b

        this_coeff = 1
        this_a = 1
        this_b = N
        while True:
            next_coeff = this_coeff * 2
            next_a, next_b = arctan_add(this_a, this_b, this_a, this_b)
            new_a, new_b = arctan_add(a,b, next_a, next_b)
            if new_a >= new_b:
                break
            this_coeff = next_coeff
            this_a, this_b = next_a, next_b
        
        coefficient += this_coeff
        a, b = arctan_add(a,b, this_a, this_b)

def lehmer(fractions):
    lamb = 0.0
    for a,b in fractions:
        lamb += 1.0 / math.log10(b / a)
    return lamb

def main():
    N = 100 # or any arbitrarily large number
    coeff, a, b = find_max_coefficient(N)
    other_a, other_b = arctan_subtract(1, 1, a, b)
    other_a, other_b = remove_bcd(other_a, other_b)
    print(f"(pi / 4) == {coeff} * arctan(1 / {N}) + arctan({other_a} / {other_b})")
    
    print("lehmer: ", lehmer([(1,N), (other_a, other_b)]))

    # sanity check:
    assert abs(math.pi/4.0 - (coeff * math.atan(1.0 / N) + math.atan(other_a/other_b))) < 1e-6


if __name__ == "__main__":
    main()