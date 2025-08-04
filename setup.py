
import setuptools

with open('README.md', encoding='utf-8') as file:
    readme = file.read()

setuptools.setup(
    name='fastapi-okta',
    version='1.3.0',
    description='Easy auth0.com integration for FastAPI',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/alliance-genome/agr_fastapi_okta',
    author='Alliance Blue Team',
    license='MIT',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    package_data={'': ['py.typed']},
    python_requires='>=3.11',
    install_requires=['fastapi>=0.95.2', 'python-jose>=3.4.0']
)
