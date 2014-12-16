<?php
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

// ******* UPDATE DATABASE ********
if(isset($_POST['update']))
{
   
    $retval = $conn->query($sql);
    if(! $retval )
    {
      die('Could not update data: ' . mysql_error());
    }
    
    echo "<script> reloadPage(); </script>";;
}


// ******* READ FROM DATABASE ********
$sql = "SELECT avg_temp, current_temp, mode, status FROM projectDB";
$result = $conn->query($sql);

if ($result->num_rows > 0) 
{
    // output data of each row
    while($row = $result->fetch_assoc()) {
        $avg_temp = $row["avg_temp"];
        $current_temp = $row["current_temp"];
        $mode = $row["mode"];
        $current_mode = $row["status"];
    }
} else 
{
    echo "0 results";
}

// Set the text for set mode according to fetched value.
if ($mode == 0)
{
  $mode = "Heating";
}
elseif ($mode == 1)
{
  $mode = "Cooling";
}
elseif ($mode == 2)
{
  $mode = "Default";
}
elseif ($mode == 3)
{
  $mode = "Off";
}
else
{
  $mode = "Error";
}

// Set the text for current status according to fetched value.
if ($current_mode == 0)
{
  $current_mode = "Heating";
}
elseif ($current_mode == 1)
{
  $current_mode = "Cooling";
}
elseif ($current_mode == 2)
{
  $current_mode = "Idle";
}
else
{
  $current_mode = "Error";
}

// Close connection.
$conn->close();
?>

<html>
  
<head>
    <title>
      TempNet - Dashboard
    </title>
    
    <link href="http://fonts.googleapis.com/css?family=Lato:100,300,400,700" media="all" rel="stylesheet" type="text/css" />
    <link href="stylesheets/bootstrap.min.css" media="all" rel="stylesheet" type="text/css" />
    <link href="stylesheets/font-awesome.css" media="all" rel="stylesheet" type="text/css" />
    <link href="stylesheets/style.css" media="all" rel="stylesheet" type="text/css" />
    
    <script src="../../../code.jquery.com/jquery-1.10.2.min.js" type="text/javascript"></script><script src="../../../code.jquery.com/ui/1.10.3/jquery-ui.js" type="text/javascript"></script><script src="javascripts/bootstrap.min.js" type="text/javascript"></script><script src="javascripts/raphael.min.js" type="text/javascript">
    </script>
    <script src="javascripts/jquery.mousewheel.js" type="text/javascript"></script>
    <script src="javascripts/jquery.bootstrap.wizard.js" type="text/javascript"></script>
    <script src="javascripts/modernizr.custom.js" type="text/javascript"></script>
    <script src="javascripts/main.js" type="text/javascript"></script>
    <script src="javascripts/respond.js" type="text/javascript"></script>

    <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" name="viewport">
  </head>
  <body>
    <div class="modal-shiftfix">
      <!-- Header -->
            <div class="navbar scroll-hide">
              
              <div class="container-fluid main-nav clearfix">
                <div class="nav-collapse">
                  <ul class="nav">
                    
                      <a class="logo logoText" href="index.php">TempNet</a>
                    
                  </ul>
                </div>
              </div>
            </div>
      <!-- End Header -->
      <div class="container-fluid main-content">
        <!-- Main Stats -->
        <div class="row">
          <div class="col-lg-12">
            <div class="widget-container stats-container">
              <div class="col-md-3">
                <div class="number">
                  <?php echo $avg_temp; ?> <small>&deg;</small>
                </div>
                <div class="text">
                  Average temperature
                </div>
              </div>
              <div class="col-md-3">
                <div class="number">
                  <?php echo $current_temp; ?> <small>&deg;</small>
                </div>
                <div class="text">
                  Current set temperature
                </div>
              </div>
              <div class="col-md-3">
                <div class="number">
                  <?php echo $mode?>
                </div>
                <div class="text">
                  Set Mode
                </div>
              </div>
              <div class="col-md-3">
                <div class="number">
                  <?php echo $current_mode?>
                </div>
                <div class="text">
                  System status
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- End Main Stats -->
        <div class="row">
          <!-- Form -->
          <div class="col-md-12">
            <div class="row">
              <div class="col-lg-12">
                <div class="widget-container fluid-height clearfix">
                  <div class="heading">
                    <i class="icon-reorder"></i>Settings
                  </div>
                  <div class="widget-content padded">
                    <form method="post" action="form_submit.php" class="form-horizontal" onsubmit="reloadPage()">
                
                      <div class="form-group">
                        <label class="control-label col-md-2">Set temperature (F)&deg</label>
                        <div class="col-md-7">
                          <input name = "set_temp" id = "set_temp" class="form-control" placeholder="" type="text">
                        </div>
                      </div>
                     
                      <div class="form-group">
                        <label class="control-label col-md-2">Mode</label>
                        <div class="col-md-7">

                          <label class="radio-inline"><input name="mode" id="mode" type="radio" value="heating"><span>Heating</span></label>

                          <label class="radio-inline"><input name="mode" id="mode"  type="radio" value="cooling"><span>Cooling</span></label>

                          <label class="radio-inline"><input name="mode" id="mode"  type="radio" value="default" checked="checked"><span>Default</span></label>
                          
                          <label class="radio-inline"><input name="mode" id="mode"  type="radio" value="off"><span>Off</span></label>
                          
                        </div>
                      </div>
                      
                      <div class="form-group">
                        
                        <label class="control-label col-md-2"></label>
                        
                        <div class="col-md-7">
                          <button name ="update" class="btn btn-primary" type="submit">Submit </button>
                          <button class="btn btn-default-outline">Cancel</button>
                        </div>
                      
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- end Form-->
          
      </div>
    </div>
  </body>
</html>