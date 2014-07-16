<h2 class="course-page-header">
    Cookie Clicker    <a class="coursera-reporter-link" title="Click here if you're experiencing technical problems or found errors in the course materials." target="_blank" href="https://class.coursera.org/principlescomputing-001/help/pages?url=https%3A%2F%2Fclass.coursera.org%2Fprinciplescomputing-001%2Fwiki%2Fview%3Fpage%3Dclicker">
      Help
    </a>
    <a data-coursera-admin-helpwidget-link rel="help" href="https://class.coursera.org/mooc/help/pages/setup" title="Course Page Setup" style="display:none;">Learn more.</a>
</h2>


<p></p>
<h4>Overview</h4>
<p>
Cookie Clicker is a simple optimization game in which you try to produce as many cookies as possible.  You can play it <a href="http://orteil.dashnet.org/cookieclicker/" target="_blank">here</a>.
</p>
<p>
The object of the game is to produce cookies as fast as possible.  You have many options to produce cookies.  Originally, you can only produce cookies by clicking your mouse.  However, you can use your cookies to buy other methods of producing cookies (Grandmas, farms, factories, etc.).  Each production method increases the number of "cookies per second" (CPS) you produce.  Further, each time you buy one of the production methods, its price goes up.  So, you must carefully consider the cost and benefits of purchasing a production method, and the trade-offs change as the game goes on.
</p>
<p>
For this assignment, you will implement a simple simulation of the Cookie Clicker game.  You will implement different strategies and see how they fare over a given period of time.  In our version of the game, there is no graphical interface and therefore no actual "clicking".  Instead, you will start with a CPS of 1.0 and may start purchasing automatic production methods once you have enough cookies to do so.  You will implement both the simulation engine for the game and your own strategies for selecting what production methods to buy.
</p>
<p>
We have provided the following <a href="http://www.codeskulptor.org/#poc_clicker_template.py" target="_blank">template</a> that contains an outline of the code you will write, including a <code>ClickerState</code> class, which will keep track of the state of the simulation, and a <code>simulate_clicker</code> function, which will run the simulation.  The signature (name and parameters) of the functions, classes, and methods in this file must remain unchanged, but you may add any additional functions, methods, or other code that you need to. 
</p>
<p>
</p>
<h4>Provided Code</h4>
<p>
We have provided a <code>BuildInfo</code> class for you to use.  This class keeps track of the cost (in cookies) and value (in CPS) of each item (production method) that you can buy.  When you create a new <code>BuildInfo</code> object, it is initialized by default with the default parameters for our game.  Keep in mind that if you pass a <code>BuildInfo</code> object around in your program and it is modified anywhere, then you will see the changes everywhere.  If you do not want that, we have provided a <code>clone</code> method that will create an identical copy of the object.  You can see a description of the class and its methods <a href="BuildInfo">here</a>.  It has methods to allow you to find out what all of the items' names are, the cost/CPS of each item, and to update the cost of a particular item appropriately.
</p>  
<p>
We have also provided a <code>run</code> function to run your simulator. Note that the <code>run</code> function simply calls <code>run_strategy</code>, which runs the simulator once with a given strategy.  You can add more calls to <code>run_strategy</code> inside of <code>run</code> once you develop your own strategies.  The <code>run_strategy</code> function runs the simulation, prints out the final state of the game after the given time and then plots the total number of cookies over time.  You can replace our <code>SimplePlot</code> plotting code with your own plotting code if you wish to use IDLE or another Python IDE.  If you do leave our plots in, make sure that your web browser is configured to allow popup windows from CodeSkulptor.  The plots will help you understand how the number of cookies grow over time, which is the point of this week in the class, so we recommend you do look at the plots, even if you comment them out while you are debugging.
</p>
<p>
We have provided a simple strategy, called <code>strategy_cursor</code>.  Note the signature of the function: <code>strategy_cursor(cookies, cps, time_left, build_info)</code>.   All strategy functions take the current number of cookies, the current CPS, the amount of time left in the simulation, and a <code>BuildInfo</code> object (even if they don't use these parameters).  You'll note that this simple strategy just always picks <code>"Cursor"</code> no matter what the state of the game is.  This is obviously not a good strategy, but rather is a placeholder so you can see the signature of a strategy function looks like and use it while you are debugging other parts of your code.
</p>
<h4>Testing your mini-project</h4>
As always, testing is a critical part of the process of building your mini-project.  Remember you should be testing each method as you write it.  Don't try to implement all of the methods and then test.  You will have lots of errors that all interact in strange ways that make your program very hard to debug.
<p>
</p>
<ul>
<li>
As you implement the <code>ClickerState</code> class, we suggest that you build your own collection of tests using the <a href="http://www.codeskulptor.org/#poc_simpletest.py" target=""><code>poc_simpletest</code> module</a> that we have provided.  Please review this <a href="view?page=testing_methodogy">page</a> for an overview of the capabilities of this module.  These tests can be organized into a separate test suite that you can import and run in your program as we demonstrated for <a href="mancala">Solitaire Mancala</a>.  To facilitate testing on the first few mini-projects, we will create a thread in the forums where students may share and refine their test suites for each mini-project.  We also strongly suggest that you write a <code>print_history</code> function that nicely prints the history of the game.  Then, you can run short simulations, print the history, and confirm that things are working as you would expect.
<p></p>
</li>
<li>
Finally, submit your code (with the call to <code>run</code> commented out) to this <a href="http://www.codeskulptor.appspot.com/owltest?urlTests=poc.week1_tests.py&amp;urlPylintConfig=poc.pylint_config2.py&amp;imports=%7Bpoc:(poc_clicker_provided)%7D" target="">Owltest</a> page.  This page will automatically test your mini-project.  It will run faster if you comment out the call to <code>run</code> before submitting.  Note that trying to debug your mini-project using the tests in OwlTest can be very tedious since they are slow and give limited feedback.  Instead, we <i>strongly</i> suggest that you first test your program using your own test suite.  Programs that pass these tests are much more likely to pass the OwlTest tests.
</li>
</ul>
<p>
Remember that OwlTest uses Pylint to check that you have followed the <a href="view?page=style_guidelines">coding style guidelines</a> for this class. Deviations from these style guidelines will result in deductions from your final score.  Please read the feedback from Pylint closely.  If you have questions, feel free to consult <a href="view?page=pylint_errors">this page</a> and the class forums. </p>
<p>
When you are ready to submit your code to be graded formally, submit your code to the CourseraTest page for this mini-project that is linked on the main assignment page.
</p>
<h4>Phase One</h4>
<p>
You should first implement the <code>ClickerState</code> class.  This class will encapsulate many of the variables that you used in implementing <code>resources_vs_time</code> in the homework and keep track of the state of the game during a simulation.  By encapsulating the game state in this class, the logic for running a simulation of the game will be greatly simplified.  The <code>ClickerState</code> class must keep track of four things:
</p>
<ol>
<li>The total number of cookies produced throughout the entire game (this should be initialized to <code>0.0</code>).
</li>
<li>The current number of cookies you have (this should be initialized to <code>0.0</code>).
</li>
<li>The current time (in seconds) of the game (this should be initialized to <code>0.0</code>).
</li>
<li>The current CPS (this should be initialized to <code>1.0</code>).
</li>
</ol>
<p>
Note that you should use <code>float</code>s to keep track of all state properties.  You will have fractional values for cookies and CPS throughout.
</p>
<p>
During a simulation, upgrades are only allowed at an integral number of seconds as required in Cookie Clicker. (Upgrades will not be allowed at fractional seconds as in the homework).  However, the CPS value is a floating point number.  In addition to this information, your <code>ClickerState</code> class must also keep track of the history of the game.  We will track the history as a list of tuples.  Each tuple in the list will contain 4 values: a time, an item that was bought at that time (or <code>None</code>), the cost of the item, and the total number of cookies produced by that time.  This history list should therefore be initialized as <code>[(0.0, None, 0.0, 0.0)]</code>.
</p>
<p>
The methods of the <code>ClickerState</code> class interact with this state as follows:
</p>
<ul>
<li>
<code>__str__</code>: This method should return the state (without the history list) as a string in a human readable format.  This is primarily to help you develop and debug your program.
</li>
<li>
<code>get_cookies</code>, <code>get_cps</code>, <code>get_time</code>, <code>get_history</code>: These methods should simply return the current number of cookies, the current CPS, the current time, and the history, respectively.
</li>
<li>
<code>time_until</code>: This method should return the number of seconds you must wait until you will have the given number of cookies. Remember that you cannot wait for fractional seconds, so while you should return a <code>float</code> it should not have a fractional part.
</li>
<li>
<code>wait</code>: This method should "wait" for the given amount of time.  This means you should appropriately increase the time, the current number of cookies, and the total number of cookies.
</li>
<li>
<code>buy_item</code>: This method should "buy" the given item.  This means you should appropriately adjust the current number of cookies, the CPS, and add an entry into the history.
</li>
</ul>
<p>
If you are passed an argument that is invalid (such as an attempt to buy an item for which you do not have enough cookies), you should just return from the method without doing anything.
</p>
<h4>Phase Two</h4>
<p>
Once you have a complete <code>ClickerState</code> class, you are ready to implement <code>simulate_clicker</code>.  The <code>simulate_clicker</code> function should take a <code>BuildInfo</code> class, the number of seconds to run the simulation for, and a strategy function.  Note that <code>simulate_clicker</code> is a higher-order function: it takes a strategy function as an argument!
</p>
<p>
The first thing you should do in this function is to make a clone of the <code>build_info</code> object and create a new <code>ClickerState</code> object.  The function should then loop (in the same manner as in <code>resources_vs_time</code> from the homework) until the time in the <code>ClickerState</code> object reaches the duration of the simulation.
</p>
<p>
For each iteration of the loop, your <code>simulate_clicker</code> function should do the following things:
</p>
<ol>
<li>Check the current time and break out of the loop if the duration has been passed.
</li>
<li>Call the strategy function with the appropriate arguments to determine which item to purchase next.  If the strategy function returns <code>None</code>, you should break out of the loop, as that means no more items will be purchased.
</li>
<li>Determine how much time must elapse until it is possible to purchase the item.  If you would have to wait past the duration of the simulation to purchase the item, you should end the simulation.
</li>
<li>Wait until that time.
</li>
<li>Buy the item.
</li>
<li>Update the build information.
</li>
</ol>
<p>
Note that the <code>ClickerState</code> class already implements methods that will greatly simplify steps 3–6.  Use them!
</p>
<p>For correctness, you should not allow the simulation to run past the duration.  This means that you should not allow an item to be purchased if you would have to wait until after the duration of the simulation to have enough cookies.  Further, after you have exited the loop, if there is time left, you should allow cookies to accumulate for the remainder of the time left. Note that you <em>should</em> allow the purchase of items at the final duration time. Also, if you have enough cookies, it is possible to purchase multiple items at the same time step.  (Note that this differs from the actual Cookie Clicker game, where it is not possible to buy multiple items at the same time.)  This is most likely to happen exactly at the final duration time, when a strategy might choose to buy as many items as it can, given that there is no more time left.
</p>
<p>
Finally, you should return the <code>ClickerState</code> object that has captured the state of the game.
</p>
<p>
If you have implemented things correctly, with the provided <code>strategy_cursor</code> function, the given <code>SIM_TIME</code>, and default <code>BuildInfo</code>, the final state of the game should be:
</p>
<ul>
<li>Time: 10000000000.0
</li>
<li>Current Cookies: 6965195661.5
</li>
<li>CPS: 16.1
</li>
<li>Total Cookies: 153308849166.0
</li>
</ul>
<h4>Phase Three</h4>

<p>
Finally, you should implement some strategies to select items for you game.  You are required to implement the following strategies:
</p>
<ol>
<li>
<code>strategy_cheap</code>: this strategy should always select the cheapest item that you can afford in the time left.
</li>
<li>
<code>strategy_expensive</code>: this strategy should always select the most expensive item you can afford in the time left.
</li>
<li>
<code>strategy_best</code>: this is the best strategy that you can come up with.
</li>
</ol>
<p>
If there is not enough time left for you to buy any more items (or your strategy chooses not to), your strategy function should return <code>None</code>, otherwise your strategy functions should return a valid name of an item as a string.  As described above, this should cause your <code>simulate_clicker</code> function to exit the loop and finish the simulation.
</p>
<p>
For <code>strategy_best</code>, you will be graded on how many total cookies you are able to earn with the default <code>SIM_TIME</code> and <code>BuildInfo</code>.  To receive full credit, you must get at least $$1.25 \times 10^{18}$$ total cookies. In addition, you may implement as many other strategies as you like.  We will have a forum thread dedicated to showing off your favorite/best strategies!
</p>
<hr>
<div>
