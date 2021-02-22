import json
import cx_Oracle

# Oracle database connection string
enotice_connect_string = "anonymous/anonymous@cdbp"

# -- Select the most recent set of notices published
sql = """
SELECT revisions.ddocname AS ID
, docmeta.xfromdt AS "Notice Date"
, docmeta.xsubtp AS "Notice Type"
, docmeta.xcntntctgry1 AS "Application/permit type"
, docmeta.xcntymulti AS "County"
, docmeta.xsbjcttxt AS "Description"
, 'https'||'://permitting.sjrwmd.com/apps/idcplg?IdcService=GET_FILE&RevisionSelectionMethod=Latest&dDocName=' || revisions.ddocname AS "Notice Document"
FROM apps64.revisions
JOIN apps64.docmeta ON revisions.did = docmeta.did
WHERE docmeta.xprofiletrigger = 'ENotice'
AND docmeta.xfromdt = (SELECT MAX(xfromdt)
    FROM apps64.docmeta
    WHERE docmeta.xprofiletrigger = 'ENotice')"""

def load_db():
	# initialize a dictionary for the data
	return_dataset = []

	# open a connection to the database
	connection = cx_Oracle.connect(enotice_connect_string)

	# create a cursor to execute the query and place all the data in the dictionary
	cursor = connection.cursor()
	cursor.execute(sql)
	columns = [col[0] for col in cursor.description]
	cursor.rowfactory = lambda *args: dict(zip(columns, args))
	for row in cursor:
		return_dataset.append(row)

	# close the connection
	connection.close()
	
	# return the dictionary full of data from the query
	return return_dataset

db = load_db()