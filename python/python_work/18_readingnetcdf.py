# Exercise 1. Using netCDF4 to examine contents of a file
print "Exercise 1"
from netCDF4 import Dataset
dataset = Dataset("example_data/ggas2014121200_00-18.nc") #Open file
for v in dataset.variables: #Loop listing ids
    print v,
sst = dataset.variables["SSTK"]
print sst
for d in dataset.dimensions: #Loop through dimenstions of variable
    print d, len(dataset.variables[d])
print sst.shape, sst.size
for attr in sst.ncattrs():
    print attr, "=", getattr(sst, attr)

# Exercise 2. Extract data
print "Exercise 2"
arr = sst[1, 0, 10:20, 30:35] #Take a slice
print type(arr)
dims = sst.dimensions
print dims
vars = dataset.variables #Assign dictionary
arr_time = vars["time"][1] #Extract slices from variables
arr_level = vars["surface"][0]
arr_lats = vars["latitude"][10:20]
arr_lons = vars["longitude"][30:35]
for vals in (arr_time, arr_level, arr_lats, arr_lons):
    print vals
metadata = {}
for attr in sst.ncattrs():
    metadata[attr] = getattr(sst, attr)
print metadata


    
