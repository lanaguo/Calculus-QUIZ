from website import create_app  # imported from __init__
import os

app = create_app()


if __name__ == '__main__': # run webserver only if main file is run
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port) # runs flask application
# debug = true for development only so server reruns every time change is made
