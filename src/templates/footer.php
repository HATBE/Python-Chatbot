        </main>
        <footer class="bg-dark text-white text-center text-lg-start">
            <div class="container p-4">
                <!--Grid row-->
                <div class="row">
                    <div class="col-lg-6 col-md-12 mb-4 mb-md-0">
                        <h5 class="text-uppercase"><?= ucfirst(strtolower(PAGE_TITLE))?></h5>
                        <p>
                            <?= ucfirst(strtolower(PAGE_TITLE))?>
                        </p>
                    </div>
                    <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
                        <h5 class="text-uppercase"></h5>

                        <ul class="list-unstyled mb-0">

                        </ul>
                    </div>
                    <div class="col-lg-3 col-md-6 mb-4 mb-md-0">
                        <h5 class="text-uppercase mb-0">Links</h5>
                        <ul class="list-unstyled">
                            <li>
                                <a href="/imprint" class="underline text-white">Impressum</a>
                            </li>
                            <li>
                                <a href="/imprint" class="underline text-white">Datenschutz</a>
                            </li>
                            <li>
                                <a href="/copyright" class="underline text-white">Copyright</a>
                            </li>
                            <li>
                            <?php if(app\user\User::isLoggedIn()):?>
                                <a href="/logout" class="underline text-white">Logout</a>
                                <?php else:?>
                                <a href="/login" class="underline text-white">Login</a>
                            <?php endif;?>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="text-center bg-o-dark p-3">
                © <?= '2019 - ' . date('Y')?> Copyright:
                <a class="text-white" href="https://aarongensetter.ch/">Aaron Gensetter</a>
            </div>
        </footer>
    </body>
</html>