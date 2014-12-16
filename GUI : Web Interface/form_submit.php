<?php
header( "refresh:3;url=http://sumitk.me/eceproject/index.php" );

$servername = "localhost";
$username = "timuster_ece4564";
$password = "netApps4564";
$dbname = "timuster_ece4564";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

// UPDATE
if(isset($_POST['update']))
{
    $set_temp = $_POST['set_temp'];

    $set_mode = $_POST['mode'];
    $set_mode_value = 100;
    if ($set_mode == "heating")
    {
      $set_mode_value = 0;
    }
    elseif ($set_mode == "cooling")
    {
      $set_mode_value = 1;
    }
    elseif ($set_mode == "default")
    {
      $set_mode_value = 2;
    }
    elseif ($set_mode == "off")
    {
      $set_mode_value = 3;
    }
    
    $sql = "UPDATE projectDB ".
           "SET current_temp = $set_temp ".
           "WHERE db_index = 0" ;

  
    $retval = $conn->query($sql);
    if(! $retval )
    {
      die('Could not update data 1 ' . mysql_error());
    }
    
    // UPDATE MODE

    $sql = "UPDATE projectDB ".
           "SET mode = $set_mode_value ".
           "WHERE db_index = 0" ;

    
    $retval = $conn->query($sql);
    if(! $retval )
    {
      die('Could not update mode ' . mysql_error());
    }
    
    echo "Updated. Reloading Dashboard.";
}

$conn->close();
?>