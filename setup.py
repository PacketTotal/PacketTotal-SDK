import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='packettotal_sdk',
     version='0.2',
     scripts=['scripts/packettotal'],
     author="PacketTotal, LLC.",
     author_email="admin@packettotal.com",
     description="PacketTotal API client",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://packettotal.com",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache2 License",
         "Operating System :: OS Independent",
     ],
 )