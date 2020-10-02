def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True


def prime_product(m):
    for i in range(2, m):
        if is_prime(i) and (m % i == 0):
            temp = m / i
            if is_prime(temp):
                return True

    return False


if __name__ == '__main__':
    m = int(input("Enter a integer number: "))
    print(prime_product(m))