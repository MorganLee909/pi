<!doctype html>

<html>
<head>
  <link rel="stylesheet" type="text/css" href="style.css"/>
</head>

  <?php
    $pin = 0;
    if(isset($_POST['first'])){
      $pin = 7;
    }
    else if(isset($_POST['second'])){
      $pin = 8;
    }
	
    shell_exec("sudo python -c 'from relayControl import recieveInput; recieveInput()' " .$pin);
  ?>

<body>
  <h1>Lee Morgan</h1>
  <div>
    <form method="post">
      <button name="first">Light</button>
      <button name="second">Fan</button>
  </div>
</body>
</html>
