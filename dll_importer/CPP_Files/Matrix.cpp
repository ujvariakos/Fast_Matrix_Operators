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
    return matrix;
}

Matrix Matrix::operator*(float s)
{
    Vector* vectors = (Vector*)malloc(this->vector_number * sizeof(Vector));
    for (int i = 0; i < this->vector_number; i++) {

        *(vectors + i) = *(this->vectors + i) * s;
    }
    Matrix matrix = Matrix(vectors, this->vector_number);
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
    return matrix;
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


