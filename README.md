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

EDGAR provides bulk access via HTTP. See <https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm> for details.

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
