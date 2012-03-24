<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>The Latest Scoops!</title>
        <link rel="stylesheet" type="text/css" href="http://d.bldm.us/scoops.css">
        <link href='http://fonts.googleapis.com/css?family=Lora:700,400' rel='stylesheet' type='text/css'>
        <link rel="shortcut icon" href="http://media.musicfortheblind.co.uk/static/favicon.ico" type="image/vnd.microsoft.icon">
    </head>

    <body>

<!--
    <span class="presses">This just in:</span>
-->
    <div class="headline">
    <h2>
        %if first == 'company':
            {{story0}}<span class="company">{{company}}</span>{{story1}}<span class="game">{{game}}</span>{{story2}}
        %else:
            {{story0}}<span class="game">{{game}}</span>{{story1}}<span class="company">{{company}}</span>{{story2}}
        %end
    </h2>
    </div>

    <p class="further">
        For more on these or other stories from the world of video games, check out <a href="https://twitter.com/patrickklepek">PATRICK KLEEEEEEEEEEEEEEEEEEEEPEK</a> (on twitter).
    </p>
    <div class="credit">
        <p><a href="https://bitbucket.org/colons/scoops">Source</a> (Python, Bottle)</p>
        <p>A <a href="http://www.musicfortheblind.co.uk/">Music for the Blind</a> production</p>
    </div>
    </body>
</html>
