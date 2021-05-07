#define _USE_MATH_DEFINES
#include <cmath>
#include <complex>
#include <vector>
#include <iostream>
#include <iomanip>

extern "C"
{
    void dft(std::complex<double>* input, std::complex<double>* output, const int size);
    void fft(std::complex<double>* x, int size);
}

void fft(std::complex<double>* x, int size)
{
	const size_t N = size;
	if (N <= 1) return;

    int M = size/2;
    
    std::complex<double>* even = new std::complex<double>[M];
    std::complex<double>* odd = new std::complex<double>[M];

    for(int i = 0; i < M; i++)
    {
        even[i] = x[2*i];
        odd [i] = x[2*i + 1];
    }

	// conquer
	fft(even, M);
	fft(odd, M);

	// combine
	for (size_t k = 0; k < N / 2; ++k)
	{
		std::complex<double> t = std::polar(1.0, -2 * M_PI * k / N) * odd[k];
		x[k    ]     = even[k] + t;
		x[k + N / 2] = even[k] - t;
	}
}

void dft(std::complex<double>* input, std::complex<double>* output, const int size)
{
    int N = size;
    int K = N;

    std::complex<double> intSum;

    for (int k = 0; k < K; k++)
    {
        intSum = std::complex<double>(0, 0);

        for (int n = 0; n < N; n++)
        {
            double realPart = cos(((2* M_PI)/N) * k * n);
            double imagPart = sin(((2* M_PI)/N) * k * n);
            std::complex<double> w (realPart, -imagPart);
            intSum += input[n] * w;
        }
        output[k] = intSum;
    }
}