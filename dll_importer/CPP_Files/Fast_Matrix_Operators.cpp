#include "pch.h"
#include <stdexcept>
//#include <exception>
using namespace std;



//struct MyException : public std::exception
//{
//	const char * what () const throw ()
//    {
//    	return "C++ Exception";
//    }
//}

#define LIBDLL extern "C" __declspec(dllexport)

LIBDLL int sum(int a, int b) {
    return a + b;
}

LIBDLL float* vector_add(float* v0, int size_v0, float* v1, int size_v1) {
    float *ret_v = (float*)malloc(size_v0 * sizeof(float));
    if (size_v0 != size_v1) {
        throw std::invalid_argument("vectors length are different");
        //          throw MyException()
    }
    else {
        for (int i = 0; i < size_v0; i++) {
            *(ret_v + i) = *(v0 + i) + *(v1 + i);
        }
    }
    return ret_v;
}

LIBDLL float* vector_sub(float* v0, int size_v0, float* v1, int size_v1) {
    float* ret_v = (float*)malloc(size_v0 * sizeof(float));
    if (size_v0 != size_v1) {
        throw std::invalid_argument("vectors length are different");
        //          throw MyException()
    }
    else {
        for (int i = 0; i < size_v0; i++) {
            *(ret_v + i) = *(v0 + i) - *(v1 + i);
        }
    }
    return ret_v;
}

LIBDLL float* vector_mult(float* v0, int size_v0, float s) {
    float* ret_v = (float*)malloc(size_v0 * sizeof(float));
    for (int i = 0; i < size_v0; i++) {
        *(ret_v + i) = *(v0 + i) * s;
    }
    return ret_v;
}

LIBDLL float* vector_div(float* v0, int size_v0, float s) {
    if (s == 0) {
        throw std::invalid_argument("scalar can not be 0");
        //          throw MyException()
    }
    float* ret_v = (float*)malloc(size_v0 * sizeof(float));
    for (int i = 0; i < size_v0; i++) {
        *(ret_v + i) = *(v0 + i) / s;
    }
    return ret_v;
}

LIBDLL float* vector_free(float* v0) {
    free(v0);
    return v0;
}