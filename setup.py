# will find all available packages in the directory we've created for this project
from setuptools import find_packages, setup
from typing import List

# "-e ." is typed at the end of requirements.txt and will automatically trigger setup.py
# when you "pip install -r requirements.txt" it tells your computer that setup.py is there, and automatically this will all run to build this project
# will build ml_project.egg-info
HYPHEN_E_DOT = '-e .'

# says the input parameter must be a string of the file path name, and must return a list of strings (the names of the packages/libraries to install)
def get_requirements(path_to_requirements_file:str)->List[str]:
    requirements = []

    with open(path_to_requirements_file) as file_object:
        requirements = file_object.readlines() # will read in each line with "\n" at the end of them
        requirements = [requirement.replace('\n', '') for requirement in requirements] 

        # since "-e ." is not actually a package, we don't want to read it in
        # just want to make sure that it links the requirement.txt file to the setup.py file
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

# add information on the metadata about the entire project here (name, description, etc.)
setup(name='ml-project',
      version='0.0.1', # since this is the first version
      author='Hilary',
      author_email='hilpresent@gmail.com',
      packages=find_packages(), # this does the work for you to gather all packages
      install_requires=get_requirements('requirements.txt'), # make a function to automatically do the installation of the packages we want
    )

# find_packages works by going into your directory and seeing how many folders have "__init__.py"
# as of now, the only folder with "__init__.py" in it is "src", so find_packages will consider src as a package itself and will try to build it