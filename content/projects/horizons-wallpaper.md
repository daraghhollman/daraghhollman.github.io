+++
title = 'Horizons Wallpaper'
date = 2024-07-20T20:08:30+01:00
tags = ["art", "python", "software"]
+++

# Horizons Wallpaper

A python script to plot a live wallpaper of the solar system from the orbital information of specified objects.

{{< img src=/photos/horizons-wallpaper.jpg caption="A sample output from the script.">}}

This script queries the API of NASA JPL's Horizons System to obtain orbital positions in cartesian coorinates. These are then drawn to an image (flattened to the ecliptic) and saved as a png or jpg to a path of your chosing.

The idea being: if you ran this script every day, and automatically updated your wallpaper, you would essentially have a live wallpaper of the positions of planets, asteroids, and spacecraft.

Horizons Wallpaper is published on [Github](https://github.com/daraghhollman/horizons-wallpaper).
