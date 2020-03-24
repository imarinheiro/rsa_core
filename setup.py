import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="rsa_core",
    version="1.0.0",
    author="Iago Marinheiro Elias",
    author_email="go.marinheiro@gmail.com",
    description="Simplified RSA implementation in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imarinheiro/rsacore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=['sympy'],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'keygen=rsa.keygen:main',
            'cipher=rsa.cipher:main',
            'decipher=rsa.decipher:main',
            'encryptor=rsa.encryptor:main',
            'decryptor=rsa.decryptor:main',
            'tests=tests.tests:main'
        ],
    },
)
