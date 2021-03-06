def pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(1000):                       # Change the range value to achieve different levels of precision
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


digits = pi()
pi_list = []
values = []

for i in pi():
    values.append(str(i))                      # Appends data to the array 'values'

values = values[:1] + ['.'] + values[1:]
string = "".join(values)
print ("Pi:\n%s" % string)                     # Prints resulting calculation
