#include "pch.h"
#include <stdexcept>
#include "Vector.h"
#include "Matrix.h"
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

//LIBDLL int sum(int a, int b) {
//    return a + b;
//}

LIBDLL float* vector_add(float* v0, int size_v0, float* v1, int size_v1) {
    //float* ret_v = (float*)malloc(size_v0 * sizeof(float));
    //    if (size_v0 != size_v1) {
    //        throw std::invalid_argument("vectors length are different");
    //    }
    //    else {
    //        for (int i = 0; i < size_v0; i++) {
    //            *(ret_v + i) = *(v0 + i) + *(v1 + i);
    //        }
    //    }
    //    return ret_v;
    Vector vec1 = Vector(v0, size_v0);
    Vector vec2 = Vector(v1, size_v1);
    Vector vec3 = vec1 + vec2;
    return vec3.get_vector_elements();
}

//LIBDLL float* vector_add2(float* v0, int size_v0, float* v1, int size_v1) {
//    float *ret_v = (float*)malloc(size_v0 * sizeof(float));
//    if (size_v0 != size_v1) {
//        throw std::invalid_argument("vectors length are different");
//    }
//    else {
//        for (int i = 0; i < size_v0; i++) {
//            *(ret_v + i) = *(v0 + i) + *(v1 + i);
//        }
//    }
//    return ret_v;
//}

LIBDLL float* vector_sub(float* v0, int size_v0, float* v1, int size_v1) {
    //    float* ret_v = (float*)malloc(size_v0 * sizeof(float));
    //    if (size_v0 != size_v1) {
    //        throw std::invalid_argument("vectors length are different");
    //        //          throw MyException()
    //    }
    //    else {
    //        for (int i = 0; i < size_v0; i++) {
    //            *(ret_v + i) = *(v0 + i) - *(v1 + i);
    //        }
    //    }
    //    return ret_v;
    Vector vec1 = Vector(v0, size_v0);
    Vector vec2 = Vector(v1, size_v1);
    Vector vec3 = vec1 - vec2;
    return vec3.get_vector_elements();
}

LIBDLL float* vector_mult(float* v0, int size_v0, float s) {
    //    float* ret_v = (float*)malloc(size_v0 * sizeof(float));
    //    for (int i = 0; i < size_v0; i++) {
    //        *(ret_v + i) = *(v0 + i) * s;
    //    }
    //    return ret_v;
    Vector vec1 = Vector(v0, size_v0);
    Vector vec2 = vec1 * s;
    return vec2.get_vector_elements();
}

LIBDLL float* vector_div(float* v0, int size_v0, float s) {
    //    if (s == 0) {
    //        throw std::invalid_argument("scalar can not be 0");
    //        //          throw MyException()
    //    }
    //    float* ret_v = (float*)malloc(size_v0 * sizeof(float));
    //    for (int i = 0; i < size_v0; i++) {
    //        *(ret_v + i) = *(v0 + i) / s;
    //    }
    //    return ret_v;
    Vector vec1 = Vector(v0, size_v0);
    Vector vec2 = vec1 / s;
    return vec2.get_vector_elements();
}

//LIBDLL float* vector_free(float* v0) {
//    free(v0);
//    return v0;
//}

LIBDLL float* create_matrix(float* matrix_elements, int vector_number, int vector_size) {
    Vector* v = (Vector*)malloc(vector_number * sizeof(Vector));
    for (int i = 0; i < vector_number; i++) {
        *(v + i) = Vector((matrix_elements + i * vector_size), vector_size);
    }
    Matrix matrix = Matrix(v, vector_number);
    //free(v);
    return ((Vector*)matrix.get_vectors() + 2)->get_vector_elements();
}

LIBDLL float* matrix_add(float* matrix_elements_m0, int vector_number_m0, int vector_size_m0, float* matrix_elements_m1, int vector_number_m1, int vector_size_m1) {
    Vector* vectors_m0 = (Vector*)malloc(vector_number_m0 * sizeof(Vector));
    Vector* vectors_m1 = (Vector*)malloc(vector_number_m1 * sizeof(Vector));
    for (int i = 0; i < vector_number_m0; i++) {
        *(vectors_m0 + i) = Vector((matrix_elements_m0 + i * vector_size_m0), vector_size_m0);
    }
    for (int i = 0; i < vector_number_m1; i++) {
        *(vectors_m1 + i) = Vector((matrix_elements_m1 + i * vector_size_m1), vector_size_m1);
    }
    Matrix m0 = Matrix(vectors_m0, vector_number_m0);
    Matrix m1 = Matrix(vectors_m1, vector_number_m1);
    Matrix res = m0 + m1;
    return res.serialize();
}

LIBDLL float* matrix_sub(float* matrix_elements_m0, int vector_number_m0, int vector_size_m0, float* matrix_elements_m1, int vector_number_m1, int vector_size_m1) {
    Vector* vectors_m0 = (Vector*)malloc(vector_number_m0 * sizeof(Vector));
    Vector* vectors_m1 = (Vector*)malloc(vector_number_m1 * sizeof(Vector));
    for (int i = 0; i < vector_number_m0; i++) {
        *(vectors_m0 + i) = Vector((matrix_elements_m0 + i * vector_size_m0), vector_size_m0);
    }
    for (int i = 0; i < vector_number_m1; i++) {
        *(vectors_m1 + i) = Vector((matrix_elements_m1 + i * vector_size_m1), vector_size_m1);
    }
    Matrix m0 = Matrix(vectors_m0, vector_number_m0);
    Matrix m1 = Matrix(vectors_m1, vector_number_m1);
    Matrix res = m0 - m1;
    return res.serialize();
}

LIBDLL float* matrix_mul_scalar(float* matrix_elements_m0, int vector_number_m0, int vector_size_m0, float s) {
    Vector* vectors_m0 = (Vector*)malloc(vector_number_m0 * sizeof(Vector));
    for (int i = 0; i < vector_number_m0; i++) {
        *(vectors_m0 + i) = Vector((matrix_elements_m0 + i * vector_size_m0), vector_size_m0);
    }
    Matrix m0 = Matrix(vectors_m0, vector_number_m0);
    Matrix res = m0 * s;
    return res.serialize();
}
