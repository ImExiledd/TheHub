<?php 
    @session_start();
    // Check to see if the user is banned via DB first.
    require $_SERVER['DOCUMENT_ROOT'] . "/_/sql.php";
    $ouruuid = $_SESSION['guid'];
    
    $checkBannedQuery = "SELECT * FROM users WHERE id = ".$ouruuid.";";
    if($result = mysqli_query($con, $checkBannedQuery)) {
        while($row = mysqli_fetch_row($result)) {
            // Code here
            if($row[8] == 1) {
                session_destroy();
                Header("Location: /accounts/login.php?err=banned");
            }
        }
    }

    function createCard($title, $size, $link, $image, $platform, $mp) {
        echo '
        <div class="searchableCard card-sm" id="1">
        <div class="card-img">
            <img src="'.$image.'">
        </div>
        <div id="1-inner" class="card-content">
            <span class="game-title"><img style="position: relative; bottom: -1px;" src="/img/'.$platform.'logo.png" alt=" "> '.$title.' ('. $mp .')</span>
            <div class="card-content-right">
                <a href="'.$link.'"><span class="material-icons">download</span></a>
            </div>
            <div class="card-content-left">'.$size.'</div>
        </div>
    </div>
        ';
    }
    if(isset($_SESSION['userid'])) {
        // yes session
        if(!$_SESSION['RulesAccepted']) {
            // Havent accepted rules. Redirect.
            Header("Location: /accounts/rules.php");
        }
    
    } else if(!$_SESSION['userid']) {
        // no session
        header("Location: /accounts/login.php");
    }
    if(isset($_SESSION['userid'])) {
        // User is logged in, now check perms.
        if($_SESSION['is_hub_authed'] == 1) {
            // if the user has permissions to access games, go to games.php.
        } else if($_SESSION['is_hub_authed'] == 0) {
            // if the user doesn't have games permissions, check for ayako permissions.
            if($_SESSION['AyakoEnabled'] == 1) {
                // user has ayako permissions but not hub permissions, redirect to ayako.
                Header("Location: ayako.php");
            } else {
                // if no access, 403
                Header("Location: 403.html");
            }
        }
    } else {
        Header("Location: /accounts/login.php");
    }
?>
<!DOCTYPE HTML>
<html>
    <head>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
        <link href="/assets/css/main.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/jquery-modal/0.9.1/jquery.modal.min.css" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>The Hub - <?php echo $page_title ?></title>
        <style>
            .dropdown-content {
                display: none;
                position: absolute;
                top: 3.5em;
                background: #856aff;
                left: 4.2em;
                min-width: 154px;
                z-index: 9999;
                padding: 8px;
                text-align: center;
                border-radius: 5px;
            }
            .dropdown-content > a:hover {
                color: black !important;
            }
            .showDrop {
                display: block;
            }
        </style>
        <script>
            $(document).ready(function() {
                $('.profile_view').hover(function() {
                    $('#profileDropdown').slideToggle();
                })
            })
        </script>
    </head>
    <body>
    <div class="input-group">
        <input id="searchbar" type="text" class="form-control bg-light border-0 small" placeholder="Search for..." aria-label="Search" aria-describedby="basic-addon2">
            <div class="input-group-append"></div>
    </div>
    <!-- Potential feature - Pop-out profiles -->
    <div class="side-nav">
        <a href="/"><span class="logo"><img class="small" src="/assets/img/logo.png">The Hub</span></a>
        <div class="content">
            <div>
           <br>
                <div onclick="$('.profile-popout').toggle()" class="profile_view" id="profile_view">
                    <?php 
                    
                    // check for user profile picture in db
                    $sql2 =  "select * from users where id='".$_SESSION['guid']."'";
                    $result2 = mysqli_query($con, $sql2);
                    $row2 = mysqli_fetch_array($result2);
                    $InviteCode = $row2["INVITE_CODES"];
                    echo "<img class='profile_picture' src=".$row2["userProfilePicture"]."><a href='#'>".$_SESSION["userid"]."</a>";
                    ?>
                    <br><div class="profile-popout">
                        <div class="profile-popout-content">
                            <span class="user-description"></span>
                            <br><span style="color: yellow;">Invite Code: <br><?php echo $InviteCode ?></span><br>
                            <span class="user-links"><br>
                            <span style="font-style: italic; color: #7c7c7d;">Invite codes can only be used once!</span>
                            </span><br>
            </div>
        </div>
                    <!-- <img class="profile_picture" src="/assets/img/undraw_profile.svg"><a href="/profile.php"><?php // echo $_SESSION['userid']; ?> <span class="material-icons">chevron_right</span>--></a>
                    <!-- <div id="profileDropdown" class="dropdown-content">
                         <a href=#>Change PFP</a><br> 
                        <span>Invite:</span><span style="color: yellow"><?php echo $InviteCode?></span>
                    </div> -->
                </div>
            </div>
            <a href="/" class="active nav-link"><span class="material-icons">code</span> Games</a><br>
            <!-- <a href="https://forum.imexile.moe" class="nav-link"><span class="material-icons">forum</span> Forums  </a> -->
            <?php 
                        if($_SESSION["AyakoEnabled"] == 1) {
                            echo '<a href="/ayako.php" class="nav-link"><span class="material-icons">ondemand_video</span> Ayako</a><br>';
                        }
                        if($_SESSION["IS_ADMIN"]) {
                            
                            echo '<a href="/admin" class="nav-link"><span class="material-icons">admin_panel_settings</span> Admin</a>';
                        }
            ?>
            <div class="nav-footer">
                <a class="btn-logout" href="javascript:if(confirm('Are you sure you want to sign out?') === true) { window.location = '/_/logout.php'; } else { }"><span class="material-icons">power_settings_new</span> Logout</a>
            </div>
        </div>
    </div>
    <script>
        window.onload = function() {
            var hasRedirected = false;
            if (top.location.pathname === '/mobile.php') {
                /* magic ... */
            } else {
                if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
                    window.location = "/mobile.php";
                } else {
                    // do nothing
                }
            }

            var user_name = $('.profile_view > a').text();
            var shortText = jQuery.trim(user_name).substring(0,6)
                          .trim(this) + "...";
        }
        $('.profile_view > a').text(shortText);
    </script>
    <div class="container">
        <div class="row">
