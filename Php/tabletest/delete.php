<?php
/**************************************************************************************
 * delete row from database- delete.php
 * Author: Shane  <shane *at* hackosis *dot* com>
 * use this to learn, share, or what ever else floats your boat and finds your lost remote
 **************************************************************************************/
 
//Get database credentials
require 'config.php';

//Get the row ID to delete!
$column1 = $_GET['column1'];

// connect to the mysql database server.
mysql_connect ($dbhost, $dbusername, $dbuserpass);
//select the database
mysql_select_db($dbname) or die('Cannot select database');

//Set the query to return names of all employees
$query = "DELETE FROM postcodes WHERE postcode_id = '".$column1."';";

//Run the query
$result = mysql_query($query) or die(mysql_error());

//link variable is equal to the referring page
$link = $_SERVER['HTTP_REFERER'];
//sends a header directly to the browser telling it to redirect the user to the referring page
header("Location: $link");

?>
