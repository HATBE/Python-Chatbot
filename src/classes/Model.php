<?php
    namespace app;

    abstract class Model {
        protected $db;
        protected $exists = false;

        public function exists() {
            return $this->exists;
        }
    }