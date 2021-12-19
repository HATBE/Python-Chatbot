<?php
    namespace app\user;

    class User {
        public static function isLoggedIn() {
            return isset($_SESSION['loggedIn']);
        }

        public function __construct() {
            
        }
    }