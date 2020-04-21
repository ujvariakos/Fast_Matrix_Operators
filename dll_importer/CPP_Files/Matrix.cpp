#include "pch.h"
#include "Matrix.h"
#include <stdexcept>
using namespace std;


Matrix::Matrix(Vector* vectors, int vector_number)
{
    this->vectors = vectors;
    this->vector_number = vector_number;
    this->vector_size = vectors->get_size_v();
    for (int i = 0; i < vector_number; i++) {
        if (this->vector_size != (vectors + i)->get_size_v()) {
            throw std::invalid_argument("Can not create different matrix with different vector size");
        }

    }
}

Matrix::~Matrix()
{
//    free(this->vectors);
}

float* Matrix::serialize()
{
    float* data = (float*)malloc(this->vector_number * this->vector_size * sizeof(float));
    for (int i = 0; i < this->vector_number; i++) {
        for (int k = 0; k < this->vector_size; k++) {
            *(data + ((i * this->vector_size) + k)) = *((((this->vectors) + i)->get_vector_elements()) + k);
        }
    }
    return data;
}

Matrix Matrix::operator+(Matrix m)
{
    if (this->vector_number != m.get_vector_number()) {
        throw std::invalid_argument("different matrix size");
    }
    if (this->vector_size != m.get_vector_size()) {
        throw std::invalid_argument("different vector size");
    }

    Vector* vectors = (Vector*)malloc(this->vector_number * sizeof(Vector));
    for (int i = 0; i < this->vector_number; i++) {

        *(vectors + i) = *(this->vectors + i) + *(m.get_vectors() + i);
    }
    Matrix matrix = Matrix(vectors, this->vector_number);
    free(vectors);
    return matrix;
}

Matrix Matrix::operator-(Matrix m)
{
    if (this->vector_number != m.get_vector_number()) {
        throw std::invalid_argument("different matrix size");
    }
    if (this->vector_size != m.get_vector_size()) {
        throw std::invalid_argument("different vector size");
    }

    Vector* vectors = (Vector*)malloc(this->vector_number * sizeof(Vector));
    for (int i = 0; i < this->vector_number; i++) {

        *(vectors + i) = *(this->vectors + i) - *(m.get_vectors() + i);
    }
    Matrix matrix = Matrix(vectors, this->vector_number);
    free(vectors);
    return matrix;
}

Matrix Matrix::operator*(float s)
{
    Vector* vectors = (Vector*)malloc(this->vector_number * sizeof(Vector));
    for (int i = 0; i < this->vector_number; i++) {

        *(vectors + i) = *(this->vectors + i) * s;
    }
    Matrix matrix = Matrix(vectors, this->vector_number);
//    free(vectors);
    return matrix;
}

Matrix Matrix::operator*(Matrix m)
{
    //if (this->vector_number != m.get_vector_size()) {
    //    throw std::invalid_argument("invalid matrix size");
    //}
    if (this->vector_size != m.get_vector_number()) {
        throw std::invalid_argument("invalid size");
    }

    Vector* vectors = (Vector*)malloc(this->vector_number * sizeof(Vector));
    for (int i = 0; i < this->vector_number; i++) {
        Vector v = *(m.get_vectors() + 0) * *((this->vectors + i)->get_vector_elements() + 0);
        for (int k = 0; k < this->vector_size; k++) {
            if (k == 0) {
                // Nope
            }
            else {
                v = v + *(m.get_vectors() + k) * *((this->vectors + i)->get_vector_elements() + k);
            }
        }
        *(vectors + i) = v;

    }
    Matrix matrix = Matrix(vectors, this->vector_number);
//    free(vectors);
    return matrix;
}

Matrix Matrix::operator/(float s)
{
    if (s == 0) {
        throw std::invalid_argument("scalar can not be 0");
        // throw MyException();
    }
    Vector* vectors = (Vector*)malloc(this->vector_number * sizeof(Vector));
    for (int i = 0; i < this->vector_number; i++) {

        *(vectors + i) = *(this->vectors + i) / s;
    }
    Matrix matrix = Matrix(vectors, this->vector_number);
    free(vectors);
    return matrix;
}

float Matrix::det(Matrix m, float asign, float amul_value)
{
    float ret = 0.0;
    if (m.get_vector_number() != m.get_vector_size()) {
        throw std::invalid_argument("matrix is not square");
    }
    if (this->vector_size == 1) {
        return *this->vectors->get_vector_elements();
    }
    else if (this->vector_size == 2) {
        float det = *this->vectors->get_vector_elements() * *((this->vectors + 1)->get_vector_elements() + 1) - *((this->vectors + 1)->get_vector_elements() + 0) * *((this->vectors + 0)->get_vector_elements() + 1);
        return asign * det * amul_value;
    }
    else {
        for (int i = 0; i < m.get_vector_size(); i++) {
            float mul_value = *(m.get_vectors()->get_vector_elements() + i);
            float sign = 1.0;
            if (i % 2 != 0) {
                sign = -1.0;
            }
            Vector* vectors = (Vector*)malloc((m.get_vector_number() - 1) * sizeof(Vector));
            for (int row = 1; row < m.get_vector_number(); row++) {
                float* elements = (float*)malloc((m.get_vector_number() - 1) * sizeof(float));
                for (int col = 0; col < m.get_vector_size(); col++) {
                    if (i > col) {
                        *(elements + col) = *((m.get_vectors() + row)->get_vector_elements() + col);
                    }
                    else if (i < col) {
                        *(elements + col - 1) = *((m.get_vectors() + row)->get_vector_elements() + col);
                    }
                    else {
                        // NOPE

                    }
                }
                *(vectors + row - 1) = Vector(elements, (m.get_vector_size() - 1));
                //free(elements);
            }
            Matrix new_m = Matrix(vectors, m.get_vector_number() - 1);
            ret = ret + asign*amul_value*new_m.det(new_m, sign, mul_value);
            free(vectors);
        }
        return ret;
    }
}

Matrix Matrix::transpose()
{
    Vector* vectors = (Vector*)malloc((this->vector_size) * sizeof(Vector));
    for (int row = 0; row < this->vector_size; row++) {
        float* elements = (float*)malloc(this->vector_number * sizeof(float));
        for (int col = 0; col < this->vector_number; col++) {
            *(elements + col) = *((this->vectors + col)->get_vector_elements() + row);
        }
        *(vectors + row) = Vector(elements, this->vector_number);
    }
    return Matrix(vectors, (this->vector_size));
}

Matrix Matrix::adj()
{
    Vector* new_vectors = (Vector*)malloc((this->vector_number) * sizeof(Vector));
    for (int col = 0; col < this->vector_number; col++) {
        float* new_elements = (float*)malloc(this->vector_size * sizeof(float));
        for (int row = 0; row < this->vector_size; row++) {
            float sign = 1;
            if ((col * this->vector_size +row) %2 != 0) {
                sign = -1;
            }
            Vector* vectors = (Vector*)malloc((this->vector_number - 1) * sizeof(Vector));
            for (int col1 = 0; col1 < this->vector_number; col1++) {
                float* elements = (float*)malloc((this->vector_size - 1) * sizeof(float));
                for (int row1 = 0; row1 < this->vector_size; row1++) {
                    if (row < row1) {
                        *(elements + row1 - 1) = *((this->vectors + col1)->get_vector_elements() + row1);
                    }
                    else if (row > row1) {
                        *(elements + row1) = *((this->vectors + col1)->get_vector_elements() + row1);
                    }
                }
                if (col < col1) {
                    *(vectors + col1 - 1) = Vector(elements, (this->vector_size - 1));
                }
                else if (col > col1) {
                    *(vectors + col1) = Vector(elements, (this->vector_size - 1));
                }
            }
            Matrix m_new = Matrix(vectors, (this->vector_number - 1));
            *(new_elements + row) = m_new.det(m_new, sign, 1);
        }
        *(new_vectors + col) = Vector(new_elements, this->vector_number);
    }
    return Matrix(new_vectors, (this->vector_size));
}

Vector* Matrix::get_vectors()
{
    return this->vectors;
}

int Matrix::get_vector_number()
{
    return this->vector_number;
}

int Matrix::get_vector_size()
{
    return this->vector_size;
}


