from website import create_app, create_database

app = create_app()

#only if we run this file will this be executed not if we import
if __name__ == '__main__':  
    #automatically rerun the webserver
    app.run(debug=True) 
   
    
