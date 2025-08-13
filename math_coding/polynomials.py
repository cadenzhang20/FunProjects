import random

print("Polynomial Generator")

while True:
    print("""MODES
    1: practice mode""")
    choice = input()

    choice = 1

    max_a = 5
    max_b = 10
    max_c = 5
    max_d = 10

    if int(choice) == 1:
        print("Begin: ", end="")
        count = 0
        while input() == "":
            a = random.randint(1, 5)

            choices = list(range(-10, 0)) + list(range(1, 11))
            [choices.remove(x) for x in [a, -a]]
            b = random.choice(choices)

            c = list(range(1, 6))
            c.remove(abs(a))
            if -5 <= b <= 5: c.remove(abs(b))
            c = random.choice(c)

            [choices.remove(x) for x in [b, -b, c, -c]]
            d = random.choice(choices)

            coef_a = a * c
            coef_b = a * d + b * c
            coef_c = b * d

            if coef_a == 1: coef_a = ""

            if coef_b > 0: coef_b = f"+ {coef_b}"
            else: coef_b = f"- {-coef_b}"

            if coef_c > 0: coef_c = f"+ {coef_c}"
            else: coef_c = f"- {-coef_c}"

            print(f"{coef_a}x^2 {coef_b}x {coef_c}", end="\t\t\t")


            factor = 1

            for x in range(2, 5):
                if a % x == b % x == 0:
                    a //= x
                    b //= x
                    factor *= x
                if c % x == d % x == 0:
                    c //= x
                    d //= x
                    factor *= x

            if factor == 1:
                factor = ""


            if a == -1: a = "-"
            elif a == 1: a = ""

            if b < 0: b = f"- {-b}"
            elif b > 0: b = f"+ {b}"

            if c == -1: c = "-"
            elif c == 1: c = ""

            if d < 0: d = f"- {-d}"
            elif d > 0: d = f"+ {d}"

            answer = f"{factor}({a}x {b})({c}x {d})"
            input()
            count += 1
            print(answer)

        print(f"{count} questions completed")
