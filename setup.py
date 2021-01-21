from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_caitlinkermen", # the name that you will install via pip
    version="1.0",
    author="Caitlin Anna Kermen",
    author_email="caitlinkermen@gmail.com",
    description="my first python environment",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/caitlinkermen/lambda_dspt9_test1",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)