import setuptools

setuptools.setup(
    name="hblfit",
    version="0.1.0",
    author="Lachlan Marnoch",
    #    short_description=long_description,
    url="https://github.com/Lachimax/hblfit",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "astropy",
        "matplotlib",
        "numpy",
    ],
    license='Attribution-NonCommercial-ShareAlike 4.0 International'
)
