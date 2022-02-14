<!--Copyright (C) SuperDARN Canada, University of Saskatchewan 
Author(s): Marina Schmidt, Daniel Billett
Modifications:
2020-12-01 Carley Martin added git_hdw_file
2020-01-05 Marin Schmidt switched VT hardware repo to SuperDARN hardware repo

Disclaimer:
pyDARN is under the LGPL v3 license found in the root directory LICENSE.md 
Everyone is permitted to copy and distribute verbatim copies of this license 
document, but changing it is not allowed.

This version of the GNU Lesser General Public License incorporates the terms
and conditions of version 3 of the GNU General Public License, supplemented by
the additional permissions listed below.
-->
    
# Radar Fields-of-View Coordinates and Beams

The `radar_fov` function in pyDARN is an easy way to grab the coordinates of a specific radars field-of-view. All you need is the station id (key: `stid`) of the radar of interest.

Example code:
```python
import pydarn

# Geographic coordinates for Clyde River (STID: 66) FOV
aacgm_mlt_lats, aacgm_mlt_lons=pydarn.radar_fov(66)
```

`coords` is an option to set the type of coordinate system and/or conversion one desires. Please see [Coordinates](coordinates.md) to see which coordinate system and/or conversion is available with the `Coords` object. If you don't know `pyDARN.Coords.` with autocomplete will list the options. The default is AACGM coordinates with MLT shift. 

```python
import pydarn
import datetime as dt

# AACGMv2 MLT coordinates for Dome C (STID: 96), valid for November 26th, 2005
aacgm_mlt_lats, aacgm_mlt_lons=pydarn.radar_fov(96, coords=Coords.AACGM_MLT, date=dt.datetime(2005,11,26))
```

The outputs for `radar_fov` are two numpy arrays of latitude and longitude coordinates with dimensions (number_of_beams+1 x number_of_gates+1). They correspond to the corners of each range gate.

Options and defaults of `radar_fov`:

| name        | type       | default          | definition                                                            |
| ----------- | ---------- | ---------------- | --------------------------------------------------------------------- |
| `stid`      | int        | None             | Station identifier                                                    |
| `rsep`      | int        | 45               | Range gate separation set by the control program id (km)              |
| `frang`     | int        | 180              |                                                                       |
| `ranges`    | tuple(int) | None             | default gets set to 0-45 km number of range gates                     |
| `coords`    | Coords     | Coords.AACGM_MLT | Coordinates system to return latitude and longitude                   |
| `max_beams` | int        | None             | Maximum beams to plot from 0, default is max beams from hardware file |
| `date`      | datetime   | Now()            | The time for the coordinate system shift                              | 


## Beam Scan
