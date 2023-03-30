import fractions
import math

fraction_1 = input('Enter first fraction: ').split('/')
fraction_2 = input('Enter second fraction: ').split('/')

numerator_1 = int(fraction_1[0])
denumerator_1 = int(fraction_1[1])
numerator_2 = int(fraction_2[0])
denumerator_2 = int(fraction_2[1])

numerator_sum = numerator_1 * denumerator_2 + numerator_2 * denumerator_1
denominator_sum = denumerator_1 * denumerator_2

gcd_for_sum = math.gcd(numerator_sum, denominator_sum)
if gcd_for_sum:
    numerator_sum //= gcd_for_sum
    denominator_sum //= gcd_for_sum

numerator_multi = numerator_1 * numerator_2
denominator_multi = denumerator_1 * denumerator_2

gcd_for_multi = math.gcd(numerator_multi, denominator_multi)
if gcd_for_multi:
    numerator_multi //= gcd_for_multi
    denominator_multi //= gcd_for_multi

print(f'Fractions sum: \
    {numerator_sum}/{denominator_sum}')
print(f'Fractions sum with Fraction: \
    {fractions.Fraction(numerator_1, denumerator_1) + fractions.Fraction(numerator_2, denumerator_2)}')

print(f'Fractions multiply: \
    {numerator_multi}/{denominator_multi}')
print(f'Fractions multiply with Fraction: \
    {fractions.Fraction(numerator_1, denumerator_1) * fractions.Fraction(numerator_2, denumerator_2)}')