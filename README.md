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
