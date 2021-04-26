import logbook

try:
    import requests
except ImportError:
    print("Could not import requests, is my_package_with_extra installed with its extra?")
