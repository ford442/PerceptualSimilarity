
import setuptools
from setuptools import Extension,setup; 
from Cython.Build import cythonize;
from Cython.Compiler import Options
Options.infer_types = True
Options.language_level = 3
extensions = [Extension('lpips',['lpips/*.py'])];
setuptools.setup(
     name='lpips',  
     version='0.1',
     author="Richard Zhang",
     author_email="rizhang@adobe.com",
     description="LPIPS Similarity metric",
     packages=['lpips'],
     package_data={'lpips': ['weights/v0.0/*.pth','weights/v0.1/*.pth']},
     include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: BSD License",
         "Operating System :: OS Independent",
     ],
    ext_modules=cythonize(extensions),
 )
