from website import create_app
import settings

app = create_app()
if __name__ == "__main__":
    #app.run(debug=settings.AppSettings.USE_DEBUG_MODE)
    from waitress import serve
    print("Running app on port 5000")
    serve(app, host="0.0.0.0", port=5000)
