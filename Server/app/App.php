<?php
class App{
    private $__controller, $__action, $__params;
    function __construct(){ 
        $this->__controller = 'api';
        $this->__action = 'index';
        $this->__params = []; 
        $this->handleUrl();
    }
    function getUrl(){ 
        if(!empty($_SERVER['PATH_INFO'])){
            $url = $_SERVER['PATH_INFO'];
        }else{ 
            $url = '/';
        }
        return $url;
    }
    public function handleUrl(){ 
        $url = strtolower($this->getUrl());
        $url = strtolower($url);
        $urlArr = array_filter(explode('/',$url));
        $urlArr = array_values($urlArr);
        /*
        echo '</pre>';
        print_r($urlArr);
        echo '</pre>';
        */

        if (!empty($urlArr[0])){
            $this->__controller = $urlArr[0];
            if (file_exists(('app/controller/'.($this->__controller).'.php'))){
                require_once 'controller/'.($this->__controller).'.php';
                $this->__controller = new $this->__controller();
                unset($urlArr[0]);
            }else{ 
                echo 'error';
            }
        }
        if (!empty($urlArr[1])){
            $this->__action = $urlArr[1];
            unset($urlArr[1]);
        }
        $this->__params = $urlArr;
        call_user_func_array([$this->__controller, $this->__action],$this->__params);
        

    }
}