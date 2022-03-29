<?php 

class SQL{
    function __construct($arr){ 
        $this->data = $arr;
        $this->nameSever = $arr['SERVERNAME'];
        $this->userName = $arr['USERNAME'];
        $this->password = $arr['SQLPASSWORD'];
        $this->userTable = $arr['USERTABLE'];
        #var_dump($this->data);
    }
    
    function checkConnectToSQL(){
        
        $conn = new mysqli($this->nameSever, $this->userName, $this->password);
        if ($conn->connect_error) {
            return false;
        }else{
            $conn->close();
            return true;
        } 
    }
    function createDatabase($database){
        error_log("create database");
        $conn = new mysqli($this->nameSever, $this->userName, $this->password);
        $reqSQL = "CREATE DATABASE {$database}";
        if ($conn->query($reqSQL) === TRUE) {
            return true;
        } else {
            error_log("create database fail with error: ".$conn->error);
            return false;
        }
    }
    function createUserTable($database){
        $conn = new mysqli($this->nameSever, $this->userName, $this->password, $database);
        $reqSQL = "CREATE TABLE {$this->userTable} (
            id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
            user VARCHAR(225) NOT NULL ,
            password VARCHAR(255) NOT NULL,
            fullname VARCHAR(255) NOT NULL
        )";
        if ($conn->query($reqSQL) === TRUE) {
            return true;
        } else {
            error_log("create table fail with error: ".$conn->error);
            return false;
        }
    }
    function register($username= '',$password= '') {
        $log = [];
        if ($username =='' || $password == '') {
            $log['status'] = 'false';
            $log['error'] = "don't exist username or password";
            return $log;
        }
        $conn = new mysqli($this->nameSever, $this->userName, $this->password, $this->data['DATABASENAME']);
        $reqSQL = "SELECT user FROM {$this->data['USERTABLE']} WHERE user='$username'";
        $res = $conn->query($reqSQL); 
        $num = $res->num_rows;
        if ($num>0){
            $log['status'] = 'false';
            $log['error'] = "exist username";
            return $log;
        }
        $ran = rand(100000,9999999);
        $passwordhash= password_hash($password,PASSWORD_DEFAULT);
        $reqSQL= "
        INSERT INTO `USER` (
            `id`,
            `user`, 
            `password`
        ) VALUES (
            '$ran', 
            '$username', 
            '$passwordhash'
        )
        ";
        $res = $conn->query($reqSQL);
        $log ['status'] = $res;
        $log ['error'] = Null;
        return $log;

    }

    function login($username= '', $password= ''){
        $log = [];
        if ($username =='' || $password == '') {
            $log['status'] = 'false';
            $log['error'] = "don't exist username or password";
            return $log;
        }
        $conn = new mysqli($this->nameSever, $this->userName, $this->password, $this->data['DATABASENAME']);
        $reqSQL = "SELECT * FROM {$this->data['USERTABLE']} WHERE user='$username'";
        $res = $conn->query($reqSQL);
        if ($res->num_rows > 0){
            $row = $res->fetch_assoc();
            $passwordhash = $row['password'];
            $check = password_verify($password,$passwordhash);
            $log['status'] = $check;
            if ($check === True) {
                $log['token'] = $row['id'];
            }else{ 
                $log['error'] = "password incorrect";
            }
            return $log;
        } else{
            $log['status'] = 'false';
            $log['error'] = "not exist account";
            return $log;
        }
    }

}