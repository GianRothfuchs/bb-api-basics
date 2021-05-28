# bb-api-basics
Basics on how to integrate Bloomberg API in Python. The very first time the [Setup](notes/Setup.md) has to be performed. 

# Package xbbg

The basic query commands are similar to the Excel version:

```python
from xbbg import blp

out = blp.bdp(	tickers=['BE0002644251 Corp','FR0011951771 Corp'],
				flds=['SHORT_AND_LONG_TERM_DEBT','BS_TOT_ASSET'])

history = blp.bdh(	tickers='LEGATRUU Index', 
					flds=['PX_LAST'],
					start_date='12/31/20', 
					end_date='05/28/21')
```

More examples are provided on [GitHub](https://github.com/alpha-xone/xbbg).