Get and analyse EDGAR filings in Python.

## Install

1. Install

    <https://github.com/andrewkittredge/financial_fundamentals>

2. Comment out vector_cache stuff in setup.py (not on pypi)

3. `pip install`

Now you can run:

    python edgar.py

## Library Review

Focus on python libraries (as I'm familiar with them).

* https://github.com/andrewkittredge/financial_fundamentals - clean and simple
* https://github.com/lukerosiak/pysec - somewhat raw and I struggled to get it working
* http://arelle.org/ - powerful - much more than parsing - and looks well
  maintained but I did not use as looked overly complex for my needs

### Scraping

Python-based

* https://github.com/rahulrrixe/SEC-Edgar
  * Simple scraper library to download companies periodic reports, filings and forms from EDGAR database.
  * Only supports 10-K, 10-Q, 8-K, 13-F
  * Have not tried. Overall looks quite basic

* https://github.com/edouardswiac/python-edgar
  * downloads the EDGAR fillings index from the SEC FTP. The index is comprised of IDX files. An IDX file is a csv-like file that contains the following information:
  * So this is only part of EDGAR

