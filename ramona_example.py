#!/usr/bin/env python
import ramona

class RamonaExampleConsoleApp(ramona.console_app):
      pass

if __name__ == '__main__':
      app = RamonaExampleConsoleApp(configuration='./ramona_example.conf')
      app.run()
