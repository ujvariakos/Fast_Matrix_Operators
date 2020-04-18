#include "pch.h"

using namespace std;

#define LIBDLL extern "C" __declspec(dllexport)

LIBDLL int sum(int a, int b) {
	return a + b;
}