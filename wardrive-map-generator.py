#!/usr/bin/env python
# coding: utf-8

# dependencies
# pip install ipython3 pandas folium --break-system-packages

# Use this script to generate a HTML Map of the scanned WiFi AP/Stations from Wardriving log files.

# Place your wardrive .log files next to this script and run it with:
# ipython wardrive-map-generator.py

# import required libraries
import pandas as pd    # Read CSV data from Wigle/Wardriving Wifi log files
import folium          # Mapping Library
import glob, os, sys   # search for the log files


valid = []

for root, dirs, files in os.walk("./"):
    for file in files:
        if file.endswith(".log"):
            df = pd.read_csv(file, delimiter = ',', encoding='latin-1', header=1)
            for newRow in df[['MAC', 'SSID', 'AuthMode', 'FirstSeen', 'Channel', 'RSSI', 'CurrentLatitude', 'CurrentLongitude', 'AltitudeMeters', 'AccuracyMeters', 'Type']].values:
                if (newRow[10] == 'WIFI'):
                    rowExists = False
                    for existingRow in valid:
                        if newRow[0] == existingRow[0]:
                            rowExists = True
                            
                    if rowExists == False:
                        valid.append(newRow)                
                        # df.sample(5)


# Clean Set by dropping all NA values
validframes = pd.DataFrame(valid).dropna()
validframes.head()


# Label Columns
validframes.columns = ['MAC', 'SSID', 'AuthMode', 'FirstSeen', 'Channel', 'RSSI', 'CurrentLatitude', 'CurrentLongitude', 'AltitudeMeters', 'AccuracyMeters', 'Type']


# Compute Average of all the latitudes and longitudes in our dataset to find center and set zoom
# You can also hardcode center adddress like
# mymap = folium.Map( location=[34.0522, -118.243683], zoom_start=12)
mymap = folium.Map( location=[ validframes.CurrentLatitude.mean(), validframes.CurrentLongitude.mean() ], zoom_start=10)


# Filter Out Wifi Data
for coord in validframes[['CurrentLatitude','CurrentLongitude', 'SSID', 'Type', 'MAC', 'AuthMode']].values:
    if ("?" not in str(coord[0])) and ("?" not in str(coord[1])):
        # Set location using Lat-Long(cord[0]-cord[1])
        # Set radius and color of marker 
        # Set data to show on popup
        if ("OPEN" in str(coord[5])):
            iconColor = "green"
        else:
            iconColor = "red"

        folium.Marker(location=[coord[0],coord[1]],tooltip=["SSID:", coord[2].translate(str.maketrans({"-":  r"\-",
                                        "]":  r"\]",
                                        "\\": r"\\",
                                        "`":  r"\'",
                                        "^":  r"\^",
                                        "$":  r"\$",
                                        "*":  r"\*",
                                        ".":  r"\."}))], 
                                        popup=["SSID:", coord[2].translate(str.maketrans({"-":  r"\-",
                                        "]":  r"\]",
                                        "\\": r"\\",
                                        "`":  r"\'",
                                        "^":  r"\^",
                                        "$":  r"\$",
                                        "*":  r"\*",
                                        ".":  r"\."})),
                                        "BSSID:", coord[4],
                                        "SECURITY:", coord[5]
                                        ]
                                        ,icon=folium.Icon(color=iconColor,prefix='fa',icon='wifi')
                                        ).add_to(mymap)


# Save MapData To HTML File:
mymap.save('mapdata.html')


get_ipython().run_cell_magic('HTML', '', '<iframe width="100%" height="650" src="mapdata.html"></iframe>')

