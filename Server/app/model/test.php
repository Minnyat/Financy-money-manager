<?php

require_once 'sql.php';
require_once 'data.php';

$temp = new env();
$test = new SQL($temp->data);

$res =  $test->login('admin','admin');
print_r ($res);
?>