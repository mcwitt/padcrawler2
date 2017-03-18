from setuptools import setup

package = 'padfinder'
version = '0.1'

setup(name=package,
      version=version,
      description="scraper and data model for apartment hunting",
      url='https://github.com/mcwitt/padfinder',
      install_requires=[
          'psycopg2',
          'scrapy',
          'sqlalchemy'
      ])
