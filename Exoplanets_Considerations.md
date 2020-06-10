# Exoplanets Considerations

##Disclaimer:

I’m not an astronomer or astrophysicist. The considerations show here are only for my understanding, and historic registry of my line of reasoning. 

I didn’t search about subject and my knowledge is of just a curious. So, early apologies. 

However, I wait some thoughts and conclusions can bring some interesting questions about this area.  

##Planetary Mass
File: analysis01.py
variables:
 - planet_mass
 - st_distance 

We'll do an initial analysis of the set of Exoplanets. The intention with this preprocessing is to discard systems that for some special reason may exit the pattern we want to find.

Plotting the mass of planets x distance:
<img src="/img/planets01.jpg" width="400px">

The first plotted image of the total universe of nearly 4000 exoplanets shows several outliers. We will initially limit the plot to planets with masses smaller then 1000 times that of Earth. For this study we will assume that more massive planets could alter the pattern (if it exists) of planet formation.

<img src="/img/planets02.jpg" width="400px">

The graph above shows a less massive concentration of planets well below the two hundred earth masses. It is important to note that we are not taking into account the type of detection, but apparently planets with less than 50 earth masses are much more common. In our solar system only Jupiter and Saturn have masses more than 20 times larger. 

<img src="/img/planets03.jpg" width="400px">

In plotting with planets with less than 200 earth masses, the concentration of records below the red line is visually detectable, coincidentally or not, starting around 20 earth masses.

<img src="/img/planets04.jpg" width="400px">

Making a cut on 20 land masses we decided to make also a cut on the planets located at more than 2000 parsecs. Our equipment is not efficient to find small planets at a distance greater than 750 parsecs.

<img src="/img/planets05.jpg" width="400px">

Thus, we will limit our study, first to systems that have at most planets with up to 1000 earth masses and are at a distance of up to 2000 parsecs. However, we decided to stretch up to 2000 pc, because our intention is, in the end, to locate positions for possible undiscovered planets. 