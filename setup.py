from setuptools import find_packages, setup
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]

setup(
name='MLproject',
version='0.0.1',
author='Satya',
author_email='kumarisatyasingh22@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)