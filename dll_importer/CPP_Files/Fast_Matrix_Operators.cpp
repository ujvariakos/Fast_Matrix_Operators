#include "pch.h"
#include <stdexcept>
#include "Vector.h"
#include "Matrix.h"
//#include <exception>
using namespace std;

#define LIBDLL extern "C" __declspec(dllexport)

LIBDLL float* vector_add(float* v0, int size_v0, float* v1, int size_v1) {
    Vector vec1 = Vector(v0, size_v0);
    Vector vec2 = Vector(v1, size_v1);
    Vector vec3 = vec1 + vec2;
    return vec3.get_vector_elements();
}

LIBDLL float* vector_sub(float* v0, int size_v0, float* v1, int size_v1) {
    Vector vec1 = Vector(v0, size_v0);
    Vector vec2 = Vector(v1, size_v1);
    Vector vec3 = vec1 - vec2;
    return vec3.get_vector_elements();
}

LIBDLL float* vector_mult(float* v0, int size_v0, float s) {
    Vector vec1 = Vector(v0, size_v0);
    Vector vec2 = vec1 * s;
    return vec2.get_vector_elements();
}

LIBDLL float* vector_div(float* v0, int size_v0, float s) {
    Vector vec1 = Vector(v0, size_v0);
    Vector vec2 = vec1 / s;
    return vec2.get_vector_elements();
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
    free(vectors_m0);
    free(vectors_m1);
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
    free(vectors_m0);
    free(vectors_m1);
    return res.serialize();
}

LIBDLL float* matrix_mul_scalar(float* matrix_elements_m0, int vector_number_m0, int vector_size_m0, float s) {
    Vector* vectors_m0 = (Vector*)malloc(vector_number_m0 * sizeof(Vector));
    for (int i = 0; i < vector_number_m0; i++) {
        *(vectors_m0 + i) = Vector((matrix_elements_m0 + i * vector_size_m0), vector_size_m0);
    }
    Matrix m0 = Matrix(vectors_m0, vector_number_m0);
    Matrix res = m0 * s;
    free(vectors_m0);
    return res.serialize();
}


LIBDLL float* matrix_mul_m(float* matrix_elements_m0, int vector_number_m0, int vector_size_m0, float* matrix_elements_m1, int vector_number_m1, int vector_size_m1) {
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
    Matrix res = m0 * m1;
    free(vectors_m0);
    free(vectors_m1);
    return res.serialize();
}

LIBDLL float* matrix_div_scalar(float* matrix_elements_m0, int vector_number_m0, int vector_size_m0, float s) {
    Vector* vectors_m0 = (Vector*)malloc(vector_number_m0 * sizeof(Vector));
    for (int i = 0; i < vector_number_m0; i++) {
        *(vectors_m0 + i) = Vector((matrix_elements_m0 + i * vector_size_m0), vector_size_m0);
    }
    Matrix m0 = Matrix(vectors_m0, vector_number_m0);
    Matrix res = m0 / s;
    free(vectors_m0);
    return res.serialize();
}

LIBDLL float matrix_determinant(float* matrix_elements_m0, int vector_number_m0, int vector_size_m0) {
    Vector* vectors_m0 = (Vector*)malloc(vector_number_m0 * sizeof(Vector));
    for (int i = 0; i < vector_number_m0; i++) {
        *(vectors_m0 + i) = Vector((matrix_elements_m0 + i * vector_size_m0), vector_size_m0);
    }
    Matrix m0 = Matrix(vectors_m0, vector_number_m0);
    float val = m0.det(m0, 1.0, 1.0);
    return val;
}

LIBDLL float* matrix_invert(float* matrix_elements_m0, int vector_number_m0, int vector_size_m0) {
    Vector* vectors_m0 = (Vector*)malloc(vector_number_m0 * sizeof(Vector));
    for (int i = 0; i < vector_number_m0; i++) {
        *(vectors_m0 + i) = Vector((matrix_elements_m0 + i * vector_size_m0), vector_size_m0);
    }
    Matrix m0 = Matrix(vectors_m0, vector_number_m0);
    float det = m0.det(m0, 1.0, 1.0);
    Matrix m1 = m0.adj();
    Matrix m1t = m1.transpose();
    Matrix ret = m1t/det;
    return ret.serialize();
}
