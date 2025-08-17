# wardrive-map-generator
Generate HTML Map from Wardrive/Wigle WiFi log files

<table>
  <td width="50%" valign="top">
    <img src="https://raw.githubusercontent.com/sorinbotirla/wardrive-map-generator/refs/heads/main/images/screenshot.jpg" width="100%" />
    Markers showing a wardrive from the log file I included in this repo.
  </td>
  <td width="50%" valign="top">
    <img src="https://raw.githubusercontent.com/sorinbotirla/wardrive-map-generator/refs/heads/main/images/screenshot2.jpg" width="100%" />
    Open WiFi networks are shown as green markers
  </td>
</table>

---
## Install

```bash
git clone https://github.com/sorinbotirla/wardrive-map-generator.git
cd ./wardrive-map-generator/
```

Add your wardrive .log files next to the script. When you run the script, it will parse all the log files and generate a html map which you can open in the browser. Open networks will be shown as green markers. 

---

## Dependencies
python3, ipython3, pandas, folium

```bash
pip install ipython3 pandas folium --break-system-packages
```

---

## How to run

```bash
ipython wardrive-map-generator.py
```

Then open mapdata.html in your browser and check the markers.

## How to get wardrive log files

You can use the <a href="https://wigle.net/" target="_blank">Wigle.net</a> app or buy an ESP32 Marauder from <a href="https://justcallmekokollc.com/" target="_blank">https://justcallmekokollc.com/</a> or <a href="https://awokdynamics.com/" target="_blank">https://awokdynamics.com/</a>
<img src="https://raw.githubusercontent.com/sorinbotirla/wardrive-map-generator/refs/heads/main/images/wardrivers.jpg" width="100%" />

To build an ESP32 Marauder you can follow my guide <a href="https://github.com/sorinbotirla/Dual-ESP32-CAM-Marauder" target="_blank">here</a> and <a href="https://github.com/sorinbotirla/esp32-marauder-ESP32-3248S035C" target="_blank">here</a>

## Ok, but what's Wardriving?

According to <a href="https://en.wikipedia.org/wiki/Wardriving" target="_blank">Wikipedia</a>, wardriving is 
```bash
Wardriving is the act of searching for Wi-Fi wireless networks as well as cell towers, usually from a moving vehicle, using a laptop or smartphone. Software for wardriving is freely available on the internet.
```

You can scan all the WiFi networks around you using a software/app/device that has GPS and WiFi capabilities. The point is to collect all the wireless network locations, store them in log files, and upload the logs on the international wireless database found on <a href="https://wigle.net/" target="_blank">https://wigle.net/</a>, where you can contribute and search for the location of various wireless stations/access points around the world.

## Is Wardriving legal?

Yes. You do not hack the wireless networks, neither connect to them. Wardriving is just creating a world map of wifi networks.


