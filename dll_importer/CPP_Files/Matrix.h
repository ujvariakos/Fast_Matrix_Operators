#ifndef MATRIX_H
#define MATRIX_H
#define LIBDLL extern "C" __declspec(dllexport)
#include "Vector.h"

class Matrix
{
private:
	Vector* vectors;
	int vector_number;
	int vector_size;
public:
	Matrix(Vector* vectors, int vector_number);
	~Matrix();
	float* serialize();
	Matrix operator + (Matrix m);
	Matrix operator - (Matrix m);
	//Vector operator * (float s);
	//Vector operator / (float s);
	Vector* get_vectors();
	int get_vector_number();
	int get_vector_size();
	//	void free_elements();
};

#endif