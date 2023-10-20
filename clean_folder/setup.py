from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    author='Daryna M.',
    author_email='dmirzagholi@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts':['clean=clean_folder.clean:start']}
)