import financial_fundamentals.edgar as edgar
from financial_fundamentals.xbrl import XBRLDocument, InstantContext,\
            DurationContext, XBRLMetricParams
def ex():
    print 'Calculating key accounting figures for Apple (2012 filing)'
    ticker = 'aapl'
    # filings = edgar.get_filings(symbol=ticker, filing_type='10-Q')
    # filing = filings[filings.bisect(date(2013, 1, 23)) - 1]
    # print filing

    url = 'http://www.sec.gov/Archives/edgar/data/320193/000119312513022339/aapl-20121229.xml'
    doc = XBRLDocument.gets_XBRL_from_edgar(xbrl_url=url)
    # filing = Filing(filing_date=None, document=xbrl_document, next_filing=None)

    tags = [
        # short-name, tagname, 'd/i' = duration or instance
        ['assets', 'us-gaap:Assets', 'i'],
        ['liabilites', 'us-gaap:Liabilities', 'i'],
        ['shares', 'dei:EntityCommonStockSharesOutstanding', 'i'],
        ['equity', 'us-gaap:StockholdersEquity', 'i'],
        ['eps', 'us-gaap:EarningsPerShareDiluted', 'd']
        ]
    out = {}
    for tag in tags:
        context = DurationContext if tag[2] == 'd' else InstantContext
        metric_params = XBRLMetricParams(possible_tags=[tag[1]],
            context_type=context
            )
        out[tag[0]] = doc.latest_metric_value(metric_params=metric_params)
    out['book'] = out['assets'] - out['liabilites']
    out['book-ps'] = out['book'] / out['shares']
    for k in out:
        print k, ': ', out[k]


# experiment with pysec library
def pysec_ex():
    # import vendor/pysec/xbrl
    fp = 'tmp/0001213900-13-000794.txt'
    docs = getxbrl(open(fp))
    print len(docs)
    # print docs[0][:30]
    parsed = xbrl.XBRL(docs[0])
    print parsed.fields

def getxbrl(fo):
    docs = []
    out = ''
    inxbrl = False
    for line in fo.readlines():
        if line == '</XBRL>\n':
            inxbrl = False
            docs.append(out)
            out = ''
        if inxbrl:
            out += line
        if line == '<XBRL>\n':
            inxbrl = True
    return docs


if __name__ == '__main__':
    ex()

