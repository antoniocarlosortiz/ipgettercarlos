from setuptools import setup

def readme():
	with open('README.rst') as f:
		return f.read()


setup(	name = 'ipgettercarlos',
		version = 	'0.1',
		description = 'a copy of ipgetter made by phoemur which basically does what the name says but improved to work',
		long_description = 'The same as the short descript',
		classifiers = [
			'Development Status :: 3 - Alpha',
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 2.7',
			'Operating System :: OS Dependent',
			'Topic :: Software Development :: Libraries :: Python Modules',
			'Topic :: System :: Networking',
			'Topic :: Utilities',
			'Environment :: Console',
			],
		keywords = 'ip getter tpain hiphop drake my anaconda dont want none',
		url = '',
		author = 'Antonio Carlos L. Ortiz',
		author_email = 'ortizantoniocarlos@gmail.com',
		license = 'MIT',
		packages = ['ipgettercarlos'],
		zip_safe = False)
