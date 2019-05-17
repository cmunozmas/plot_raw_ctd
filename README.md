# plot_raw_ctd
The plot_socib_rv_adcp is a set of python scripts and functions developed at SOCIB to plot the data collected by a SBE911+ CTD mounted onboard the SOCIB Research Vessel. They are able to plot the main variables stored into the cnv files and plot them interpolate the profiles over the longitude dimension.

## Prerequisites:

    See requirements file for external libraries needed.
   
## The following features are already implemented in the toolbox:

    One main script to perform data processing:
        main.py
    Seven processing functions to perform:
        DataOps.py: reading, loading and organizing files.
        globfile.py: set  path variable as glogal.
        Plot.py: plot profiles and TS diagrams.
        PlotSettings.py: variables and station codes naming.
        ProfileSettings.py: Identifies variables with their location in the input files columns.
        SetPaths.py: set input and output paths and get file information (deployment, instrument, station, etc)
        

## The following features are planned or in development:

    Load stations from a gpx file

## Copyright

Copyright (C) 2013-2018 ICTS SOCIB - Servei d'observació i predicció costaner de les Illes Balears http://www.socib.es

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
