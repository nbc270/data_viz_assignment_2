Assignment 2 by Nathan Caplan (nbc270)
A Webpage for my visualization can be found [here](https://nbc270.github.io/data_viz_assignment_2/). 


Methods for reproducibility: 
1) Run get_bus_locations.py to get the current location of each bus for the route you select (in this case M11). Name the cvs according to the time as you will have to find the route that matches the time of the bus locations in stops.txt later.  In the case of this viz, things will be occuring around 12:38 PM on Friday.
2) Run hw_2.ipynb accrodingly to get M11 Bus route and stop locations that are occuring around 12:38 on a weekday. Can change occording to the time you run get_bus_locations.py  by finding weekday, weekend, and holiday schedules in stops.txt. 
3) Save the viz as an html and create an iframe in a github readme (as seen below). 

<iframe width="450" height="600" src='hw_2.html'></iframe>
The challenge was to accurately map out a bus route for a certain line, their respotive stops, and the busses locations at a certain time. For the purpose of this visualization I used the M11 bus line which goes from Riverbank Park down to the West Village. I chose 12:38 PM to map out bus locations, as explained above. The color line indidcates the beginning of the route (blue) which changes over the length of the route to red (the end). We see the live bus locations using green markers, some of which were at bus stops, using blue markers. This visualization uses many idioms, such as zoom control, which is necessary to view the viz in great detail, layer control, in order to see or remove from view certain icons, and tool tip which provides captions of bus stops and bus names.
