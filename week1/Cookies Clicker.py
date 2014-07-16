"""
Cookie Clicker Simulator
"""

import simpleplot
import codeskulptor
import math
codeskulptor.set_timeout(20)

import poc_clicker_provided as provided
#BuildInfo = provided.BuildInfo()
# Constants
SIM_TIME = 10000000000.0
GLOBAL_CLONE = [{i:80} for i in provided.BuildInfo().build_items()]

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._totalcookies = .0
        self._currentcookies = .0
        self._currenttime = .0
        self._cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        string = "Time: %1f Current Cookies: %f CPS: %.1f Total Cookies: %.1f _history (length: %d): %s"
        return string % (self._currenttime,self._currentcookies,self._cps,self._totalcookies,len(self._history),self._history)
    
    def get__totalcookies(self):
        """
        Return total number of cookies
        (not total number of cookies)
        Should return a float
        """
        return self._totalcookies
    
    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)
        Should return a float
        """
        return self._currentcookies
    
    def get_cps(self):
        """
        Get current CPS
        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time
        Should return a float
        """
        return self._currenttime
    
    def get_history(self):
        """
        Return _history list

        _history list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: (0.0, None, 0.0, 0.0)
        """
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        return 0.0 if self._currentcookies > cookies else math.ceil((cookies - self._currentcookies)/self._cps)
        
            
    
    def wait(self, time):
        """
        Wait for given amount of time and update state
        Should do nothing if time <= 0
        """
        if time > 0:
            self._currenttime += time
            self._currentcookies += time*self._cps
            self._totalcookies += time*self._cps
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._currentcookies - cost >= 0:
            self._cps += additional_cps
            self._currentcookies -= cost
            self._history.append((self.get_time(),item_name,
                             cost,self._totalcookies))


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy. Returns a ClickerState
    object corresponding to game.
    """
    
    # Replace with your code
    test = ClickerState()
    while test.get_time() <= duration:
        _stragety = strategy(test.get_cookies(),test.get_cps(),duration - test.get_time(),build_info)
        if _stragety!= None and test.time_until(build_info.get_cost(_stragety))+test.get_time() <= duration:
            test.wait(test.time_until(build_info.get_cost(_stragety)))
        else:
            test.wait(duration - test.get_time())
            break;
            
        test.buy_item(_stragety,build_info.get_cost(_stragety),build_info.get_cps(_stragety))
        build_info.update_item(_stragety)
    return test


def strategy_cursor(cookies, cps, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic strategy does not properly check whether
    it can actually buy a Cursor in the time left. Your strategy
    functions must do this and return None rather than an item you
    can't buy in the time left.
    """
   
    return "Cursor"
def strategy_none(cookies, cps, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that you can use to help debug
    your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, time_left, build_info):
    """
    pass
    """
    _item = build_info.build_items()[0]
    _min = build_info.get_cps(_item)
    for item in build_info.build_items()[1:]:
        if _min > build_info.get_cost(item):
            _min = build_info.get_cost(item)
            _item = item
       
    
    return _item if cookies+cps*time_left >= build_info.get_cost(_item) else None

def strategy_expensive(cookies, cps, time_left, build_info):
    """
    pass
    """
    _item = build_info.build_items()[0]
    _max = build_info.get_cps(_item)
    for item in build_info.build_items()[1:]:
        if _max < build_info.get_cost(item) and cookies+cps*time_left >= build_info.get_cost(item):
            _max = build_info.get_cost(item)
            _item = item
       
    
    return _item if cookies+cps*time_left >= build_info.get_cost(_item) else None

def strategy_best(cookies, cps, time_left, build_info):
    """
    A strategy for the best game on CookiesClick
    the first click 'll pick a Cursor and until 4 times on a collection called globalclone
    next iteration on globalclone and pick the next item and count until 4
    """
    
    #for item in GLOBAL_CLONE:
    # _item = item.keys()[0]
    # if item[_item] > 0:
    # item[_item]-=1
    # return _item
    # return "Antimatter Condenser"
    for item in GLOBAL_CLONE:
        _item = item.keys()[0]
        if item[_item] > 0:
            item[_item]-=1
            return _item
    return "Antimatter Condenser"
        
        
def run_strategy(strategy_name, time, strategy):
    """
Run a simulation with one strategy
"""
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    #_history = state.get_history()
    #_history = [(item[0], item[3]) for item in _history]
    
    #simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [_history], True)
    
    
def run():
    """
    Run the simulator.
    """
    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor)
    #simulate_clicker(build_info, duration, strategy):
    #print simulate_clicker(provided.BuildInfo({'Cursor':
    # [15.0, 0.10000000000000001]
    # }, 1.15), 500,
     # strategy_cursor)
    #print simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001]}
     # , 1.15), 10,strategy_cursor)
    # Add calls to run_strategy to run additional strategies
    #run_strategy("Cheap", SIM_TIME, strategy_cheap)
    #run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
#run()
#obj = ClickerState()
#obj.wait(45)
#obj.buy_item('item', 1.0, 3.5)
#print obj.time_until(49)
#b = provided.BuildInfo()
#print GLOBAL_CLONE
    
#wait_test.run_test(ClickerState)
#time_until_test.run_test(ClickerState)
#buy_test.run_test(ClickerState)
#testsuite.run_tests(ClickerState,simulate_clicker,strategy_cursor)
