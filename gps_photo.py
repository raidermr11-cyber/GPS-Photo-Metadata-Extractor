import exifread
import os

def dms_to_decimal(dms, ref):
    """Convert DMS to Decimal degrees"""
    degrees = float(dms[0])
    minutes = float(dms[1])
    seconds = float(dms[2])
    decimal = degrees + minutes/60 + seconds/3600
    if ref in ['S', 'W']:
        decimal = -decimal
    return round(decimal, 6)

print("🔹 GPS Photo Metadata Extractor 🔹\n")

# Ask for photo path
image_path = input("Enter full photo path: ").strip()

if not os.path.exists(image_path):
    print("❌ File not found!")
    exit()

print("\nReading photo metadata...\n")

with open(image_path, 'rb') as f:
    tags = exifread.process_file(f, details=False)

gps_found = False
lat = lon = None
lat_ref = lon_ref = None

print("="*50)
print("📸 PHOTO INFORMATION")
print("="*50)

for tag in sorted(tags.keys()):
    if any(x in tag for x in ["Date", "Make", "Model", "Software", "GPS", "Image Width", "Image Length"]):
        value = tags[tag]
        print(f"{tag:35}: {value}")

    # Extract GPS data
    if tag == 'GPS GPSLatitude':
        lat = tags[tag].values
        lat_ref = str(tags.get('GPS GPSLatitudeRef', 'N')).strip()
        gps_found = True
    if tag == 'GPS GPSLongitude':
        lon = tags[tag].values
        lon_ref = str(tags.get('GPS GPSLongitudeRef', 'E')).strip()
    if tag == 'GPS GPSAltitude':
        print(f"GPS Altitude                     : {tags[tag]}")

if gps_found and lat and lon:
    latitude = dms_to_decimal(lat, lat_ref)
    longitude = dms_to_decimal(lon, lon_ref)
    
    print("\n" + "="*50)
    print("📍 GPS LOCATION INFORMATION")
    print("="*50)
    print(f"Latitude          : {latitude}° {lat_ref}")
    print(f"Longitude         : {longitude}° {lon_ref}")
    
    maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
    print(f"\n🗺️ Google Maps Link:")
    print(maps_link)
    
    # Optional: Open link automatically in browser
    # os.system(f"termux-open-url '{maps_link}'")
    
else:
    print("\n⚠️ No GPS data found in this photo.")

print("\n✅ Done!")
