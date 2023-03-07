from setuptools import setup

setup(
    name='aws-pyspark',
    version='0.0.1',
    description='A Pyspark AWS Kafka Program.',
    package_data={'': ['src/*']},
    include_package_data=True,
)


"""
#Setup For Spacy Below
import os
def installspacylibs():
    try:
        os.system("python -m spacy download en_core_web_sm")
    except:
        pass
    try:
        os.system("python3 -m spacy download en_core_web_sm")
    except:
        pass
"""