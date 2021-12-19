<?php
    namespace app\blog;

    use app\Database;
    
    class PostsProvider {
        private $db;

        public function __construct(Database $db) {
            $this->db = $db;
        }
    }