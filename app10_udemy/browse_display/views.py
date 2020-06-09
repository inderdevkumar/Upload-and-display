from django.shortcuts import render
from django.http import HttpResponse
import mimetypes
import pandas as pd
import geopy  # Foe geolocation
from geopy.geocoders import ArcGIS

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
# Create your views here.

# Create your views here.
def home(request):
    #row_data= "test"
    return render(request, 'index.html')
#This function is made  to solve GeocoderTimedOut
def do_geocode(df):
    geopy = Nominatim()
    #geopy= ArcGIS()
    try:
        #nom= ArcGIS()
        df["Co-ordinates"]= df["Address"].apply(geopy.geocode)
        
        df["Latitue"]= df["Co-ordinates"].apply(lambda x: x.latitude if x != None else None)
        df["Longitude"]= df["Co-ordinates"].apply(lambda x: x.longitude if x != None else None)
        df.drop(["City", "State", "Country", "Co-ordinates"], axis = 1, inplace = True)
        #Push this data into static excel file which will be downloaded
        df.to_excel(r"F:\lecture\python\Udemy\scripts\project by instructor\app10\By me\main_folder\app10_udemy\app10_udemy\static\original.xlsx")
        return df
    except GeocoderTimedOut:
        return do_geocode(df)

def display(request):
    #content=  request.FILES.getlist('myfile')
    #content= request.GET('myfile')
    if request.method == 'POST':
        file1 = request.FILES['file']
        df= pd.read_excel(file1)
        
        # For geocoding
        # nom= ArcGIS()
        # df["Co=ordinates"]= df["Address"].apply(nom.geocode)
        # df.drop(["City", "State", "Country"], axis = 1, inplace = True)
        #df["Latitue"]= df["Co=ordinates"].apply(lambda x: x.latitude if x != None else None, timout= None)
        #df["Longitude"]= df["Co=ordinates"].apply(lambda x: x.longitude if x != None else None)

        columns_list= df.columns
        for value in columns_list:
            if (value == "Address"):
                df["Address"]= df["Address"]+" "+df["City"]+" "+ df["State"]+" "+df["Country"]
                do_geocode(df)
                dataframe_new= list(df.values.tolist())
                #print(dataframe_new)
        if "Address" not in columns_list:
            dataframe_new= "Dataframe must have Address column to be displayed"
        
        
    #contentOfFile = file1.read()
    if file1:
        #return render(request, 'display.html', {'file': file1, 'tables': table_format, 'titles':table_titles})
        return render(request, 'display.html', 
                                {'column_names':df.columns.values,
                                'row_data': dataframe_new
                                })

def download(request):
    # fill these variables with real values
    return render(request, 'display.html')
