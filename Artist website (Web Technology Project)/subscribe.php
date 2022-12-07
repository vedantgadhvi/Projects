<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname="userlogin";


$sql = "INSERT INTO user (name,emailid) VALUES ('".$_POST['uname']."', '".$_POST['pass']."')";
if ($conn->query($sql) === TRUE) {
    echo =Succesful" ; 
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();


?>