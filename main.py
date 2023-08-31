from website import create_app

app = create_app()

if __name__ == '__main__': #the app is only created if the main.py file is being
                           #being run.
    app.run(debug=True)    #Kept on during development so that each time we make
                           #a change in our code, the website will automatically 
                           #rerun. Turn off when not developing.

