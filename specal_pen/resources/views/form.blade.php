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
    <form action="/numbers/insert" method="post">
    左辺:<input type ="text" name="num-l"><br>
    演算子:<input type ="text" name="ope"><br>
    右辺:<input type ="text" name="num-r"><br>
    答え:<input type ="text" name="ans"><br>
        <input type="submit" value="送信">
        
    </form>
    </body>

</html>