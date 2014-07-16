<h2 class="course-page-header">
    Zombie Apocalypse (BFS)    <a class="coursera-reporter-link" title="Click here if you're experiencing technical problems or found errors in the course materials." target="_blank" href="https://class.coursera.org/principlescomputing-001/help/pages?url=https%3A%2F%2Fclass.coursera.org%2Fprinciplescomputing-001%2Fwiki%2Fview%3Fpage%3Dzombie">
      Help
    </a>
    <a data-coursera-admin-helpwidget-link rel="help" href="https://class.coursera.org/mooc/help/pages/setup" title="Course Page Setup" style="display:none;">Learn more.</a>
</h2>


<h4>Overview</h4>
In this mini-project, we will create a simulation of zombies and humans interacting on a grid.  As in the movies, our zombies are hungry for human brains.  As a result, zombies chase humans and humans flee from zombies.  To keep our simulation manageable, the positions of the zombies and humans will be restricted to a grid.   In our simulation, zombies are not very agile and can only move up, down, left or right in one step of the simulation.   On the other hand, humans are more agile and can move in these four directions as well as the four neighboring diagonal directions.  If a zombie catches a human by positioning itself in the same cell, the zombie enjoys some delicious human brains.  Being a Computer Scientist, the human has plenty of brains to spare and continues to live on in our simulation ☺. 
<p></p>
<p>
To enhance the realism of our simulation, some of the cells in this grid will be marked as impassable and restrict zombie/human movement so that they can not move through these cells. Our task in this simulation is to implement a <code>Zombie</code> class that encapsulates the core mechanisms of this simulation and that interacts with a GUI that we have created for visualizing the simulation in CodeSkulptor.   This <code>Zombie</code> class is a sub-class of the <a href="http://www.codeskulptor.org/#poc_grid.py" target="_blank"><code>Grid</code> class</a> and inherits the <code>Grid</code> class methods.  Passable cells in the grid correspond to <code>EMPTY</code> cells while <code>FULL</code> cells are impassable.  Humans and zombies can only inhabit passable cells of the grid.  However, several humans and zombies may inhabit the same grid cell.
</p>
<p>
This <code>Zombie</code> class also includes two lists, one for zombies and one for humans.  Note that the entries in each list are cell indices of the form <code>(row, col)</code> that represent the position of zombies/humans in the grid.  Each step in the simulation will either update the positions of the zombies based on the state of the grid and the position of the humans or update the positions of the humans based on the state of the grid and the position of the zombies.

</p>
<h4>Testing your code</h4>
Your task for this mini-project is to implement the <code>Zombie</code> class described in detail below.  Remember to test each method as you implement it using the testing philosophy discussed in class.  You are also welcome to experiment with your simulation code in CodeSkulptor using our provided GUI. Note that the template contains two lines of the form
<pre>import poc_zombie_gui
poc_zombie_gui.run_gui(Zombie(30, 40))
</pre>
that will load, create and run our GUI in CodeSkulptor.  Once you are confident that your implementation works correctly, test your code using our <a href="http://codeskulptor.appspot.com/owltest?urlTests=poc.week4_tests.py&amp;urlPylintConfig=poc.pylint_config2.py&amp;imports=%7Bpoc:(poc_grid,%20poc_queue,%20poc_zombie_gui)%7D&amp;" target="_blank">Owltest</a> test suite.  
<p></p>
<p>
Remember that OwlTest uses Pylint to check that you have followed the <a href="view?page=style_guidelines">coding style guidelines</a> for this class. Deviations from these style guidelines will result in deductions from your final score.  Please read the feedback from Pylint closely.  If you have questions, feel free to consult <a href="view?page=pylint_errors">this page</a> and the class forums. </p>
<p>
When you are ready to submit your code to be graded formally, submit your code to the CourseraTest page for this mini-project that is linked on the main assignment page.
</p>


<h4> Phase One</h4> 
 In phase one, we will implement the basic methods for the <code>Zombie</code> class.  We suggest that you start from <a href="http://www.codeskulptor.org/#poc_zombie_template.py" target="_blank">this template</a>.   Note that the <code>Zombie</code> class is a subclass of the <a href="http://www.codeskulptor.org/#poc_grid.py" target="_blank"><code>Grid</code> class</a> and inherits all of its methods. <!--Running the template in CodeSkulptor will create a GUI that allows you to mark cells in the grid as being impassable (black) via mouse clicks on the canvas.-->
<p></p>
<p>
The template contains an implementation of the <code>__init__</code> method for the <code>Zombie</code> class.  The initializer takes two required arguments <code>grid_height</code> and <code>grid_width</code>. The initializer also takes three optional arguments <code>obstacle_list</code>, <code>zombie_list</code>, and <code>human_list</code> which are lists of cells that initially contain obstacles, zombies and humans, respectively.  For phase one, your task is to implement the remaining seven <code>Zombie</code> methods:
</p>
<ul>
<li> <code>def clear(self):</code>  Reset all cells in the grid to be passable and reinitialize the human and zombie lists to be empty. Remember that you can use the <code>clear</code> method from the <code>poc_grid.Grid</code> class to clear the grid of impassable cells. Examine the implementation of the <code>__init__</code> method for how to call this method.
</li>
<li>       
    <code>def add_zombie(self, row, col):</code> Add a zombie to the zombie list at the supplied row and column.
 </li>
<li>        
<code>def num_zombies(self):</code>
        Return the number of zombies in the zombie list.
</li>
<li>       
    <code>def zombies(self):</code>
        Generator that allows you to iterate over zombies in the zombie list.  Here, a zombie is a tuple of the form <code>(row, col)</code> indicating the zombie's location in the grid. The generator <b>must</b> yield the zombies in the order they were added (even if they have moved). Remember that you can use a generator to implement this method in one or two lines of code.
</li>
<li>
<code>def add_human(self, row, col):</code> Add a human to the human list at the supplied row and column.
 </li>
<li>
    <code>def num_humans(self):</code>
        Return the number of humans in the human list.
 </li>
<li>
<code>def humans(self):</code>
        Generator that allows you to iterate over humans in the human list. The generator <b>must</b> yield the humans in the order they were added (even if they have moved). Again, you can use a generator to implement this method in one or two lines of code.
</li>
</ul>

Once you have successfully implemented these methods, you should be able to add zombies (red cells) and humans (green cells) to the simulation by toggling the button labelled <code>"Mouse click: ..."</code> and then clicking on the canvas. Cells that are occupied by both zombies and humans are purple.

<h4>Phase Two </h4>
Phase two is the core of this mini-project.  Your task will be to compute a simple approximation of the distance from each cell in the grid to the nearest zombie (or human).  This distance will correspond to the length of the <em>shortest</em> sequence of adjacent grid cells (a path) from the cell to a zombie.  This 2D array of integer distances is a <em>distance field</em>.  The image below shows an example of two (red) zombies on a $$4 \times 6$$  grid and the distances from each cell in the grid to the nearest zombie.  Note that in this diagram, we are using the cell's four neighbors when determining whether cells are adjacent.
<p></p>
<p>
<img src="https://storage.googleapis.com/codeskulptor-poc/poc_distance_field.png" width="300" height="200"></p>
<p></p>
<p>
Observe that the distances in this example grow in a manner strikingly similar to the order in which cells are visited during breadth-first search.  This observation is not a coincidence.  In fact, this distance field was computed using breadth-first search.  To compute this distance field, start by recalling the English description of <a href="view?page=bfs" target="_blank">breadth-first search</a>.
</p>
<pre>while boundary is not empty:
    current_cell  ←  dequeue boundary
    for all neighbors neighbor_cell of current_cell:
        if neighbor_cell is not in visited:
            add neighbor_cell to visited
            enqueue neighbor_cell onto boundary
</pre>
This description can be modified to compute a distance field during breadth-first search as follows:  
<p>
</p>
<ul>
<li>  Create a new grid <code>visited</code> of the same size as the obstacle grid and initialize its cells to be empty.
</li>
<li>  Create a 2D list <code>distance_field</code> of the same size as the grid and initialize each of its entries to be the product of the height times the width of the grid. (This value is larger than any possible distance.)
</li>
<li> Create a queue <code>boundary</code> that is a <b>copy</b> of either the zombie list or the human list.  For cells in the queue, initialize <code>visited</code> to be <code>FULL</code> and <code>distance_field</code> to be zero.  We recommend that you use our <a href="http://www.codeskulptor.org/#poc_queue.py" target="_blank"><code>Queue</code> class</a>.
</li>
<li> For each <code>neighbor_cell</code> in the inner loop, check whether the cell is passable and update the neighbor's distance to be the minimum of its current distance  and <code>distance_field[cell_index[0]][cell_index[1]] + 1</code>.
</li>
</ul>
<p></p>
<p>
This method computes distances in exactly the order that the wild-fire spreads.  When a <code>neighbor_cell</code> is added to the queue, that neighbor's distance from a start position is just the distance to the cell <code>current_cell</code> plus the one step to the neighbor. Working from the outline above, your task in phase two is to implement the method <code>compute_distance_field</code> as specified below:
</p>
<p></p>
<p>
</p>
<ul><li>
<code>def compute_distance_field(self, entity_type):</code>
        This method returns a 2D distance field computed using four-way distance for the given entity type (either <code>ZOMBIE</code> or <code>HUMAN</code>).  Note that entries of the computed distance fields should be zero at the entities in the specified list. Non-zero distances should be computed using the shortest path computation based on breadth-first search described above.  These shortest paths should avoid impassable cells.
</li></ul>
Finally, if you are having trouble converting our English description above into Python, remember that the  <code>update_boundary()</code> method from the <a href="http://www.codeskulptor.org/#poc_wildfire_student.py" target="_blank">wild-fire demo</a> implements one step of breadth-first search.
<h4>Phase Three </h4>
 
In phase three, your task is to implement two final methods that update the positions of the zombies and humans, respectively.
<p></p>
<p>
</p>
<ul>
<li>
<code>    def move_humans(self, zombie_distance): </code>
        This method updates the entries in the human list to model humans avoiding zombies.  Each human either stays in its current cell or moves to a neighboring cell to maximize its distance from the zombies. Specifically, humans move to a cell that maximize their distance from the zombies according to the supplied <code>zombie_distance</code> field.  In the case where several cells shared the same maximal distance, we recommend (but do not require) choosing among these cells at random.

<p>   
</p>
</li>
<li>
 <code>def move_zombies(self, human_distance):</code>
       This method updates the entries in the zombie list to model zombies chasing humans.  Each zombie either stays in its current cell or moves to a neighboring cell to minimize its distance to the humans. Specifically, zombies moves to the cell that minimizes their distance to the humans according to the supplied <code>human_distance</code> field.  In the case where several cells shared the same minimal distance, we recommend choosing  (but do not require) among these cells at random.
</li>
</ul>
Once you have successfully implemented the three methods in phase two and phase three, the buttons in the GUI labelled <code>"Zombies stalk</code> and <code>"Humans flee"</code>  should work.  Zombies should stalk humans and humans should flee zombies.  We encourage you to spend some time testing/experimenting with the simulation using our GUI. Once your code works, submit it to Owltest for grading.
<h4>Just for fun! Observations from the simulation</h4>
At a distance, zombies are quite good at finding humans (even ones hiding in buildings) since breadth-first search always searches the interiors of buildings (provided there is an entrance).  The human distance field decreases steadily and always reaches zero at a delicious human brain.  Humans, on the other hand, aren't so smart while fleeing since they greedily maximize the local distance away from the nearest zombies on each step.  As a result, humans often run to the nearest corner of a building and cower as the zombies approach.  (Hey, this is a pretty realistic simulation!)
<p></p>
<p>
However, in close quarters, humans have a large advantage since they can move diagonally.  Unless cornered by multiple zombies, humans can easily out-maneuver a single zombie and avoid having their brains eaten.  For packs of zombies inhabiting a single cell, the strategy for breaking ties in <code>move_zombies</code> is important. When the pack has a choice between moving to two neighboring cells that minimize distance, always choosing the one cell or the other causes the zombies to stay in clumped in a single cell.  Having each zombie choose between the two cells at random causes the pack to tend to disperse.
</p>
<p></p>
<p>
This situation arises when the pack is chasing a human that is fleeing diagonally (say down and left). There are two directions (down or left) that are available to the zombies that minimize the distance to the human.  Instead of having all of the zombies move in the same direction, each zombie should choose one of the two optimal directions randomly.  With the random approach, some zombies go down and some zombies go left and the pack of zombies tends to spread out. This behavior makes the zombies more likely to catch the human when he/she ends up huddled in a corner.  
</p>
<p></p>
<p>
There are several other interesting scenarios in the simulation that we will let you explore on your own.  For example, you might consider creating a "zombie-proof" building that exploits the human's ability to move diagonally between obstacles. Feel free to post interesting scenarios that you discover in the forum. So, have fun and enjoy some "Brains!"
</p>
<hr>
<div>
