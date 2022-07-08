def main():
    mass = int(input("Enter mass (in Kilograms) "))
    print("E: ",calc_energy(mass))


def calc_energy(m):
    print("M:", m)
    energy = m * (300000000 ** 2)
    return energy 



main()