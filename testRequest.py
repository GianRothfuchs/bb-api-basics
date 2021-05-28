# -*- coding: utf-8 -*-
"""
Created on Fri May 28 15:50:17 2021
@author: giro
"""

from xbbg import blp

out = blp.bdp(tickers=['BE0002644251 Corp','FR0011951771 Corp'],flds=['SHORT_AND_LONG_TERM_DEBT','BS_TOT_ASSET'])

history = blp.bdh(tickers='LEGATRUU Index', 
        flds=['PX_LAST'],
        start_date='12/31/20', 
        end_date='05/28/21',
        Per='W', Fill='P', Days='A')

print(history)