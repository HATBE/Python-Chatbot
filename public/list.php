<?php
    require_once(__DIR__ . '/../src/init.php');

    use app\Template;
    use app\blog\Article;
?>

<?= Template::load('header', ['selected' => 'blog', 'title' => 'List', 'description' => '', 'keywords' => '']);?>



<?= Template::load('footer');?>