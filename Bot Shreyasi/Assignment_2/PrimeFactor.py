


def prime_factor(val):
    prime_numbers = []
    divisior = 2

    while val>1:
        count = 0
        while val%divisior==0:
            print(f'{val} % {divisior} = {val%divisior}')
            val//=divisior
            count+=1
        if count>0:
            prime_numbers.append((divisior,count))
        divisior+=1



    return prime_numbers


pf = prime_factor(60)
print(pf)