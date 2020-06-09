import pandas as pd

df= pd.read_excel("test.xlsx")
##print(df)
columns_list= df.columns
for value in columns_list:
    if (value == "Address"):
        print(df)
if "Address" not in columns_list:
    print("Dataframe must have colimn to be displayed")            














def display(request):
    #content=  request.FILES.getlist('myfile')
    #content= request.GET('myfile')
    if request.method == 'POST':
        file1 = request.FILES['file']
        df= pd.read_excel(file1)
        
        table_format= [df.to_html(classes='data')]
        table_titles= df.columns.values
        columns_list= df.columns
        for value in columns_list:
            if (value == "Address"):
                print(df)
        if "Address" not in columns_list:
            print("Dataframe must have colimn to be displayed")
    #contentOfFile = file1.read()
    if file1:
        #return render(request, 'display.html', {'file': file1, 'tables': table_format, 'titles':table_titles})
        return render(request, 'index.html', {'column_names':df.columns.values, 'row_data':list(df.values.tolist())
                           })
