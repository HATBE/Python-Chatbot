<?php
    namespace app\blog;

    use app\Model;
    use app\Database;

    class Post extends Model {
        private $data;

        public function __construct(Database $db, $input) {
            $this->db = $db;

            if(is_object($input)) {
                $this->data = $input;
                $this->exists = true;
            } else {
                $id = filter_var($input, FILTER_VALIDATE_INT);

                $this->db->query('SELECT id, title FROM posts WHERE id LIKE :id;');
                $this->db->bind(':id', $id);
                $this->data = $this->db->single();
                $this->exists = $this->db->rowCount() > 0;
            }
        }

        public function getId() {
            return $this->data->id;
        }

        public function getTitle() {
            return $this->data->title;
        }
    }