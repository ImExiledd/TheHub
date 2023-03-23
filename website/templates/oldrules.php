<?php 
if(session_status() !== PHP_SESSION_ACTIVE) session_start();
if(!$_SESSION['userid']) {
    // No user id!
    Header("Location: /");
}
?>

<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>The Hub - Welcome aboard!</title>

    <!-- Custom fonts for this template-->
    <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
    <link
        href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i"
        rel="stylesheet">

    <!-- Custom styles for this template-->
    <link href="css/sb-admin-2.min.css" rel="stylesheet">

</head>

<body class="bg-gradient-primary">

    <div class="container">

        <!-- Outer Row -->
        <div class="row justify-content-center">

            <div class="col-xl-10 col-lg-12 col-md-9">

                <div class="card o-hidden border-0 shadow-lg my-5">
                    <div class="card-body p-0">
                        <!-- Nested Row within Card Body -->
                        <div class="row">
                            
                            <div class="col-lg-12">
                                <div class="p-5">
                                    <div class="text-center" id="errsect">
                                        <h1 class="h4 text-gray-900 mb-4">Welcome aboard, <?php echo $_SESSION['userid']; ?>!</h1>
                                        <h8>The following are the rules of our community and web pages, including those hosted on other platforms. Failure to follow these rules may result in an account ban. You will be refered to as "the user" on this page.
                                        <br><br>
                                        <h8>&bull; "The User" will not advertise or otherwise make known the presence of The Hub unless offering an "invite code" to another individual.</h8><br>
                                        <h8>&bull; "The User" will not download any file from "The Hub" unless a download link is provided on the page.</h8><br>
                                        <h8>&bull; "The User" will not, under any circumstance, attempt to breach, hack, or otherwise gain unauthorized access to any page or portion of the server running The Hub without expressed, written consent.</h8><br>
                                        <h8>&bull; "The User" agrees that, should they have concerns related to The Hub, they will contact any authorized administrator and understands that authorized administrators have a designated dark red background behind their name</h8><br>
                                        <h8>&bull; "The User" agrees to not harrass, bully, or otherwise cause harm in any way to any other user of the platform.</h8><br>
                                        <h8>&bull; "The User" agrees that in areas where uploads are possble and allowed, they will not post content which depicts any of the following: Minors, Child Pornography. The only exception to this rule are "Hentai" images and videos, consisting exclusively of 2D images or videos.</h8><br>
                                        <!-- test -->
                                        <?php 
                                            if(isset($_GET['err'])) {
                                                if($_GET['err'] == 'usedcode') {
                                                    echo "<br><span style='color:red;'>The invite code you have tried to use has already been redeemed.</span>";
                                                }
                                            }
                                        ?>
                                    </div>
                                    <hr>
                                    <div class="text-center">
                                        <!-- <a class="small" href="register.html">Create an Account!</a> -->
                                        <input type="checkbox" class="btn-check" id="RuleAgreeCheckBox" autocomplete="off">By checking this box, I acknowledge that I have read and agree to abide by all terms listed above, and agree that should any of these rules be violated, there is the possibility of a <span style="color: red;">permanent and unreversable suspension.</span></input><br><br>
                                        <form class="user" method="post" action="_/ruleAccept.php">
                                            <button class="btn btn-primary" type="submit" id="RuleAcceptButton" name="btn_submit" disabled onclick="window.location = '/';">I've read the rules, take me to The Hub!</button>
                                        </form>
                                        <button class="btn btn-red" type="" id="RuleDeclineButton" onclick="window.location = '/_/logout.php';">I do not accept the rules, log me out.</button>
                                        
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>

        </div>

    </div>

    <!-- Bootstrap core JavaScript-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Core plugin JavaScript-->
    <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

    <!-- Custom scripts for all pages-->
    <script src="js/sb-admin-2.min.js"></script>
    <script src="js/main.js"></script>

</body>

</html>
<?php

?>