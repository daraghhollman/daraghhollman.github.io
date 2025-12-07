+++
date = '2025-08-04T16:19:30+01:00'
draft = true
title = 'Automatic detection of magnetic boundary crossings at Mercury'
mathjax = true
+++

Recently I submitted my first 1st author publication to the [Journal of
Geophysical Research: Machine Learning and
Computation](https://agupubs.onlinelibrary.wiley.com/journal/29935210). It is
currently undergoing peer review prior to publication, however the
[preprint](https://essopenarchive.org/users/867402/articles/1320325-identifying-messenger-magnetospheric-boundary-crossings-using-a-random-forest-region-classifier)
is currently available to view online.

In this post, I will endeavour to explain the work with plain language, and
provide further diagrams and figures.

## Contents
- [Background](#background)
    - [Bar-Magnet Earth](#bar-magnet-earth)
    - [The Magnetosphere](#the-magnetosphere)
    - [Mercury's Magnetosphere](#mercurys-magnetosphere)
- [Our Aim](#our-aim)
- [Methods](#methods)
    - [Modelling](#modelling)
    - [Model Application](#model-application)

## Background

### Bar-Magnet Earth
Most of the planets in the Solar System are magnetised, essentially acting as a
large bar magnet in space. Just like you may have seen with [iron filings in
science class](https://www.youtube.com/watch?v=qhZZ0ArIfhI), the magnetic field
draws lines from the north pole to the south pole (of the magnet)!

![Earth's magnetic field is like a bar-magnet](/images/earth_bar_magnet.webp)


### The Magnetosphere
If any of the planets existed in isolation, this magnetic field would stretch
out indefinitely (though getting weaker with distance). However, the Sun sends
out a stream of charged particles in all directions called the solar wind which
interact with the magnetic field of the planet. This interaction forms a large
and dynamic magnetic bubble (known as a magnetosphere) which stretches
downstream like a windsock. We label two boundaries of this bubble:

- **The bow shock** - where the solar wind rapidly decelerates and compresses
when it encounters Mercury. It goes from supersonic, to subsonic. You could
think of this like the shockwave a supersonic jet might make in the air:
Mercury's magnetosphere is the jet, and the solar wind rushing past is the air.
- **The magnetopause** - separating the planet's magnetic field from that of
the solar wind and the Sun.

These two boundaries separate the space environment around the planet into
three distinct regions:
- **Solar Wind** (outside of the bow shock)
- **Magnetosheath** (between the bow shock and magnetopause)
- **Magnetosphere** (within the magnetopause)

![An example magnetosphere](/images/magnetosphere_diagram.webp)

### Mercury's Magnetosphere
Due to changing external conditions, the location of the bow shock and
magnetopause can vary rapidly and dramatically. This is especially the case at
Mercury, the closest planet to the Sun, with the weakest magnetic field of all
the magnetised planets. Mercury's magnetosphere experiences relatively extreme
events much more often than at Earth, which make it an incredible useful lab
for understanding how extreme process affect magnetospheres in general.

Two spacecraft have previously measured the boundaries of Mercury's
magnetosphere. Mariner 10 was the first to encounter Mercury's bow shock and
magnetopause across three flybys between 1974 and 1975. The MESSENGER mission,
launched in 2004, made three flybys of Mercury before entering continual orbit
in 2011. This was followed by almost 4 years of exploration, with orbits
taking the spacecraft within the vicinity of these boundaries thousands of
times.

## Our Aim

Crossings of magnetospheric boundaries for any planet are visually identifiable
in data from spacecraft magnetometers (instruments which measure the magnetic
field strength and direction at the position of the spacecraft) as well as
other instruments.

However, due to the extreme variability of Mercury's boundaries, we often
observe multiple crossings as the boundary moves back and forth over the
spacecraft. Because of this, we can observe multiple crossings of the
boundaries over timescales of seconds, which make visual identifications
difficult, time-consuming, and tedious. As a result, previous identifications
of boundaries for the MESSENGER mission [e.g. [Philpott et al.
(2020)](https://doi.org/10.1029/2019ja027544)] instead describe a range of time
\- an interval - in which there were one or more crossings. These are hugely
varied, ranging from near instantaneous (for times where only one crossing is
present) to several hours long.

Our aim was to develop a new automated method to detect each individual
crossing for the entire MESSENGER mission.

## Data

We inspect magnetic field data from spacecraft in the form of **time series**.
The magnetic field is a **vector**, it has both a strength and a direction in
3D space. We break this vector down into 3 components, their strength in
particular directions: $B_x$ (pointing towards the Sun), $B_y$ (pointing
towards Mercury's dusk), and $B_z$ (points along the axis Mercury spins). We
find the magntiude (total strength) of this vector in the following way: $$ |B|
= \sqrt{{B_x}^2 + {B_y}^2 + {B_z}^2} $$ For each datapoint in time (up to 20
per second for these data), MESSENGER records this magnetic field vector.

Examples of these data are shown below. The lines moving from left to right
show the components described above as they change in time. The black line is
the total field strenght, while the x, y, and z components are in <span
    style="color:#D55E00">**red**</span>, <span
    style="color:#009E73">**green**</span>, and <span
    style="color:#0072B2">**blue**</span> repsectively. Vertical dashed lines
denote the boundary crossing intervals labelled by [Philpott et al.
(2020)](https://doi.org/10.1029/2019ja027544). Both examples (a) and (b)
contain **outbound bow shock** (labelled with BS OUT) crossing intervals
meaning MESSENGER is moving away from the planet, from the magnetosheath into
the solar wind.

![Example bow shock data](/images/example_bow_shock_data.webp)

## Methods


### Modelling


### Model Application
