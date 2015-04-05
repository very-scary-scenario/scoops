<!DOCTYPE html>
<html>
  <head>
    <title>lower third</title>
    <meta charset='utf-8'/>
    <link href='http://fonts.googleapis.com/css?family=News+Cycle:700' rel='stylesheet' type='text/css'>
    <style>
      @keyframes marquee {
        0% {left: 100vw}
        100% {left: -100%}
      }
      @-webkit-keyframes marquee {
        0% {left: 100vw}
        100% {left: -100%}
      }

      * {
        margin: 0;
        padding: 0;
      }

      body {
        min-width: 100vw;
        font-family: "News Cycle", sans-serif;
        position: absolute;
        display: table;
        white-space: nowrap;
        overflow: hidden;
      }

      h1 {
        margin-top: 1em;
        position: relative;
        left: -100%;

        animation: marquee 20s linear;
        -webkit-animation: marquee 20s linear;
      }
    </style>
  </head>
  <body>
    <h1 id="story"></h1>
    <script>
      var storyElement = document.getElementById('story');

      function getStory() {
        var req = new XMLHttpRequest();
        req.onload = function() {
          showStory(this.response);
        }
        req.open('get', '/raw?html=true', true);
        req.send();
      }

      function showStory(story) {
        document.body.innerHTML = '<h1 id="stort">' + story + '</h1>';
      }

      showStory(getStory());

      setInterval(function() {
        showStory(getStory());
      }, 20 * 1000);
    </script>
  </body>
</html>
