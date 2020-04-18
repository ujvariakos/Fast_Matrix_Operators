#pragma once
#ifndef VECTOR_H
#define VECTOR_H
#define LIBDLL extern "C" __declspec(dllexport)
class Vector
{
private:
	float* vector_elements;
	int size_v;
public:
	Vector(float* vector_elements, int size_v);
	~Vector();
	Vector operator + (Vector v);
	Vector operator - (Vector v);
	Vector operator * (float s);
	Vector operator / (float s);
	float* get_vector_elements();
	int get_size_v();
//	void free_elements();
};

#endif