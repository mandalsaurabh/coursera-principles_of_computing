<h2 class="course-page-header">
    2048    <a class="coursera-reporter-link" title="Click here if you're experiencing technical problems or found errors in the course materials." target="_blank" href="https://class.coursera.org/principlescomputing-001/help/pages?url=https%3A%2F%2Fclass.coursera.org%2Fprinciplescomputing-001%2Fwiki%2Fview%3Fpage%3D2048">
      Help
    </a>
    <a data-coursera-admin-helpwidget-link rel="help" href="https://class.coursera.org/mooc/help/pages/setup" title="Course Page Setup" style="display:none;">Learn more.</a>
</h2>


<p></p>
<h4>Overview</h4>
<p> 
2048 is a simple grid-based numbers game. You can play it <a href="http://gabrielecirulli.github.io/2048/" target="_blank">here</a>.
</p>
<p>
The object of the game is to combine tiles with the same number to make larger numbered tiles.  You "win" when you create a 2048 tile.  You can slide the tiles in any direction (left, right, up, or down) to move them.  When you do so, if two tiles of the same number end up next to each other, they combine to form a new tile with twice the value.  On each turn, you can slide all of the tiles left, right, up, or down.  The tiles all slide as far as they can go and merge as appropriate.  After the tiles slide a new tile is added to the board randomly.
</p>
<p>

For this assignment, your task is to implement a version of the 2048 game.  Since we will provide a graphical user interface for the game, your task is to implement the game logic in terms of a <code>TwentyFortyEight</code> class in Python.  Although the original game is played on a $$4 \times 4$$ grid, your version should be able to have an arbitrary height and width.  Since we will use grids in several assignments, you should familiarize yourself with the <a href="grids">grid conventions</a> we will use in this course.
</p>
<p>
We have provided the following <a href="http://www.codeskulptor.org/#poc_2048_template.py" target="_blank">template</a> that contains an outline of the <code>TwentyFortyEight</code> class.  The signature (name and parameters) of the functions, classes, and methods in this file must remain unchanged, but you may add any additional functions, methods, or other code that you need to. 
</p>
<p>
</p>
<h4>Testing your mini-project</h4>
As always, testing is a critical part of the process of building your mini-project.  Remember you should be testing each method as you write it.  Don't try to implement all of the methods and then test,  You will have lots of errors that all interact in strange ways that make your program very hard to debug.
<p>
</p>
<ul>
<li>
As you implement the <code>TwentyFortyEight</code> class, we suggest that you build your own collection of tests using the <a href="http://www.codeskulptor.org/#poc_simpletest.py" target=""><code>poc_simpletest</code> module</a> that we have provided.  Please review this <a href="view?page=testing_methodogy">page</a> for an overview of the capabilities of this module.  These tests can be organized into a separate test suite that you can import and run in your program as we demonstrated for <a href="mancala">Solitaire Mancala</a>.  To facilitate testing on the first few mini-projects, we will create a thread in the forums where students may share and refine their test suites for each mini-project.

<p></p>
</li>
<li>
Note that the template imports a file <code>poc_2048_gui</code> which includes a  GUI that we have written for playing 2048 in CodeSkulptor.  This GUI is created and run by the last line of the template.  (For information on how importing works, please <a href="view?page=imports">this page</a>.) While you are implementing the <code>TwentyFortyEight</code> class, you should comment out these two lines and test each method individually using your test suite.  Once your code has passed these tests, you can uncomment the two lines that import and run the GUI. You can then use this GUI to further test your code.
</li>
<p>
</p>
<li>
Finally, submit your code (with the two lines that import and run the GUI commented out) to this <a href="http://codeskulptor.appspot.com/owltest/?urlTests=poc.week0_tests.py&amp;urlPylintConfig=poc.pylint_config.py&amp;imports=%7Bpoc:(poc_2048_gui)%7D" target="">Owltest</a> page.  The OwlTest page has a pale yellow background and does <b>not</b> submit your project to Coursera.  OwlTest is just meant to allow you to test your mini-project automatically.  Note that trying to debug your mini-project using the tests in OwlTest can be very tedious since they are slow and give limited feedback.  Instead, we <i>strongly</i> suggest that you first test your program using your own test suite and the provided GUI.  Programs that pass these tests are much more likely to pass the OwlTest tests.
</li>
</ul>
<p>
Remember that OwlTest uses Pylint to check that you have followed the <a href="view?page=style_guidelines">coding style guidelines</a> for this class. Deviations from these style guidelines will result in deductions from your final score.  Please read the feedback from Pylint closely.  If you have questions, feel free to consult <a href="view?page=pylint_errors">this page</a> and the class forums. </p>
<p>
When you are ready to submit your code to be graded formally, submit your code to the CourseraTest page for this mini-project that is linked on the main assignment page.  Note that the CourseraTest page looks similar to the OwlTest page, but they are <em>not</em> the same!  The CourseraTest page has a <b>white</b> background and does submit your grade to Coursera.
</p>
<h4>Phase One</h4>
<p></p>
<p>
You should first implement a function <code>merge(line)</code> that models the process of merging all of the tile values in a single row or column.  This function takes the list <code>line</code> as a parameter and returns a new list with the tile values from <code>line</code> slid towards the front of the list and merged. This is one of the more challenging parts of implementing the game.  Remember, you are always sliding the values in the list towards the front of the list (the list position with index $$0$$).  (You will make sure you order the entries in <code>line</code> appropriately when you call this function later.)   Empty grid squares with no displayed value will be assigned a value of zero in our representation.
</p>
<p>
For example, if a row of the board started as follows:
</p>
<p>
<img src="https://storage.googleapis.com/codeskulptor-assets/poc_2022.png" width="200"></p>
<p>
And you slide the tiles left, the row would become:
</p>
<p>
<img src="https://storage.googleapis.com/codeskulptor-assets/poc_4200.png" width="200"></p>
<p>
Note that the two leftmost tiles merged to become a 4 and the third 2 just slides over next to the 4.
</p>
<p>
A given tile can only merge once on any given turn, although many pairs of tiles could merge on a single turn.
</p>
<p>
For the above example, the input to the <code>merge</code> function would be the list <code>[2, 0, 2, 2]</code>.  The function should then produce the output <code>[4, 2, 0, 0]</code>.  We suggest you begin to implement this function as follows:
</p>
<p>
</p>
<ol>
<li>Start with a result list that contains the same number of $$0$$'s as the length of the <code>line</code> argument.
</li>
<li>Iterate over the <code>line</code> input looking for non-zero entries.  For each non-zero entry, put the value into the next available entry of the result list (starting at position 0).
</li>
</ol>
<p>
Notice if you only follow this process, you would end up with the result <code>[2, 2, 2, 0]</code>.  
</p>
<p>
Now you should think through what you should add to your function in order to merge tiles.  Keep in mind, however, that any tile should only be merged once and that these merges should happen in order from lowest index to highest index.  For instance, on the input <code>[2, 0, 2, 4]</code>, the result should be <code>[4, 4, 0, 0]</code>, <b>not</b> <code>[8, 0, 0, 0]</code>.  In order to merge two tiles, you will need to check if the last tile you added to the result list is the same as the current tile you are trying to add.  If so, then you should merge the tiles.  You will also need to track whether the last tile you added was merged, so that you do not merge a tile twice.  We suggest using a boolean flag that you set to <code>True</code> or <code>False</code> appropriately to indicate whether the last tile was merged.
</p>
<p>
Here are some simple tests you should try:
</p>
<ul>
<li>
<code>[2, 0, 2, 4]</code> should return <code>[4, 4, 0, 0]</code>
</li>
<li>
<code>[0, 0, 2, 2]</code> should return <code>[4, 0, 0, 0]</code>
</li>
<li>
<code>[2, 2, 0, 0]</code> should return <code>[4, 0, 0, 0]</code>
</li>
<li>
<code>[2, 2, 2, 2]</code> should return <code>[4, 4, 0, 0]</code>
</li>
<li>
<code>[8, 16, 16, 8]</code> should return <code>[8, 32, 8, 0]</code>
</li>
</ul>
<h4>Phase Two</h4>
<p>
In the template, we have provided the skeleton of a <code>TwentyFortyEight</code> class.  You should first implement the grid logic.  The <code>__init__</code> method takes the number of rows and columns in the grid.  You should store the number of rows and columns and then reset the grid to have $$row \times col$$ zeros (using the <code>reset</code> method, which will also be called when you click the "reset" button in the GUI).  <b>Note that neither <code>__init__</code> nor <code>reset</code> should add any tiles to the grid.</b>  The <code>new_tile</code> method, which you will implement in phase 3, will be called (by the GUI or tester) to add new tiles to the grid, as necessary.
</p>
<p>
You should then implement the <code>get_grid_height</code>, <code>get_grid_width</code>, <code>__str__</code>, and <code>get_tile</code> methods.  The first three methods should return the number of rows in the grid, return the number of columns in the grid, and return a string representation of the grid (to help you debug).  The <code>get_tile(self, row, col)</code> method should return the value of the tile at the position $$(row, col)$$ in the grid.  Note that the rows of the grid are indexed from top to bottom starting at zero while the columns are indexed from left to right starting at zero.
</p>
<p>
You should test these functions.  During testing, you will want to implement the <code>set_tile</code> method so that you can start with different board states.
</p>
<h4>Phase Three</h4>
<p>
You are now ready to implement the final two methods, <code>new_tile</code> and <code>move</code>.  The new tile method should randomly select an empty grid square (one that currently has a value of $$0$$) if one exists and place a new tile in that square.  The new tile should have the value 2 90% of the time and the value 4 10% of the time.
</p>
The <code>move</code> method is where the real logic of the game goes.  This method should slide all of the tiles in the given direction.  The <code>direction</code> argument will be one of the constants, <code>UP</code>, <code>DOWN</code>, <code>LEFT</code>, or <code>RIGHT</code>.  There are many ways of implementing the <code>move</code> method.  Here is one approach that will help you avoid writing separate pieces of code for each direction.  
<p></p>
<p>
For each direction, we recommend pre-computing a list of the indices for the <em>initial</em> tiles in that direction. Initial tiles are those whose values appear first in the list passed to the <code>merge</code> function.  For example, the initial tiles for the <code>UP</code> direction lie along the top row of the grid and in a $$4 x 4$$ grid have indices <code>[(0, 0), (0, 1), (0, 2), (0, 3)]</code>.  Since these lists of indices will be used throughout the game,  we recommend computing them once in the <code>__init__</code> method and then storing them in  a dictionary where the keys are the direction constants (<code>UP</code>, <code>DOWN</code>, <code>LEFT</code>, and <code>RIGHT</code>).
</p>
<p></p>
<p>
With this dictionary computed, the <code>move</code> method can be implemented as follows.  Given a direction, iterate over the list of initial tiles for that direction and perform the following three steps for each initial tile:
</p>
<ol>
<li> Use the offsets in the provided <code>OFFSETS</code> dictionary to iterate over the entries of the associated row or column, retrieve the tile values from those entries, and store them in a temporary list.
</li>
<li> Use your <code>merge</code> function to merge the tile values in this temporary list.
</li>
<li> Iterate over the entries in the row or column again and store the merged tile values back into the grid 
</li>
</ol>
<p>
To illustrate this process, consider updating the state of the game via the method call  <code>move(UP)</code> in the configuration shown below.  </p>
<p>
<img src="https://storage.googleapis.com/codeskulptor-assets/poc_2048_before.png" width="200"></p>
<p>
Following our outline above, we retrieve the list of initial tiles <code>[(0, 0), (0, 1), (0, 2), (0, 3)]</code> for the top row of the grid and use the offset <code>(1, 0)</code> associated with the <code>UP</code> direction to iterate over the grid indices for each column.  For the second column, these indices are <code>[(0, 1), (1, 1), (2, 1), (3, 1)]</code>.  Using these indices, we can create a temporary list <code>[2, 0, 2, 2]</code> that holds the tile values in this column, apply <code>merge</code> to compute the merged list <code>[4, 2, 0, 0]</code>, and finally copy the new merged tile values back into the grid.  This sequence of operations yields the grid shown below. </p>
<p>
</p>
<p></p>
<p>
<img src="https://storage.googleapis.com/codeskulptor-assets/poc_2048_after.png" width="200"></p>
<p>
If you have done this correctly, a single call to the <code>move</code> method should slide all of the tiles in the given direction.  All that remains is that you must determine if any tiles have moved.  You can easily do this when you put the line back into the grid.  For each element, check if it has changed and keep track of whether any tiles have changed.  If so, you should add a new tile to the grid, by calling your <code>new_tile</code> method.  Now, you are ready to run the GUI and play 2048!
</p>
<p>
Note that you have not written any logic at this point to determine whether the user has "won" or "lost" the game.  This is not required for this assignment, but you can think about how to do so and add it if you would like.
</p>
<p></p>
<hr>
<div>
