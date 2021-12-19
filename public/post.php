<?php
    require_once(__DIR__ . '/../src/init.php');

    use app\Template;
    use app\blog\Post;

    $post = null;
    if(isset($_GET['id'])) {
        $post = new Post($db, filter_var($_GET['id'], FILTER_VALIDATE_INT));
        if(!$post->exists()) {
            $post = null;
        }
    }
?>

<?= Template::load('header', ['selected' => 'blog', 'title' => 'Post', 'description' => '', 'keywords' => '']);?>

    <section class="container">
        <?php if($post):?>
            <?= $post->getTitle();?>
        <?php else:?>
            Post nicht gefunden
        <?php endif;?>
    </section>

<?= Template::load('footer');?>