<?php
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);

    session_start();

    require_once('autoload.php');
    require_once('config.php');

    $db = new app\Database();

    //$loggedInUser = new App\user\User;