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

You can use the <a href="https://wigle.net/">Wigle.net</a> app or buy an ESP32 Marauder from <a href="https://justcallmekokollc.com/">https://justcallmekokollc.com/</a> or <a href="https://awokdynamics.com/">https://awokdynamics.com/</a>
<img src="https://raw.githubusercontent.com/sorinbotirla/wardrive-map-generator/refs/heads/main/images/wardrivers.jpg" width="100%" />

To build an ESP32 Marauder you can follow my guide <a href="https://github.com/sorinbotirla/Dual-ESP32-CAM-Marauder">here</a> and <a href="https://github.com/sorinbotirla/esp32-marauder-ESP32-3248S035C">here</a>


