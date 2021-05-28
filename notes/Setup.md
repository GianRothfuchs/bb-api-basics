# Setup

The following Steps are needed to integrate Bloomberg API in Python. This assumes Bloomberg is already installed. Please note links may change:
1. pip install --index-url=https://bcms.bloomberg.com/pip/simple/ blpapi
2. pip install xbbg
3. Download "C++ Supported Release" from: https://www.bloomberg.com/professional/support/api-library/
	3.1 run $ where python
	3.2 get the Anaconda location of python.exe
	3.3 copy the dowloaded files bin/blpapi3_32.dll and bin/blpapi3_64.dll to the Anaconda location
4. To use: > from xbbg import blp
