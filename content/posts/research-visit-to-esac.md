+++
date = '2026-04-19T21:42:40+01:00'
draft = false
title = 'Visiting ESAC'
tags = ["science", "travel"]
+++

I'm just back from my first research visit to [ESAC](https://en.wikipedia.org/wiki/European_Space_Astronomy_Centre) in Madrid. This was the first of two visits as part of the [ESA Archival Research Visitor Programme](https://www.cosmos.esa.int/web/esdc/visitor-programme) ( see: [Awards](/awards) ).

I spent two weeks in Madrid, where I discussed my previous and ongoing research with world-leading experts on the solar wind who work with the Solar Orbiter (and other) spacecraft.

![ESAC Antenna](/images/esac-antenna.webp)


## The project

We plan to use a machine learning method to predict the solar wind at/upstream of Mercury. Many planetary science missions to date have consisted of single-spacecraft orbiters (e.g. MESSENGER at Mercury, MAVEN at Mars, Juno at Jupiter). This has the distinct disadvantage that, while their instruments could always be switched on, what is being observed will change over the course of an orbit. The spacecraft may begin by measuring the solar wind, but as it moves in its orbit, it may pass within the bow shock (a shock wave upstream of planets, formed as the solar wind is forced to slow down rapidly). When it does so, we no longer measure the pristine solar wind, and instead (typically) measure the magnetosheath, or magnetosphere instead (see [here (WIP)](/posts/messenger-crossing-detection) for more detail on this).

This makes it very difficult to connect observations internal to the bow shock to external drivers (and vise versa). For single case-studies it may be possible to infer properties of the solar wind, however for large scale statistical studies, we have no quantified estimate (with uncertainties) of the properties of the solar wind at Mercury.

Our aim is to create a machine learning model to estimate the solar wind upstream of Mercury for the duration of the MESSENGER mission. It is difficult to quantify the performance of a gap filling model on MESSENGER data itself, as the lengths of time MESSENGER spends in the solar wind are comparable to those within the bow shock. Instead, we aim to utilise other spacecraft in the heliosphere which have measured the solar wind more continuously. We plan to use MAG data from Solar Orbiter, Parker Solar Probe, and Helios 1 and 2. When these spacecraft are 'near Mercury', we can take their (relatively) continuous data and insert artificial gaps representing what MESSENGER typically observed. By then applying our model inside those gaps, we can compare with the data (and also any other benchmark models) and quantify its performance, and only then apply the model to MESSENGER - assuming the same performance.
