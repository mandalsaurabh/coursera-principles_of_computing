<h2 class="course-page-header">
    Tic-Tac-Toe (Monte Carlo)    <a class="coursera-reporter-link" title="Click here if you're experiencing technical problems or found errors in the course materials." target="_blank" href="https://class.coursera.org/principlescomputing-001/help/pages?url=https%3A%2F%2Fclass.coursera.org%2Fprinciplescomputing-001%2Fwiki%2Fview%3Fpage%3Dtictactoemc">
      Help
    </a>
    <a data-coursera-admin-helpwidget-link rel="help" href="https://class.coursera.org/mooc/help/pages/setup" title="Course Page Setup" style="display:none;">Learn more.</a>
</h2>


<p></p>
<h4>Overview</h4>
<p>
<a href="http://en.wikipedia.org/wiki/Tic-tac-toe">Tic-Tac-Toe</a> is a simple children's game played on a $$3 \times 3$$ grid.  Players alternate turns placing an "X" or an "O" on an empty grid square.  The first player to get three-in-a-row wins. If you know the appropriate strategy and your opponent does not, you cannot lose the game.  Further, if both players understand the appropriate strategy the game will always end in a tie. An interesting variant of the game is "reverse" Tic-Tac-Toe in which you lose if you get three-in-a-row.  The game is also more interesting if you play on larger square grids.
</p>
<p>
For this assignment, your task is to implement a machine player for Tic-Tac-Toe.  Specifically, your machine player will use a Monte Carlo simulation to decide its next move.  We will provide both a console-based interface to the game where your machine player will play against itself and a graphical user interface where you can play against your machine player.  Although the game is played on a $$3 \times 3$$ grid, your version should be able to handle any square grid.  We will continue to use the same <a href="grids">grid conventions</a> that we have used previously.
</p>
<p>
For this mini-project, we will provide you with a complete implementation of a Tic-Tac-Toe Board class.  However, for your part of the mini-project, we will provide only a very minimal amount of  <a href="http://www.codeskulptor.org/#poc_ttt_template.py" target="_blank">starting code</a>. We will also dispense with the phased description of the implementation process so that your coding task for this mini-project is a more realistic example of a typical coding problem.
</p>
<p>
</p>
<h4>Provided Code</h4>
<p>
We have provided a <code>TTTBoard</code> class for you to use.  This class keeps track of the current state of the game board.  You should familiarize yourself with the <a href="TTTBoard">interface</a> to the <code>TTTBoard</code> class in the <code>poc_ttt_provided</code> module.  The provided module also has a <code>switch_player(player)</code> function that returns the other player (<code>PLAYERX</code> or <code>PLAYERO</code>), and a <code>play_game(mc_move_function, ntrials, reverse)</code> function that uses the <code>mc_move_function</code> you provide to play a game with two machine players on a $$3 \times 3$$ board.  The <code>play_game</code> function will print the moves in the game to the console.  Finally, the provided module defines the constants <code>EMPTY</code>, <code>PLAYERX</code>, <code>PLAYERO</code>, and <code>DRAW</code> for you to use in your code.  The provided <code>TTTBoard</code> class and GUI use these same constants, so you will need to use them in your code, as well.
</p>
<p>
At the bottom of the provided template, there are example calls to the GUI and console game player.  You may uncomment and modify these during the development of your machine player to actually use it in the game.  The <code>run_gui</code> function takes five arguments: the dimension of the board, which player the machine player will be, a move function, the number of trials per move, and a reverse argument indicating whether or not you want to play normal (<code>False</code>) or reverse (<code>True</code>) game.
</p>
<h4>Testing your mini-project</h4>
As always, testing is a critical part of the process of building your mini-project.  Remember you should be testing each function as you write it.  Don't try to implement all of the functions and then test.  You will have lots of errors that all interact in strange ways that make your program very hard to debug.
<p>
</p>
<ul>
<li>
As you implement your machine player, we suggest that you build your own collection of tests using the <a href="http://www.codeskulptor.org/#poc_simpletest.py" target=""><code>poc_simpletest</code> module</a> that we have provided.  Please review this <a href="view?page=testing_methodogy">page</a> for an overview of the capabilities of this module.  These tests can be organized into a separate test suite that you can import and run in your program as we demonstrated for <a href="mancala">Solitaire Mancala</a>.  To facilitate testing on the first few mini-projects, we will create a thread in the forums where students may share and refine their test suites for each mini-project.
<p></p>
</li>
<li>
Finally, submit your code (with the calls to <code>play_game</code> and <code>run_gui</code> commented out) to this <a href="http://codeskulptor.appspot.com/owltest?urlTests=poc.week2_tests.py&amp;urlPylintConfig=poc.pylint_config.py&amp;imports=%7Bpoc:(poc_ttt_provided,%20poc_ttt_gui)%7D" target="_blank">Owltest</a> page.  This page will automatically test your mini-project.  It will run faster if you comment out the calls to <code>play_game</code> and <code>run_gui</code> before submitting.  Note that trying to debug your mini-project using the tests in OwlTest can be very tedious since they are slow and give limited feedback.  Instead, we <i>strongly</i> suggest that you first test your program using your own test suite and the provided GUI.  Programs that pass these tests are much more likely to pass the OwlTest tests.
</li>
</ul>
<p>
Remember that OwlTest uses Pylint to check that you have followed the <a href="view?page=style_guidelines">coding style guidelines</a> for this class. Deviations from these style guidelines will result in deductions from your final score.  Please read the feedback from Pylint closely.  If you have questions, feel free to consult <a href="view?page=pylint_errors">this page</a> and the class forums. </p>
<p>
When you are ready to submit your code to be graded formally, submit your code to the CourseraTest page for this mini-project that is linked on the main assignment page.
</p>
<h4>Machine Player Strategy</h4>
<p>
Your machine player should use  a Monte Carlo simulation to choose the next move from a given Tic-Tac-Toe position. The general idea is to play a collection of games with random moves starting from the position, and then use the results of these games to compute a good move.  When you win one of these random games, you want to favor the squares in which you played (in hope of choosing a winning move) and avoid the squares in which your opponent played.  Conversely, when you lose one of these random games, you want to favor the squares in which your opponent played (to block your opponent) and avoid the squares in which you played.  In short, squares in which the winning player played in these random games should be favored over squares in which the losing player played.
</p>
<p>
Here is an outline of this simulation:
</p>
<ol>
<li>Start with the current board.
</li>
<li>Repeat for the desired number of trials:
<ol type="A">
<li>Play an entire game by just randomly choosing a move for each player.
</li>
<li>Score the resulting board.
</li>
<li>Add the scores to a running total across all trials.
</li>
</ol>
</li>
<li>To select a move, randomly choose one of the empty squares on the board that has the maximum score.
</li>
</ol>
<p>
These steps should be relatively straight-forward except for step 2B, scoring the board.  Scores are kept for each square on the board.  The way you assign a score to a square depends on who won the game.  If the game was a tie, then all squares should receive a score of 0, since that game will not help you determine a winning strategy.  If you won the game, each square that matches your player should get a positive score (corresponding <code>MCMATCH</code> in the template) and each square that matches the other player should get a negative score (corresponding to <code>-MCOTHER</code> in the template).  Conversely, if you lost the game, each square that matches your player should get a negative score (<code>-MCMATCH</code>) and and each square that matches the other player should get a positive score (<code>MCOTHER</code>).  All empty squares should get a score of 0.
</p>
<p>
Note that you want to select a final move from the total scores across all trials.  So, in step 2C, you are adding the scores from 2B to the running total of all scores.  Higher scores indicate squares that are more likely to be played in winning games and lower scores indicate squares that are more likely to be played in losing games.
</p>
<h4>Implementation</h4>
<p>
Your task is to implement the following four functions: <code>mc_trial</code>, <code>mc_update_scores</code>, <code>get_best_move</code>, and <code>mc_move</code>.  These four core functions should do the following:
</p>
<ul>
<li> 
<code>mc_trial(board, player):</code>  This function takes a current board and the next player to move.  The function should play a game starting with the given player by making random moves, alternating between players.  The function should return when the game is over.  The modified board will contain the state of the game, so the function does not return anything.  In other words, the function should modify the <code>board</code> input.</li>
<li>
<code>mc_update_scores(scores, board, player): </code> This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, a board from a completed game, and which player the machine player is.  The function should score the completed board and update the scores grid.  As the function updates the scores grid directly, it does not return anything,</li>
<li>
<code>get_best_move(board, scores):</code> This function takes a current board and a grid of scores.  The function should find all of the empty squares with the maximum score and randomly return one of them as a <code>(row, column)</code> tuple.  It is an error to call this function with a board that has no empty squares (there is no possible next move), so your function may do whatever it wants in that case.  The case where the board is full will not be tested.</li>
<li>
<code>mc_move(board, player, trials):</code> This function takes a current board, which player the machine player is, and the number of trials to run.  The function should use the Monte Carlo simulation described above to return a move for the machine player in the form of a <code>(row, column)</code> tuple.  Be sure to use the other functions you have written!</li>
</ul>
You should start from <a href="http://www.codeskulptor.org/#poc_ttt_template.py">this code</a> that imports the Tic-Tac-Toe class and defines several useful constants. You may add extra helper functions if so desired. However, the signature of the four functions above must match the provided description as they will be tested by the machine grader.
<p></p>
<p>
Once you have working code, you will want to experiment with the values of <code>NTRIALS</code>, <code>MCMATCH</code>, and <code>MCOTHER</code> to get a good machine player.  You must use these constant names, as the machine grader will assume they are defined in your file.  Further, the final test will be whether your player selects obvious good next moves.
</p>
<hr>
<div>
