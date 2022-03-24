<?php

class env{
    function get(){
        require_once 'vendor/autoload.php';
        $dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
        $dotenv->load(__DIR__.'/.ENV');
        if ($_ENV['APPNAME'] != ''){
            error_log ( 'GET DATA ENV COMPLETE FOR APP ' . $_ENV['APPNAME']);
        } else{
            error_log ('CAN NOT GET DATA');
            return false;
        }
        $tmp = $_ENV;
        $tmp['DATABASENAME'] = $tmp['DEFAULTUSER'].'_'.$tmp['APPNAME'];
        return $tmp;
    } 
}

function connectSql(){
    $ENV = new env();
    $data = $ENV->get();
    $servername = $data['SERVERNAME'];
    $username = $data['USERNAME'];
    $password = $data['SQLPASSWORD'];

    // Create connection
    $conn = new mysqli($servername, $username, $password);

    // Check connection
    if ($conn->connect_error) {
        error_log($conn->connect_error);
        return false;
        die("Connection failed: " . $conn->connect_error);
    }else{ 
        error_log("Connected successfully");
        return $conn;
    } 
}

function requestSql($sql){
    $ENV = new env();
    $data = $ENV->get();
    $servername = $data['SERVERNAME'];
    $username = $data['USERNAME'];
    $password = $data['SQLPASSWORD'];
    // Create connection
    $conn = new mysqli($servername, $username, $password);

    if ($conn->query($sql) === TRUE) {
        echo "Database created successfully";
      } else {
        echo "Error creating database: ".$conn->error;
      }
    $conn->close();
}
?>