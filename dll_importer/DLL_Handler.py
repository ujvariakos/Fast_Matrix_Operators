from ctypes import *
from pathlib import Path
import subprocess
import os

class DLL_Handler:

    def __init__(self):
        # 64 bit architecture
        if sizeof(c_voidp) == 8:
            self.is64 = True
        else:
            self.is64 = False
        if self.is64:
            self.cl_exe = r"c:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC/Tools\MSVC\14.25.28610\bin\Hostx64\x64\cl.exe"
            self.vcvars_bat = r"c:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars64.bat"
        else:
            self.cl_exe = r"c:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.25.28610\bin\Hostx86\x86\cl.exe"
            self.vcvars_bat = r"c:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvars32.bat"
        if not os.path.exists(Path(self.cl_exe)):
            msg = "Please set cl.exe path correctly (hint:" + self.cl_exe + ") :"
            self.cl_exe = input(msg)
        if not os.path.exists(Path(self.cl_exe)):
            raise ValueError("cl.exe is not exists")
        if not os.path.exists(Path(self.vcvars_bat)):
            msg = "Please set vcvars.bat path correctly (hint:" + self.vcvars_bat + ") :"
            self.vcvars_bat = input(msg)
        if not os.path.exists(Path(self.vcvars_bat)):
            raise ValueError("vcvars.bat is not exists")
        # current_file_path = os.path.abspath(__file__)
        current_folder_dir = Path(__file__).parent.absolute()
        self.cwd = os.path.join(current_folder_dir,r'generated_files')
        print(self.cwd)
        # self.cwd_str = str(self.cwd)
        # self.cwd_str = r"d:/PythonProjects/Fast_Matrix_Operators_Project/dll_importer/generated_files/"
        # self.cwd = Path(self.cwd_str)
        # self.Fast_Matrix_Operators_Cpp = r"d:\PythonProjects\Fast_Matrix_Operators_Project\dll_importer\CPP_Files\Fast_Matrix_Operators.cpp"
        self.Fast_Matrix_Operators_Cpp = os.path.join(current_folder_dir,r'CPP_Files','Fast_Matrix_Operators.cpp')
        self.Vector_Cpp = os.path.join(current_folder_dir,r'CPP_Files','Vector.cpp')
        self.Matrix_Cpp = os.path.join(current_folder_dir, r'CPP_Files', 'Matrix.cpp')
        self._compile_dll()

    def _compile_dll(self):
        # " /LD " + "d:\PythonProjects\Fast_Matrix_Operators_Project\dll_importer\CPP_Files\Vector.cpp "
        cmd = r'"' + self.vcvars_bat + r'"' + " " + "&&" + " " + r'"' + self.cl_exe + r'"' +\
            " " + "/LD " + str(self.Fast_Matrix_Operators_Cpp) + " " + str(self.Matrix_Cpp) + " " + str(self.Vector_Cpp)
        proc = subprocess.Popen(cmd, cwd=self.cwd)
        proc.wait()

    def get_dll(self):
        fast_matrix_operators_dll_path = str(os.path.join(self.cwd,"Fast_Matrix_Operators.dll"))
        # fast_matrix_operators_dll = cdll.LoadLibrary(r"d:\PythonProjects\Fast_Matrix_Operators_Project\dll_importer\generated_files\Fast_Matrix_Operators.dll")
        fast_matrix_operators_dll = cdll.LoadLibrary(fast_matrix_operators_dll_path)
        return fast_matrix_operators_dll