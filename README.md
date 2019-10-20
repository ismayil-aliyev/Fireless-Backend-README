About the Fireless Android app
------------
Fireless Android app is a service which serves for fetching data from user submissions and NASA's open-source Active Fire Data, where users in Android clients receive fire accident information based on their GPS location.
This service has been developed as a part of NASA’s International Space Apps Challenge 2019 project, by team BHOSMOS, based in Baku, Azerbaijan.

Fireless Backend 
------------
Fireless Backend is built on Python's Django Framework (Py3, Django v.2.2). 


API Access
------------
Fireless Backend offers open POST access to its service through the following URL:

https://nasa-ada.herokuapp.com/spotfire/home

| Key    | Description              |
|--------|--------------------------|
| radius | Distance from user in km |
| ltd    | Latitude of user         |
| lng    | Latitude of user         |

Machine Learning model (Support-Vector Machines) for image recognition
------------
Fireless Android clients' image upload submissions are fed to a machine learning algorithm in order to avoid false reports.
Trained ML model is also publicly available in this repository, alongside with the associated Python script.



