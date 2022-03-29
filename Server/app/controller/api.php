<?php
class API{
    public function index(){
        echo 'note how to use APi';
    }
    public function login($username = '',$password = ''){
        if (!empty($_GET['username'])){
            $username = $_GET['username'];
        }
        if (!empty($_GET['password'])){
            $password = $_GET['password'];
        }
        require_once (__DIR__.'/../model/sql.php');
        require_once (__DIR__.'/../model/data.php');
        
        $temp = new env();
        $login = new SQL($temp->data);
        $res =  $login->login($username, $password);
        echo json_encode ($res);
    }
    public function register($username = '',$password = ''){
        if (!empty($_GET['username'])){
            $username = $_GET['username'];
        }
        if (!empty($_GET['password'])){
            $password = $_GET['password'];
        }
        require_once (__DIR__.'/../model/sql.php');
        require_once (__DIR__.'/../model/data.php');
        
        $temp = new env();
        $register = new SQL($temp->data);
        $res =  $register->register($username, $password);
        echo json_encode ($res);
    }
    
}