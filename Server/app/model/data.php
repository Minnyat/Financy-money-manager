<?php
require_once 'sql.php';
class env{
    function __construct(){ 
        $this->data = []; 
        $this->data = $this->get();
    }
    function get(){
        require_once 'vendor/autoload.php';
        $dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
        $dotenv->load(__DIR__.'/.env');
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
?>