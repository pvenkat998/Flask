
	<?php
	// Connect to database server
	mysql_connect("mysql:dbname=eigyou_kikaku;host=192.168.5.124;charset=utf8", "eigyou_kikaku", "As6hV2K!k") or die (mysql_error ());

	// Select database
	mysql_select_db("eigyo_kikaku") or die(mysql_error());

	// SQL query
	$strSQL = "SELECT *
FROM 
raynos_nyuukin
WHERE
uriagesyubetu="–‘O’²¸"
AND
uchitairyuukingaku>0

AND
genzitennyuukinyoteibi< 	 "2018-02-02 00:00:01"";

	// Execute the query (the recordset $rs contains the result)
	$rs = mysql_query($strSQL);
	
	// Loop the recordset $rs
	// Each row will be made into an array ($row) using mysql_fetch_array
	while($row = mysql_fetch_array($rs)) {

	   // Write the value of the column FirstName (which is now in the array $row)
	  echo $row['FirstName'] . "<br />";

	  }

	// Close the database connection
	mysql_close();
	?>