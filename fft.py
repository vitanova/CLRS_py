from math import pi, e

def recursive_fft(a, inverse=False):
    n = len(a)
    if n==1:
        return a
    omega_n = 1/e**(2*pi*(0+1j)/n)*inverse + e**(2*pi*(0+1j)/n)*(1-inverse)
    omega   = 1
    a_0 = [a[2*k] for k in range(int(n/2))]
    a_1 = [a[2*k+1] for k in range(int(n/2))]
    y_0 = recursive_fft(a_0, inverse)
    y_1 = recursive_fft(a_1, inverse)
    y   = [0]*n
    for k in range(int(n/2)):
        y[k]          = y_0[k] + omega*y_1[k]
        y[k+int(n/2)] = y_0[k] - omega*y_1[k]
        omega = omega * omega_n
    return y

a = [0, 0, 0, 0, 0, 1, 0, 0]
a_fft = recursive_fft(a, False)
recursive_fft(a_fft, True)

a = [1, 1, 1, 1]
b = [0, 0, 0, 1]

def poly_multi(a, b):
    n_a = len(a)
    a_2n = a + [0]*n_a
    b_2n = b + [0]*n_a
    fft_a = recursive_fft(a_2n)
    fft_b = recursive_fft(b_2n)
    a_dot_b = [fft_a[i]*fft_b[i] for i in range(2*n_a)]
    #print(a_2n, '\n', b_2n, '\n', fft_a, '\n', fft_b, '\n', a_dot_b)
    return [xx/(2*n_a) for xx in recursive_fft(a_dot_b, inverse=True)]
print(a)
print(b)
c = poly_multi(a, b)
print(c)