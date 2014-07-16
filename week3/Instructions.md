<h2 class="course-page-header">
    Yahtzee    <a class="coursera-reporter-link" title="Click here if you're experiencing technical problems or found errors in the course materials." target="_blank" href="https://class.coursera.org/principlescomputing-001/help/pages?url=https%3A%2F%2Fclass.coursera.org%2Fprinciplescomputing-001%2Fwiki%2Fview%3Fpage%3Dyahtzee">
      Help
    </a>
    <a data-coursera-admin-helpwidget-link rel="help" href="https://class.coursera.org/mooc/help/pages/setup" title="Course Page Setup" style="display:none;">Learn more.</a>
</h2>


<p></p>
<h4>Overview</h4>
<p>
<a href="http://en.wikipedia.org/wiki/Yahtzee">Yahtzee</a> is a dice game played with 5 dice where you try to score the most points by matching certain combinations.  You can play the game <a href="http://www.yahtzee-game.com/">here</a>.  In Yahtzee, you get to roll the dice three times on each turn.  After the first roll, you may hold as many dice as you would like and roll the remaining free dice.  After this second roll, you may again hold as many dice as you would like and roll the rest. Once you stop (either because you have exhausted your three rolls or you are satisfied with the dice you have), you score the dice in one box on the score card.
</p>
<p></p>
<p>
For this mini-project, we will implement a strategy function designed to help you choose which dice to hold after your <b>second</b> roll. This function will consider all possible choices of dice to hold and recommend the choice that maximizes the expected value of your score after the final roll.  
</p>
<p></p>
<p>
To simplify the mini-project, we will only consider scores corresponding to the "upper" section of the scorecard.  Boxes in the upper section correspond to numbers on the dice.  After each turn, you may choose one empty box and enter the sum of the dice you have with the corresponding number.  For example, if you rolled $$(2, 3, 3, 3, 4)$$, you could score $$2$$ in the Twos box, $$9$$ in the Threes box, or $$4$$ in the Fours box.  (Restricting scoring to the upper section will also allow you to debug/test your strategy function on smaller numbers of dice.)
</p>
 

<h4>Testing your mini-project</h4>
The provided <a href="http://www.codeskulptor.org/#poc_yahtzee_template.py">template</a> includes the function <code>gen_all_sequences</code> from lecture (which you should not modify) as well as a <code>run_example</code> function that you may modify as you see fit while developing, debugging, and testing your strategy function.  The template includes the stubs for the four functions that you will need to implement for this mini-project. Remember you should be testing each function as you write it.  Don't try to implement all of the functions.  If you do,  you will have errors that will interact in inexplicable ways making your program hard to debug.
<p>
</p>
<ul>
<li>
As you implement your strategy function, we suggest that you build your own collection of tests using the <a href="http://www.codeskulptor.org/#poc_simpletest.py" target=""><code>poc_simpletest</code> module</a> that we have provided.  Please review this <a href="view?page=testing_methodogy">page</a> for an overview of the capabilities of this module.  These tests can be organized into a separate test suite that you can import and run in your program as we demonstrated for <a href="mancala">Solitaire Mancala</a>.
<p></p>
</li>
<li>
If you try to test your code with five dice, it will be more difficult to understand what is going on.  Instead, we recommend that you should test first with two dice.   In particular, you may want to work out some examples by hand with two dice and create a small test suite that checks these examples.  If you are having trouble with the case of two dice, you should take a look at this week's <a href="dice_game">practice activity</a>. 
<p></p>
</li>
<li>
Finally, submit your code (with the calls to <code>run_example</code> commented out) to this <a href="http://codeskulptor.appspot.com/owltest?urlTests=poc.week3_tests.py&amp;urlPylintConfig=poc.pylint_config2.py" target="_blank">Owltest</a> page.  This page will automatically test your mini-project.  It will run faster if you comment out the call to <code>run_example</code> before submitting.  Note that trying to debug your mini-project using the tests in OwlTest can be very tedious since they are slow and give limited feedback.  Instead, we <i>strongly</i> suggest that you first test your program using your own test suite.  Programs that pass these tests are much more likely to pass the OwlTest tests.
</li>
</ul>
<p>
Remember that OwlTest uses Pylint to check that you have followed the <a href="view?page=style_guidelines">coding style guidelines</a> for this class. Deviations from these style guidelines will result in deductions from your final score.  Please read the feedback from Pylint closely.  If you have questions, feel free to consult <a href="view?page=pylint_errors">this page</a> and the class forums. </p>
<p>
When you are ready to submit your code to be graded formally, submit your code to the CourseraTest page for this mini-project that is linked on the main assignment page.
</p>
<h4>Implementation</h4>
<p>
</p>
<p>
Your task is to implement the following four functions: <code>score</code>, <code>expected_value</code>, <code>gen_all_holds</code>,  and  <code>strategy</code>.  These four functions should do the following:
</p>
<ul>
<li> 
<code>score(hand):</code>  This function takes a <code>hand</code> (which is a tuple of die values) and computes a score for the hand as the maximum of the possible values for each choice of box in the upper section of the Yahtzee scorecard. </li>
<p>
</p>
<li>
<code>expected_value(held_dice, num_die_sides, num_free_dice):</code> 
This function computes the expected value of the scores for the possible Yahtzee hands that result from holding some dice and rolling the remaining free dice. The dice being held are specified by the tuple <code>held_dice</code>.  The number of sides and the number of dice that are free to be rolled are specified by <code>num_die_sides</code> and <code>num_free_dice</code>, respectively.  You should use <code>gen_all_sequences</code> to compute all possible rolls for the dice being rolled. As an example, in a standard Yahtzee game using five dice, the length of <code>held_dice</code> plus <code>num_free_dice</code> should always be five.
</li>
<p>
</p>
<li>
<code>gen_all_holds(hand):</code>  This function takes a tuple <code>hand</code> and returns the set of all possible tuples formed by discarding a subset of the entries in <code>hand</code>.  The entries in each of these tuples correspond to the dice that will be held.  If the tuple <code>hand</code> has the entries $$(h_0, h_1, ..., h_{m-1})$$, the returned tuples should have the form $$(h_{i_0}, h_{i_1}, ..., h_{i_{k-1}})$$ where $$0\leq k \leq m$$ and the integer indices satisfy $$0\leq i_0 &lt; i_1 &lt;  ...  &lt; i_{k-1} &lt; m$$.  In the case where values in the tuple <code>hand</code> happen to be distinct, the set of tuples returned by <code>gen_all_holds</code> will correspond to all possible subsets of <code>hand</code>.</li>
<p>
</p>
<li>
<code>strategy(hand, num_die_sides):</code>  Thus function takes a <code>hand</code> and computes which dice to hold to maximize the expected value of the score of the possible hands that result from rolling the remaining free dice (with the specified number of sides).  The function should return a tuple consisting of this maximal expected value and the choice of dice that should be held to achieve this value.  If there are several holds that generate the maximal expected value, you may return any of these holds.
</li>
</ul>
As you implement these four functions, make sure that you think about the best order to write and test them in.  You may add extra helper functions if so desired. However, the signature of the four functions above must match the provided description as they will be tested by the machine grader.
<h4> Coding <code>gen_all_holds</code>
</h4>
  Implementing <code>gen_all_holds</code> is one of the main challenges of this mini-project.  While its implementation is short, the actual code requires thought.  Since tuples are immutable, your algorithm for computing the required set of tuples cannot directly delete from the tuple <code>hand</code>.  Instead, <code>gen_all_holds</code> should compute the set of all possible holds in a manner very similar to that of <code>gen_all_sequences</code>.  In particular, your implementation should iterate over the entries of <code>hand</code> and compute all possible holds for the first $$k$$ entries in <code>hand</code> using all possible holds for the first $$k-1$$ entries of <code>hand</code>. 
<p></p>
<p>
To help you test your implementation of <code>gen_all_holds</code>, you may make use of this short test suite:
</p>
<pre><code>#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
</code></pre>
<p></p>
<p>
Once you have working code, you may wish to extend the <code>score</code> function to include scores from the lower section of the Yahtzee scorecard.  (This is optional and isn't graded.)  With this extension, the <code>strategy</code> function gives quite accurate recommendations.  Impress your friends by consistently  beating them at Yahtzee!</p>
<hr>
<div>
