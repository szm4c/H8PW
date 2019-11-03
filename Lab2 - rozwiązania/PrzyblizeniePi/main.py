import random
import math

def PrzyblizPi(n):

    poleKola = 0
    poleKwadratu = n

    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        #print(f"Współrzędne punktu: ({x}, {y})")

        d = math.sqrt(x**2 + y**2)
        #print(f"Odległość punktu od (0,0): {d}\n")

        if d <= 1:
            poleKola += 1

    przyblizeniePi = 4 * poleKola / poleKwadratu
    return przyblizeniePi



print(f"1. Przybliżenie PI wynosi: {PrzyblizPi(10)}")
print(f"2. Przybliżenie PI wynosi: {PrzyblizPi(100)}")
print(f"3. Przybliżenie PI wynosi: {PrzyblizPi(1000)}")
print(f"4. Przybliżenie PI wynosi: {PrzyblizPi(10000)}")
print(f"5. Przybliżenie PI wynosi: {PrzyblizPi(100000)}")
print(f"6. Przybliżenie PI wynosi: {PrzyblizPi(1000000)}")
print(f"7. Przybliżenie PI wynosi: {PrzyblizPi(10000000)}")