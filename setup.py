from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
import os
import platform

os.environ["CC"]= "/usr/bin/g++"

if platform.system() == 'Darwin':
    extra_compile_args = ["-std=c++03"]
    extra_link_args = ["-std=c++03"]
else:
    extra_compile_args = []
    extra_link_args = []

setup(
    name='pyicp',
    ext_modules=cythonize(
        Extension(
            "pyicp",
            sources=["python/pyicp.pyx", "python/pyicpp.cpp"],
            include_dirs=[np.get_include(), "api/"],
	    language="c++",
            extra_compile_args=extra_compile_args+['-L./lib/', '-licp'],
            extra_link_args=extra_link_args+['-L./lib/', '-licp']
        )
    ),
    install_requires=["numpy"]
)

