from setuptools import setup
setup(
  name = 'censuspy',
  packages = ['censuspy'], 
  version = '0.2',
  license='MIT',
  description = 'Lightweight wrapper to access gov data',
  author = 'Aadhi Manivannan',
  author_email = 'dnrkaseff360@gmail.com',
  url = 'https://github.com/DnrkasEFF/censuspy',
  download_url = 'https://github.com/DnrkasEFF/censuspy/archive/0.2.tar.gz',
  keywords = ['census', 'python', 'wrapper'],
  install_requires=[
          'requests',
      ],
  classifiers = [],
)