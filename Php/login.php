<?php
    ob_start();
    session_start();

    $username = $_POST['username'];
    $password = $_POST['password'];

    // Required field names
    $required = array('username', 'password');

    // Loop over field names, make sure each one exists and is not empty
    $error = false;
    foreach($required as $field) {
    if (empty($_POST[$field])) {
    $error = true;
    }
    }

    if ($error) {
    header('Location: login.html');
    
    } else {
    
    	$conn = mysql_connect('localhost', 'root', ‘password’);
    	mysql_select_db('login', $conn);
     
    	$username = mysql_real_escape_string($username);
    	$query = "SELECT id, username, password, salt
    	FROM member
    	WHERE username = '$username';";
     
    	$result = mysql_query($query);
     
	// User not found. So, redirect to login_form again.
    	if(mysql_num_rows($result) == 0) 
    		{
    		header('Location: index.html');
    		}
     
    	$userData = mysql_fetch_array($result, MYSQL_ASSOC);
    	$hash = hash('sha256', $userData['salt'] . hash('sha256', $password) );
     
	// Incorrect password. So, redirect to login_form again.
    	if($hash != $userData['password']) 
    		{
    		header('Location: login.html');
		// Redirect to home page after successful login.    	
		}else{ 
    			session_regenerate_id();
    			$_SESSION['sess_user_id'] = $userData['id'];
    			$_SESSION['sess_username'] = $userData['username'];
    			session_write_close();
    			header('Location: home.php');
    		}

    }

  
?>
