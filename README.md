# GPS Photo Metadata Extractor

A simple Python tool for Termux that extracts metadata (EXIF) from photos, especially GPS location, date, camera info and generates Google Maps link.

---

## Features

- Extracts all available EXIF metadata from photos
- Shows GPS Latitude & Longitude (if available)
- Converts DMS to Decimal coordinates
- Generates direct Google Maps link
- Displays photo taken date, camera model, etc.
- Lightweight and works perfectly in Termux

---

## Installation

### 1. Install Dependencies

Open Termux and run these commands one by one:

```bash
pkg update && pkg upgrade -y
pkg install python -y
pip install exifread
