from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
import os

os.environ["CC"]= "/usr/bin/g++"

setup(
    name='pyicp',
    ext_modules=cythonize(
        Extension(
            "pyicp",
            sources=["python/pyicp.pyx", "python/pyicpp.cpp"],
            include_dirs=[np.get_include(), "api/"],
	    language="c++",
            extra_compile_args=["-std=c++03", "-mmacosx-version-min=10.9", '-L./lib/', '-licp'],
            extra_link_args=["-std=c++03", "-mmacosx-version-min=10.9", '-L./lib/', '-licp']
        )
    ),
    install_requires=["numpy"]
)

