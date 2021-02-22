# Endpoints
```
/enotices
/enotices/ENTC-2020102301009
```

## List search criteria
```
/enotices?NoticeType=Receipt
/enotices?County=Brevard
/enotices?ProjectType=ERP
/enotices?FromNoticeDate=23-OCT-2020&ToNoticeDate=23-OCT-2020
/enotices?TextSearch=duda
```
or
```
/enotices/noticetypes/<noticeType>
/enotices/counties/<county>
/enotices/projecttypes/<projectType>
```
- fromNoticeDate, toNoticeDate, and textSearch should always be query strings
- If fromNoticeDate and tNoticeDate are not specified, default to the most recent publish date

## Paging
Use query strings to support paging as the number of items can be lengthy
```
/api?page=1&page_size=25
```
```
{ 
totalResults: 255,
nextPage: "/api?page=3",
prevPage: "/api?page=1",
results: [...]
}
```

## Headers
```
X-TotalCount
X-NextPage
X-PrevPage
```