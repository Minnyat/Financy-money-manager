<?php
include 'funcServer.php';
$conn = connectSql();
$data = (new env())->get();
$sql = "CREATE DATABASE {$data['DATABASENAME']}";
requestSql($sql);
?>