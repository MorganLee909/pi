<!doctype html>

<html>
<head>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>

  <?php
    //TODO: The shell execution needs to be removed from every if statement and
    //added to the end.  Also I want to change this to call a method.
    if(isset($_POST['first'])){
      $pin = 2;
      shell_exec("sudo python relayControl.py " .$pin);
    }
    else if(isset($_POST['second'])){
      $pin = 3;
      shell_exec("sudo python relayControl.py" .$pin);
    }
  ?>

<body>
  <h4><span id="datetime"></span></h4>
  <!-- TODO: Change date/time code to be less ugly and make it dynamic -->
  <script>
    var dt = new Date();
    document.getElementById("datetime").innerHTML = (("0"+dt.getDate()).slice(-2)) +
    "."+ (("0"+(dt.getMonth()+1)).slice(-2)) +"."+ (dt.getFullYear()) +" "+
    (("0"+dt.getHours()).slice(-2)) +":"+ (("0"+dt.getMinutes()).slice(-2)) +":"+
    (("0"+dt.getSeconds()).slice(-2));
  </script>
  <h1>Lee Morgan</h1>
  <div>
    <form method="post">
      <button name="Light">First</button>
      <button name="Fan">Second</button>
  </div>
  <script>
    document.body.style.backgroundColor = "#373738";
  </script>
</body>
</html>
