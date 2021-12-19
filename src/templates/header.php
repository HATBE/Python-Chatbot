<!DOCTYPE html>
<html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="robots" content="index,follow" /> 

        <meta property="og:locale" content="de_CH">
        <meta property="og:title" content="<?=PAGE_TITLE;?> - <?=$title;?>">
        <meta property="og:site_name" content="<?=PAGE_TITLE;?>">
        <meta property="og:type" content="website">
        <meta property="og:description" content="<?= $description;?>">
        <meta property="og:url" content="https://bitsflipped.ch">
        <meta property="og:image" content="/assets/img/favicon.png">

        <meta name="description" content="<?=$description;?>">
        <meta name="keywords" content="<?=$keywords;?>">
        <meta name="author" content="Aaron Gensetter">

        <link rel="stylesheet" href="/assets/css/style.css">
        <link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'>
        <link href="/assets/css/bootstrap/bootstrap.css" rel="stylesheet">

        <script src="/assets/js/bootstrap/bootstrap.js"></script>
        <script src="/assets/js/jquery.js"></script>

        <link rel="icon" href="/assets/img/favicon.png" type="image/x-icon">
        <link rel="apple-touch-icon" href="/assets/img/favicon.png">

        <title><?=PAGE_TITLE;?> - <?=$title;?></title>
    </head>
    <body>
        <header class="bg-dark text-light">
            <h1 class="d-none"><?= $title?></h1><!-- SEO -->
            <div class="container">
                <div class="text-center p-3">
                    <h2>
                        <a href="<?=ROOT_PATH;?>" class="link-light text-decoration-none">
                            <?=PAGE_TITLE;?>
                        </a>
                    </h2>
                    <h6 class="text-muted">
                        <?= PAGE_SLOGAN;?>
                    </h6>
                </div>
                <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                    <div class="container-fluid">
                        <button class="navbar-toggler border-0" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarSupportedContent">
                            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                                <li class="nav-item">
                                    <a class="nav-link <?= $selected == 'index' ? 'text-primary' : ''?>" aria-current="page" href="/">Home</a>
                                </li>
                                <li class="nav-item">
                                    <a class="nav-link <?= $selected == 'blog' ? 'text-primary' : ''?>" aria-current="page" href="/list">Blog</a>
                                </li>
                            </ul>
                        </div>
                    </div>    
                </nav>
            </div>
        </header>
        <main>
        