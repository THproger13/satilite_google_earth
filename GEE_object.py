import ee

# Authenticate only if OAuth2 authentication is required.
try:
    ee.Initialize(project='evocative-reef-400606')
except ee.EEException:
    ee.Authenticate()
    ee.Initialize(project='evocative-reef-400606')

# Set up the Area of Interest (aoi) with specific longitude and latitude.
aoi = ee.Geometry.Point([126.97782163, 27.29989221])  # Replace with your longitude and latitude.

# Create an ImageCollection for Landsat 8 images and filter by date and area.
dataset = (ee.ImageCollection('LANDSAT/LC08/C01/T1')
           .filterDate('2023-01-01', '2023-12-31')
           .filterBounds(aoi))

# Define the thresholds.
ndviThreshold = 0.2
waterThreshold = 0.1

# Define the function to identify objects.
def identify_objects(image):
    ndvi = image.normalizedDifference(['B5', 'B4'])
    ndwi = image.normalizedDifference(['B3', 'B5'])
    objects = image.updateMask(ndvi.gt(ndviThreshold).And(ndwi.lt(waterThreshold)))
    return objects

# Map the function over the ImageCollection and get object statistics.
identified_objects = dataset.map(identify_objects)
object_statistics = identified_objects.reduce(ee.Reducer.sum())

# Print the results.
print('Object Statistics:', object_statistics.getInfo())
