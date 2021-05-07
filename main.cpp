#define _USE_MATH_DEFINES
#include <cmath>
#include <complex>
#include <vector>
#include <iostream>
#include <iomanip>

extern "C"
{
    void dft(std::complex<double>* input, std::complex<double>* output, const int size);
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