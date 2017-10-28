<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0, user-scalable=no" />
    <title>すぺちゃるぺん！</title>

    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link href="css/materialize.css" rel="stylesheet" media="screen,projection" />
    <link href="https://fonts.googleapis.com/earlyaccess/nicomoji.css" rel="stylesheet" />
    <link href="css/style.css" rel="stylesheet" />

    <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
    <script src="js/materialize.js"></script>
    <script src="js/script.js"></script>
</head>

<body>
    <nav class="light-blue darken-1 nv">
        <div class="nav-wrapper container">
            <a href="index.jsp" class="brand-logo">すぺちゃるぺん</a>
        </div>
    </nav>
    <div class="parallax-container">
        <div class="parallax">
            <img src="img/back.jpg">
        </div>
    </div>
    <a href="/numbers/delete" class="button">削除</a>
    <table class="striped">
        <?php $kekka = 0;
              $count = 0;
    foreach($numbers as $num){ 
        $count++;?>
        <tr>
            <td>
                <?php echo $count ?>問目</td>
            <td>
                <h3>
                    <?php echo $num->number_l; ?>
                    <?php echo $num->operators; ?>
                    <?php echo $num->number_r; ?>
                </h3>
            </td>
            <td id="ans<?php echo $count; ?>"><h3><?php echo $num->answer; ?></h3>
                <label id="label<?php echo $count; ?>"></label></td>
            <td>
                <?php
                    ?>
                <input type="button" value="答え" id="btn<?php echo $count; ?>">
                <script type="text/javascript">
                    $("#btn<?php echo $count; ?>").click(function() {
                        
                        <?php 
                        $hantei; 
                    if($num->operators === "+"){
                            $kekka = $num->number_l+$num->number_r;
                    }else if($num->operators === "-"){
                        $kekka = $num->number_l-$num->number_r;
                    }else{
                        $kekka = $num->number_l*$num->number_r;
                    }
                    if($kekka == $num->answer){
                        $hantei = "ok";
                    }else{
                        $hantei = "no";
                    }
                    ?>
                    alert('正解は'+<?php echo $kekka; ?>);
                        <?php
                        if($hantei === "ok"){ ?>
                        document.getElementById("ans<?php echo $count; ?>").style.color = "blue";
                        document.getElementById("label<?php echo $count; ?>").textContent ="正解";
                        document.getElementById("label<?php echo $count; ?>").style.color = "blue";
                        <?php }else{?>
                        document.getElementById("ans<?php echo $count; ?>").style.color = "red";
                        document.getElementById("label<?php echo $count; ?>").textContent ="残念！";
                        document.getElementById("lebel<?php echo $count; ?>").style.color = "purple";
                        <?php } ?>
                        
                    });
                </script>
            </td>
        </tr>
        <?php } ?>
    </table>




</body>

</html>