<?php
    require_once(__DIR__ . '/../src/init.php');

    use app\Template;
?>

<?= Template::load('header', ['selected' => 'index', 'title' => 'Home', 'description' => '', 'keywords' => '']);?>

<?= Template::load('footer');?>