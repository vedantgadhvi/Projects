<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname="userlogin";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
//echo "Connected successfully by".$username;


//$last_name = $_POST['pass'];

//$first_name = $_POST['uname'];


//echo $last_name."".$first_name;

$sql = "INSERT INTO fanpage (fanviews) VALUES ('".$_POST['fanviews']."')";
if ($conn->query($sql) === TRUE) {
    header('location:fanpage.html'); 
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();


?>