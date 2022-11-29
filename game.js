    var canvas;
    var canvasContext;
    var ball_X = 50;
    var ball_Y = 50;
    var ballSpeed_X = 15;
    var ballSpeed_Y = 8;
    var paddle1_Y = 250;
    var PADDLE1_THICKNESS = 10;
    const PADDLE1_HEIGHT = 100;
    var paddle2_Y = 250;
    var PADDLE2_THICKNESS = 10;
    const PADDLE2_HEIGHT = 100;
    var player1_score = 0;
    var player2_score = 0;
    const WINNING_SCORE = 3;
    var showingWinScreen = false;

    function calculateMousePos(evt) {
      var rect = canvas.getBoundingClientRect();
      var root = document.documentElement;
      var mouseX = evt.clientX - rect.left - root.scrollLeft;
      var mouseY = evt.clientY - rect.top - root.scrollTop;
      return {
        x: mouseX,
        y: mouseY,
      };
    }

    function handleMouseCLick(evt) {
      if (showingWinScreen) {
        player1_score = 0;
        player2_score = 0;
        showingWinScreen = false;
      }
    }

    window.onload = function () {
      console.log("hello world");
      canvas = document.getElementById("gameCanvas");
      canvasContext = canvas.getContext("2d");
      canvasContext.font = "20px, Arial";
      var framesPerSecond = 30;
      setInterval(function () {
        moveEverything();
        drawEverything();
      }, 1000 / framesPerSecond);

      canvas.addEventListener("mousedown", handleMouseCLick);

      canvas.addEventListener("mousemove", function (evt) {
        var mousePos = calculateMousePos(evt);
        paddle1_Y = mousePos.y - PADDLE1_HEIGHT / 2;
      });
    };

    function ballReset() {
      if (player1_score >= WINNING_SCORE || player2_score >= WINNING_SCORE) {
        showingWinScreen = true;
      }
      ballSpeed_X = -(ballSpeed_X);
      ball_X = canvas.width / 2;
      ball_Y = canvas.height / 2;
    }


    function computerMovement() {
      var paddle2_Y_center = paddle2_Y + PADDLE2_HEIGHT / 2;
      if (paddle2_Y_center < ball_Y - 35) {
        paddle2_Y += 9;
      } else if (paddle2_Y_center > ball_Y + 35) {
        paddle2_Y -= 9;
      }
    }

    function moveEverything() {
      if (showingWinScreen) {
        return;
      }
      computerMovement();

      ball_X += ballSpeed_X;
      ball_Y += ballSpeed_Y;
      if (ball_X >= canvas.width) {
        if (ball_Y > paddle2_Y && ball_Y < paddle2_Y + PADDLE2_HEIGHT) {
          ballSpeed_X = -ballSpeed_X;
        } else {
          player1_score++; //must be before ballReset()
          ballReset();
        }
      }

      if (ball_X < 0) {
        if (ball_Y > paddle1_Y && ball_Y < paddle1_Y + PADDLE1_HEIGHT) {
          ballSpeed_X = -ballSpeed_X;
          var deltaY = ball_Y - (paddle1_Y + PADDLE1_HEIGHT);
          ballSpeed_Y = deltaY * 0.1;
        } else {
          player2_score++; //must be before ballReset()
          ballReset();
        }
      }
      if (ball_Y >= canvas.height) {
        ballSpeed_Y = -ballSpeed_Y;
        var deltaY = ball_Y - (paddle2_Y + PADDLE2_HEIGHT);
        ballSpeed_Y = deltaY * 0.1;
      }
      if (ball_Y <= 0) {
        ballSpeed_Y = -ballSpeed_Y;
      }
    }

    function colorRect(leftX, topY, width, height, drawColor) {
      canvasContext.fillStyle = drawColor;
      canvasContext.fillRect(leftX, topY, width, height);
    }

    function colorCircle(centerX, centerY, radius, drawColor) {
      canvasContext.fillStyle = drawColor;
      canvasContext.beginPath();
      canvasContext.arc(centerX, centerY, radius, 0, Math.PI * 2, true);
      canvasContext.fill();
    }

    function drawNet() {
      for (var i = 0; i < canvas.height; i += 40) {
        colorRect((canvas.width/2) - 1, i, 2, 20, "yellow");
      }
    }

    function drawEverything() {
      // next line: blacks out the screen according to the given dimensions
      colorRect(0, 0, canvas.width, canvas.height, "black");

      if (showingWinScreen) {
        if (player1_score >= WINNING_SCORE) {
          canvasContext.fillStyle = "white";
          canvasContext.fillText(
            "Left player won. Congratulations!",
            400,
            canvas.height / 2
          );
        } else if (player2_score >= WINNING_SCORE) {
          canvasContext.fillStyle = "white";
          canvasContext.fillText(
            "Right player won. Congratulations!",
            400,
            canvas.height / 2
          );
        }

        canvasContext.fillStyle = "white";
        canvasContext.fillText("click to continue", 350, 500);
        return;
      }

     drawNet();

      function player_score(text, x_pos, y_pos, color, max_width){
        canvasContext.fillStyle = color;
        canvasContext.fillText(text, x_pos, y_pos, max_width)
      }


      // left player paddle
      colorRect(0, paddle1_Y, PADDLE1_THICKNESS, PADDLE1_HEIGHT, "white");

      // right computer player paddle
      colorRect(
        canvas.width - 10,
        paddle2_Y,
        PADDLE2_THICKNESS,
        PADDLE2_HEIGHT,
        "white"
      );

      // draws the ball
      colorCircle(ball_X, ball_Y, 9, "green");
      player_score(player1_score, 100, 100, 'white', 30)
      player_score(player2_score, canvas.width-100, 100, 'white', 30)
    }