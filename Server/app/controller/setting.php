<?php

require_once (__DIR__.'/../model/data.php');

class setting{
    
    function __construct(){
        $temp = new env();
        $this->data = $temp->data;
    }
    function run(){ 
        $sql = new SQL($this->data);
        if ($sql->checkConnectToSQL() === false){ 
            die("can't connect to SQL server. check access information </br>");
        } else{
            echo "connect SQL server successful.</br>";
            echo "checking database .....</br>";
        }
        if ($sql->createDatabase($this->data['DATABASENAME']) === false){ 
            echo "Have been exist {$this->data['DATABASENAME']}.</br>";
        }else{ 
            echo "Create database '{$this->data['DATABASENAME']}' complete.</br> ";
        }
        if ($sql->createUserTable($this->data['DATABASENAME'])){
            echo "create user table complete</br>";
        }else{
            echo "can't create user table</br>";
        }
    }
    
}
$action = new setting;
$action->run();
?>