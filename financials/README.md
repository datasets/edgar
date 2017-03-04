Financial Statement Data Sets

https://www.sec.gov/dera/data/financial-statement-data-sets.html

> The data sets below provide selected information extracted from exhibits to corporate financial reports filed with the Commission using eXtensible Business Reporting Language (XBRL). The information is presented without change from the "as filed" annual and quarterly financial reports submitted by each registrant. The data is presented in a flattened format to help users analyze and compare it. The data sets also contain additional fields including a company's Standard Industrial Classification to facilitate the data's use.
> 
> Data sets will be updated quarterly. Data contained in documents filed after 5:30PM Eastern on the last business day of a quarter will be included in the subsequent quarterly posting.
> 
> Annual and Quarterly Financial Statements (PDF, 175 kb) provides documentation of scope, organization, file formats and table definitions.

## Data

Data is provided in a quarterly basis in a zip file. Inside each zip file is a README plus data consisting of of 4 tables in tab-delimited CSV. The files are linked together with foreign-key links (see below).

The SEC readme.htm is cached here as `sec-readme.html`.

> **Note to self: This is a perfect dataset for data packagizing**

### Analysis

Here's an analysis of a recent quarterly release: http://www.sec.gov/data/financial-statements/2016q4.zip

```
readme.htm
sub.txt
num.txt
tag.txt
pre.txt
```

From the readme.htm:

> # Annual and Quarterly Financial Statements (AQFS)
> 
> The following data sets provide information extracted from EX-101 attachments submitted to the Commission in a flattened data format to assist users in more easily consuming the data for analysis. The data is sourced from selected information found in the XBRL tagged financial statements submitted by filers to the Commission.  These data sets currently include quarterly and annual numeric data appearing in the primary financial statements submitted by filers. Certain additional fields (e.g. Standard Industrial Classification (SIC)) used in the Commission’s EDGAR system are also included to help in supporting the use of the data.  The information has been taken directly from submissions created by each registrant, and the data is “as filed” by the registrant.  The information will be updated quarterly. Data contained in documents filed after 5:30pm EST on the last business day of the quarter will be included in the next quarterly posting.  
> 
> The data extracted from the XBRL submissions is organized into four data sets containing information about submissions, numbers, taxonomy tags, and presentation.  Each data set consists of rows and columns, and is provided as a tab-delimited TXT format file.  The data sets are as follows:
> 
> * SUB – Submission data set; this includes one record for each XBRL submission. The set includes fields of information pertinent to the submission and the filing entity. Information is extracted from the SEC’s EDGAR system and the filings submitted to the SEC by registrants.
> * NUM – Number data set; this includes one row for each distinct amount from each submission included in the SUB data set. The Number data set includes, for every submission, for each primary financial statement as it is rendered by the SEC Viewer/Previewer, all line item values.
> * TAG – Tag data set; includes defining information about each tag.  Information includes tag descriptions (documentation labels), taxonomy version information and other tag attributes.
> * PRE – Presentation data set; this provides information about how the tags and numbers were presented in the primary financial statements.

### Data Description

See the `sec-readme.html`.

### Links between tables

Data has foreign keys. See "Figure 1. Data relationships" in the `sec-readme.html`

Aside: you can tell from the readme inline css that this is an export from word!

