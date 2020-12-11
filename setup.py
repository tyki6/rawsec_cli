import setuptools

with open('README.md') as f:
    long_description = f.read()
f.close()

with open('dev-requirements.txt') as f:
    dev_requires = [line.strip() for line in f]
    f.close()

with open('requirements.txt') as f:
    install_requires = [line.strip() for line in f]
    f.close()

setuptools.setup(
    name='rawsec',
    version='1.0.0',
    author='mBouamama',
    author_email='matthieubouamama@gmail.com',
    description="Cli for searching tools & resources on rawsec's CyberSecrity Inventory",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mBouamama/rawsec_cli',
    install_requires=install_requires,
    entry_points={'console_scripts': ['rawsec = rawsec_cli.cli.cli:cli']},
    extras_require={'dev': dev_requires},
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.6',
)
