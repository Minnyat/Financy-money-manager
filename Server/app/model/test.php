<?php

require_once 'sql.php';
require_once 'data.php';

$temp = new env();
$test = new SQL($temp->data);

var_dump ($test->register('nhat','lam'));
?>