<a href="https://datahub.io/core/edgar"><img src="https://badgen.net/badge/icon/View%20on%20datahub.io/orange?icon=https://datahub.io/datahub-cube-badge-icon.svg&label&scale=1.25)" alt="badge" /></a>

Securities and Exchange Commission (SEC) EDGAR database. EDGAR contains
regulatory filings from publicly-traded US corporations including their annual
and quarterly reports:

[edgar]: http://www.sec.gov/edgar.shtml

> All companies, foreign and domestic, are required to file registration
> statements, periodic reports, and other forms electronically through EDGAR.
> Anyone can access and download this information for free. [from the [SEC
> website][edgar]]

## Human Interface

See <http://www.sec.gov/edgar/searchedgar/companysearch.html>

<img src="http://webshot.okfnlabs.org/api/generate?url=http%3A%2F%2Fwww.sec.gov%2Fedgar%2Fsearchedgar%2Fcompanysearch.html" />

## Bulk Data

~~EDGAR provides bulk access via FTP: <ftp://ftp.sec.gov/> - [official
documentation][ftp-doc]. We summarize here the main points.~~

Each company in EDGAR gets an identifier known as the CIK which is a 10 digit
number. You can find the CIK by searching EDGAR using a name of stock market
ticker.

For example, [searching for IBM by ticker][ibm-search] shows us that
the the CIK is `0000051143`.

Note that leading zeroes are often omitted ~~(e.g. in the ftp access)~~ so this
would become `51143`.

[ibm-search]: http://www.sec.gov/cgi-bin/browse-edgar?CIK=ibm&action=getcompany

<img src="http://webshot.okfnlabs.org/api/generate?url=http%3A%2F%2Fwww.sec.gov%2Fcgi-bin%2Fbrowse-edgar%3FCIK%3Dibm%26action%3Dgetcompany&width=1024&height=768" />

Next each submission receives an 'Accession Number' (acc-no). For example,
IBM's quarterly financial filing (form 10-Q) in October 2013 had accession
number: `0000051143-13-000007`.

### HTTPS File Paths

Given a company with CIK (company ID) XXX (omitting leading zeroes) and
document accession number YYY (acc-no on search results) the path would be:

File paths are of the form:

    /edgar/data/XXX/YYY.txt

For example, for the IBM data above it would be:

~~<ftp://ftp.sec.gov/edgar/data/51143/0000051143-13-000007.txt>~~
<https://www.sec.gov/Archives/edgar/data/51143/0000051143-13-000007.txt>

EDGAR has retired HTTP services. Instead use the HTTPS equivalent.

<https://www.sec.gov/Archives/edgar/data/51143/0000051143-13-000007.txt>

Note, if you are looking for a nice HTML version you can find it at in the
Archives section with a similar URL (just add -index.html):

<http://www.sec.gov/Archives/edgar/data/51143/000005114313000007/0000051143-13-000007-index.htm>

### Indices

If you want to get a list of all filings you'll want to grab an Index. As the help page explains:

> The EDGAR indices are a helpful resource for HTTPS retrieval, listing the
> following information for each filing: Company Name, Form Type, CIK, Date
> Filed, and File Name (including folder path).
> 
> Four types of indexes are available:
> 
> * company — sorted by company name
> * form — sorted by form type
> * master — sorted by CIK number
> * XBRL — list of submissions containing XBRL financial files, sorted by CIK
>   number; these include Voluntary Filer Program submissions

URLs are like:

~~<ftp://ftp.sec.gov/edgar/full-index/2008/QTR4/master.gz>~~
<https://www.sec.gov/Archives/edgar/full-index/2008/QTR4/master.gz>

That is, they have the following general form:

    ~~ftp://ftp.sec.gov/edgar/full-index/{YYYY}/QTR{1-4}/{index-name}.[gz|zip]~~
    https://www.sec.gov/Archives/edgar/full-index/{YYYY}/QTR{1-4}/{index-name}.[gz|zip]

So for XBRL in the 3rd quarter of 2010 we'd do:

~~<ftp://ftp.sec.gov/edgar/full-index/2010/QTR3/xbrl.gz>~~
<https://www.sec.gov/Archives/edgar/full-index/2010/QTR3/xbrl.gz>

~~[ftp-doc]: https://www.sec.gov/edgar/searchedgar/ftpusers.htm~~

### CIK lists and lookup

There's a full list of all companies along with their CIK code here: <http://www.sec.gov/edgar/NYU/cik.coleft.c>

If you want to look up a CIK or company by its ticker you can do the following query against the normal search system:

<http://www.sec.gov/cgi-bin/browse-edgar?CIK=ibm&Find=Search&owner=exclude&action=getcompany&output=atom>

Then parse the atom to grab the CIK. (If you prefer HTML output just omit output=atom).

There is also a full-text company name to CIK lookup here:

<http://www.sec.gov/edgar/searchedgar/cik.htmL>

(Note this does a POST to a 'text' API at <http://www.sec.gov/cgi-bin/cik.pl.c>)

## Parsing XBRL Data

See `scripts` and README file there.

## References

* CorpWatch have an excellent API and DB dump covering a lot of EDGAR info - see the [CorpWatch DataHub Entry][corpwatch]

[corpwatch]: http://datahub.io/dataset/corpwatch
