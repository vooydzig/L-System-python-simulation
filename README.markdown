Installation:
=============

Install additional apps:
-----------------------

Required apps are:

* python 2.6
* pyglet 1.1.4
* rabbyt 0.8.3

Clone to suitable location.

Usage:
======
Window
-------
Use main.Window class for Your simulations. 
TODO: add more window methods

Create LSystem:
----
system = LSystem2(start = 'F-F-F-F', lenght = 10, angle = 90, steps = 4, name =
'Sample')

params are:
* start - axiom, 
* lenght - line lenght in pixels that is used for drawing
* angle - angle in degrees used for rotation
* steps - number of iterations
* name - used when doing screenshots

Add rules:
------
system.rules = {
    'F' = 'FF-F-F-F-FF'
}

rules is dictionary used to generate next iterations

use `system.simulate()` to generate final L-System.

Keyboard:
--------
* 's' - generates screenshoot in gfx/ directory. Name of the screenshoot is:
  [system.nam]e_[system.steps].png
* '+' - generate next iteration, add one step 
* '-' - generate previous iteration
* '*' - multiply line lenght by 2
* '/' - divide line lenght by 2
