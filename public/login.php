<?php
    require_once(__DIR__ . '/../src/init.php');

    use app\Template;
?>

<?= Template::load('header', ['selected' => 'login', 'title' => 'Login', 'description' => '', 'keywords' => '']);?>

    <section class="d-flex justify-content-center align-items-center">
        <div class="container">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col col-xl-10">
                    <div class="card bg-transparent border-0">
                        <div class="row g-0">
                            <div class="col-md-6 col-lg-5 d-none d-md-block">
                                <img src="/assets/img/server.jpg" alt="login form" class="h-100 img-fluid object-fit-cover">
                            </div>
                            <div class="col-md-6 col-lg-7 d-flex align-items-center">
                                <div class="card-body p-4 p-lg-5 text-white">
                                    <form method="POST">
                                        <div class="d-flex align-items-center mb-3 pb-1">
                                            <span class="h1 fw-bold mb-0 text-primary">Login</span>
                                        </div>
                                        <div>
                                            <?php if(!empty($msgs)):?>
                                                <div class="alert alert-info" role="alert">
                                                    <?php foreach($msgs as $msg):?>
                                                        <?= $msg?>
                                                    <?php endforeach?>
                                                </div>
                                            <?php endif?>   
                                        </div>
                                        <h5 class="fw-normal mb-3 pb-3" style="letter-spacing: 1px;">Sign into your account</h5>
                                        <div class="form-outline mb-4">
                                            <label class="form-label" for="username">Username</label>
                                            <input name="input-username" type="text" class="form-control form-control-lg" value="<?= isset($_POST['input-username']) ? $_POST['input-username'] : ''?>"/>
                                        </div>
                                        <div class="form-outline mb-4">
                                            <label class="form-label" for="password">Password</label>
                                            <input name="input-password" type="password" class="form-control form-control-lg" />
                                        </div>
                                        <div class="pt-1 mb-4">
                                            <button name="input-submit" class="btn btn-primary btn-lg btn-block" type="submit">Login</button>
                                        </div>
                                        <a class="small text-muted" href="#!">Forgot password?</a>
                                        <!--<p class="mb-5 pb-lg-2" style="color: #393f81;">Don't have an account? <a href="#!" style="color: #393f81;">Register here</a></p>-->
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

<?= Template::load('footer');?>