import math

class complex:
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return complex(real_part, imag_part)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def __round__(self, ndigits=None):
        return complex(round(self.real, ndigits), round(self.imag, ndigits))

    def conjugate(self):
        return complex(self.real, -self.imag)

    def __str__(self):
        return f"({round(self.real, 5)} + {round(self.imag, 5)}i)"

# Function to calculate the twiddle matrix
def calculate_twiddle_matrix(N):
    twiddle_matrix = [[0 for _ in range(N)] for _ in range(N)]
    for k in range(N):
        for n in range(N):
            real = math.cos(-2 * math.pi * k * n / N)
            imag = math.sin(-2 * math.pi * k * n / N)
            twiddle_matrix[k][n] = complex(real, imag)
    return twiddle_matrix
def calculate_twiddle_matrix_star(N):
    twiddle_matrix_star = [[0 for _ in range(N)] for _ in range(N)]
    for k in range(N):
        for n in range(N):
            real = math.cos(-2 * math.pi * k * n / N)
            imag = math.sin(2 * math.pi * k * n / N)
            twiddle_matrix_star[k][n] = complex(real, imag)
    return twiddle_matrix_star
def multiply_twiddle_star(input_signal, twiddle_matrix_star):
    N = len(input_signal)
    output_star = [0] * N 
    for k in range(N):
        sum_value = 0
        for n in range(N):
            sum_value += twiddle_matrix_star[k][n] * input_signal[n]
        output_star[k] = sum_value/N
    return output_star

def Idft(input_signal):
    N = len(input_signal)
    twiddle_matrix_star = calculate_twiddle_matrix_star(N)
    Idft_result = multiply_twiddle_star(input_signal, twiddle_matrix_star)
    return Idft_result

# Function to multiply the twiddle matrix with the input signal
def multiply_twiddle(input_signal, twiddle_matrix):
    N = len(input_signal)
    output = [0] * N 
    for k in range(N):
        sum_value = 0
        for n in range(N):
            sum_value += twiddle_matrix[k][n] * input_signal[n]
        output[k] = sum_value
    return output

# Final DFT function
def dft(input_signal):
    N = len(input_signal)
    twiddle_matrix = calculate_twiddle_matrix(N)
    dft_result = multiply_twiddle(input_signal, twiddle_matrix)
    return dft_result

# Function to calculate the magnitude and phase of the DFT
def calculate_magnitude_and_phase(dft_result, epsilon=1e-10):
    magnitudes = []
    phases = []
    for value in dft_result:
        real_part = value.real
        imag_part = value.imag

        if abs(real_part) < epsilon:
            real_part = 0.0
        if abs(imag_part) < epsilon:
            imag_part = 0.0
        
        magnitude = abs(complex(real_part, imag_part))
        if magnitude < epsilon:
            magnitude = 0.0
            phase = 0.0
        else:
            phase = math.atan2(imag_part, real_part) * (180 / math.pi)
            # Normalize phase to ]-180, 180]
            if phase <= -180:
                phase += 360

        magnitudes.append(round(magnitude, 5))
        phases.append(round(phase, 5))

        dft_result[dft_result.index(value)] = complex(round(real_part, 5), round(imag_part, 5))
        
    return magnitudes, phases, dft_result

def calculate_magnitude_for_inverse(Idft_result, epsilon=1e-10):
    for value in Idft_result:
        real_part = value.real
        imag_part = value.imag

        if abs(real_part) < epsilon:
            real_part = 0.0
        if abs(imag_part) < epsilon:
            imag_part = 0.0

        Idft_result[Idft_result.index(value)] = complex(round(real_part, 5), round(imag_part, 5))
        
    return Idft_result

# Function to get input from the user in list form
def get_input():
    try:
        return list(map(float, input("Enter the signal values (space-separated): ").split()))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return get_input()

def get_input_Inverse():
    try:
        return list(map(complex, input("Enter the signal values (space-separated): ").split()))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return get_input()

def main():
    n = int(input("Enter 1 or 2\n1) DFT\n2)IDFT\n"))
    if(n == 1):
        input_signal = get_input()
        dft_result = dft(input_signal)
        magnitudes, phases, cleaned_dft_result = calculate_magnitude_and_phase(dft_result)
        print("\nDFT Result: ", cleaned_dft_result)
        print("\nMagnitude of DFT: ", magnitudes)
        print("\nPhase of DFT: ", phases)
    elif(n == 2):
        inverse_input = get_input_Inverse()
        Idft_result = Idft(inverse_input)
        cleaned_idft_result = calculate_magnitude_for_inverse(Idft_result)
        print("\nIDFT result: ",cleaned_idft_result)
if __name__ == "__main__":
    main()