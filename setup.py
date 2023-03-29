from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='Resemblyzer-Ideas',
    version='0.1.4',
    packages=find_packages(),
    package_data={
        'resemblyzer-ideas': ['pretrained.pt']
    },
    python_requires='>=3.5',
    install_requires=['librosa>=0.9.1',
                      'numpy>=1.10.1',
                      'webrtcvad>=2.0.10',
                      'torch>=1.0.1',
                      'scipy>=1.2.1',
                      'typing'],
    author='Christian Schäfer (original repo Corentin Jemine)',
    author_email='christian.schaefer@axelspringer.com',
    description='Analyze and compare voices with deep learning',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/as-ideas/Resemblyzer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
