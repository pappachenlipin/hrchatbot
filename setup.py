import setuptools
__version__ = "0.0.0"
setuptools.setup(
    name = "hrchatbot",
    version = __version__,
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where = 'src')
    
)