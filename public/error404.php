<?php
    require_once(__DIR__ . '/../src/init.php');

    use app\Template;
?>

<?= Template::load('header', ['selected' => 'error', 'title' => 'Error 404', 'description' => '', 'keywords' => '']);?>

    <section class="container d-flex justify-content-center">
        <div class="p-5 m-5">
            <h1>Error 404 - This page doesn't exist!</h1>
            <h6>Sorry, the page you requested could not be found.</h6>
        </div>
    </section>

<?= Template::load('footer');?>