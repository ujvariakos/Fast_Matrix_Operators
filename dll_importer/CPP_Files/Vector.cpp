#include "pch.h"
#include "Vector.h"
#include <stdexcept>
using namespace std;

Vector::Vector(float* vector_elements, int size_v)
{
//	this->vector_elements = (float*)malloc(size_v * sizeof(float));
//	for (int i = 0; i < size_v; i++) {
//        *(this->vector_elements + i) = *(vector_elements + i);
//    }
    this->vector_elements = vector_elements;
//	for()
	this->size_v = size_v;

}

Vector::~Vector()
{

}

//void Vector::free_elements(){
//    free(this->vector_elements);
//}



Vector Vector::operator+(Vector v)
{
    float* ret_v = (float*)malloc(this->size_v * sizeof(float));
    if (this->size_v != v.get_size_v()) {
        throw std::invalid_argument("vectors length are different");
        //          throw MyException()
    }
    else {
        for (int i = 0; i < this->size_v; i++) {
            *(ret_v + i) = *(this->vector_elements + i) + *(v.get_vector_elements() + i);
        }
    }
    Vector ret = Vector(ret_v, this->size_v);
    free(ret_v);
	return Vector(ret_v, this->size_v);
}

Vector Vector::operator-(Vector v)
{
    float* ret_v = (float*)malloc(this->size_v * sizeof(float));
    if (this->size_v != v.get_size_v()) {
        throw std::invalid_argument("vectors length are different");
        //          throw MyException()
    }
    else {
        for (int i = 0; i < this->size_v; i++) {
            *(ret_v + i) = *(this->vector_elements + i) - *(v.get_vector_elements() + i);
        }
    }
    Vector ret = Vector(ret_v, this->size_v);
    free(ret_v);
	return Vector(ret_v, this->size_v);
}

Vector Vector::operator*(float s)
{
    float* ret_v = (float*)malloc(this->size_v * sizeof(float));
    for (int i = 0; i < this->size_v; i++) {
        *(ret_v + i) = *(this->vector_elements + i) * s;
    }

    Vector ret = Vector(ret_v, this->size_v);
    free(ret_v);
	return Vector(ret_v, this->size_v);
}

Vector Vector::operator/(float s)
{
    if (s == 0) {
        throw std::invalid_argument("scalar can not be 0");
    }
    float* ret_v = (float*)malloc(this->size_v * sizeof(float));
    for (int i = 0; i < this->size_v; i++) {
        *(ret_v + i) = *(this->vector_elements + i) / s;
    }

    Vector ret = Vector(ret_v, this->size_v);
    free(ret_v);
	return Vector(ret_v, this->size_v);
}

float* Vector::get_vector_elements()
{
	return this->vector_elements;
}

int Vector::get_size_v()
{
	return this->size_v;
}
