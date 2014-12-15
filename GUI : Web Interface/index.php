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
        //echo "Average Temp: " . $row["avg_temp"]. " - Current Temp: " . $row["current_temp"]. " " . $row["mode"]. "<br>";
        $avg_temp = $row["avg_temp"];
        $current_temp = $row["current_temp"];
        $mode = $row["mode"];
    }
} else 
{
    echo "0 results";
}

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

$conn->close();
?>

<html>
  
<head>
    <title>
      TempNet - Dashboard
    </title>
    <link href="http://fonts.googleapis.com/css?family=Lato:100,300,400,700" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/bootstrap.min.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/font-awesome.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/se7en-font.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/isotope.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/jquery.fancybox.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/fullcalendar.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/wizard.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/select2.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/morris.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/datatables.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/datepicker.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/timepicker.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/colorpicker.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/bootstrap-switch.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/daterange-picker.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/typeahead.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/summernote.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/pygments.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/style.css" media="all" rel="stylesheet" type="text/css" /><link href="stylesheets/color/green.css" media="all" rel="alternate stylesheet" title="green-theme" type="text/css" /><link href="stylesheets/color/orange.css" media="all" rel="alternate stylesheet" title="orange-theme" type="text/css" /><link href="stylesheets/color/magenta.css" media="all" rel="alternate stylesheet" title="magenta-theme" type="text/css" /><link href="stylesheets/color/gray.css" media="all" rel="alternate stylesheet" title="gray-theme" type="text/css" /><script src="../../../code.jquery.com/jquery-1.10.2.min.js" type="text/javascript"></script><script src="../../../code.jquery.com/ui/1.10.3/jquery-ui.js" type="text/javascript"></script><script src="javascripts/bootstrap.min.js" type="text/javascript"></script><script src="javascripts/raphael.min.js" type="text/javascript"></script><script src="javascripts/selectivizr-min.js" type="text/javascript"></script><script src="javascripts/jquery.mousewheel.js" type="text/javascript"></script><script src="javascripts/jquery.vmap.min.js" type="text/javascript"></script><script src="javascripts/jquery.vmap.sampledata.js" type="text/javascript"></script><script src="javascripts/jquery.vmap.world.js" type="text/javascript"></script><script src="javascripts/jquery.bootstrap.wizard.js" type="text/javascript"></script><script src="javascripts/fullcalendar.min.js" type="text/javascript"></script><script src="javascripts/gcal.js" type="text/javascript"></script><script src="javascripts/jquery.dataTables.min.js" type="text/javascript"></script><script src="javascripts/datatable-editable.js" type="text/javascript"></script><script src="javascripts/jquery.easy-pie-chart.js" type="text/javascript"></script><script src="javascripts/excanvas.min.js" type="text/javascript"></script><script src="javascripts/jquery.isotope.min.js" type="text/javascript"></script><script src="javascripts/isotope_extras.js" type="text/javascript"></script><script src="javascripts/modernizr.custom.js" type="text/javascript"></script><script src="javascripts/jquery.fancybox.pack.js" type="text/javascript"></script><script src="javascripts/select2.js" type="text/javascript"></script><script src="javascripts/styleswitcher.js" type="text/javascript"></script><script src="javascripts/wysiwyg.js" type="text/javascript"></script><script src="javascripts/summernote.min.js" type="text/javascript"></script><script src="javascripts/jquery.inputmask.min.js" type="text/javascript"></script><script src="javascripts/jquery.validate.js" type="text/javascript"></script><script src="javascripts/bootstrap-fileupload.js" type="text/javascript"></script><script src="javascripts/bootstrap-datepicker.js" type="text/javascript"></script><script src="javascripts/bootstrap-timepicker.js" type="text/javascript"></script><script src="javascripts/bootstrap-colorpicker.js" type="text/javascript"></script><script src="javascripts/bootstrap-switch.min.js" type="text/javascript"></script><script src="javascripts/typeahead.js" type="text/javascript"></script><script src="javascripts/daterange-picker.js" type="text/javascript"></script><script src="javascripts/date.js" type="text/javascript"></script><script src="javascripts/morris.min.js" type="text/javascript"></script><script src="javascripts/skycons.js" type="text/javascript"></script><script src="javascripts/fitvids.js" type="text/javascript"></script><script src="javascripts/jquery.sparkline.min.js" type="text/javascript"></script><script src="javascripts/main.js" type="text/javascript"></script><script src="javascripts/respond.js" type="text/javascript"></script>
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
                  <!--<div class="icon globe"></div>-->
                  <?php echo $avg_temp; ?> <small>&deg;</small>
                </div>
                <div class="text">
                  Average temperature
                </div>
              </div>
              <div class="col-md-3">
                <div class="number">
                  <!--<div class="icon visitors"></div>-->
                  <?php echo $current_temp; ?> <small>&deg;</small>
                </div>
                <div class="text">
                  Current set temperature
                </div>
              </div>
              <div class="col-md-3">
                <div class="number">
                  <!--<div class="icon chat-bubbles"></div>-->
                  <?php echo $mode?>
                </div>
                <div class="text">
                  Current State
                </div>
              </div>
              <div class="col-md-3">
                <div class="number">
                  <!--<div class="icon money"></div>-->
                  OK 
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
          <div class="col-md-8">
            <div class="row">
              <div class="col-lg-12">
                <div class="widget-container fluid-height clearfix">
                  <div class="heading">
                    <i class="icon-reorder"></i>Settings
                  </div>
                  <div class="widget-content padded">
                    <form method="post" action="form_submit.php" class="form-horizontal" onsubmit="reloadPage()">
                
                      <div class="form-group">
                        <label class="control-label col-md-2">Set temperature</label>
                        <div class="col-md-7">
                          <input name = "set_temp" id = "set_temp" class="form-control" placeholder="" type="text">
                        </div>
                      </div>
                     
                      <div class="form-group">
                        <label class="control-label col-md-2">Mode</label>
                        <div class="col-md-7">

                          <label class="radio-inline"><input name="mode" id="mode" type="radio" value="heating"><span>Heating</span></label>

                          <label class="radio-inline"><input name="mode" id="mode"  type="radio" value="cooling"><span>Cooling</span></label>

                          <label class="radio-inline"><input name="mode" id="mode"  type="radio" value="default"><span>Default</span></label>
                          
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
          <div class="col-md-4">
            
          <!-- System Stats -->
            <div class="widget-container small">
              <div class="heading">
                <i class="icon-signal"></i>System stats<i class="icon-list pull-right"></i><i class="icon-refresh pull-right"></i>
              </div>
              <div class="widget-content padded">
                <div class="bar-chart-widget">
                  <div class="chart-graph">
                    <div id="barcharts">
                      Loading...
                    </div>
                   
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- End System Stats -->
        </div>
        
      </div>
    </div>
  </body>
</html>