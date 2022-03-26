<?php
class API{
    public function index(){
        echo 'note how to use APi';
    }
    public function login($username = 'None',$password = 'None'){
        if (!empty($_GET['username'])){
            $username = $_GET['username'];
        }
        if (!empty($_GET['password'])){
            $password = $_GET['password'];
        }
        echo $username. ' '. $password;
    }
}