import time

import requests
import datetime
import smtplib
import time

EMAIL = "example@mail.com"
PASSWORD = "yourpassword"

MY_LATITUDE = 20.675608
MY_LONGITUDE = -103.274428


while True:
    time.sleep(60)
    # =====================================================================================================================
    #                                     GET THE CURRENT HOUR AND MINUTE
    # =====================================================================================================================
    now = datetime.datetime.now()
    now_time = str(now).split(" ")[1].split(".")[0].split(":")
    now_hour = int(now_time[0])
    now_minute = int(now_time[1])

    # =====================================================================================================================
    #                               GET THE CURRENT LONGITUDE AND LATITUDE OF ISS
    # =====================================================================================================================
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_current = iss_response.json()["iss_position"]
    iss_latitude = float(iss_current["latitude"])
    iss_longitude = float(iss_current["longitude"])
    print(iss_current)


    # =====================================================================================================================
    #                               OBTAIN THE SUNRISE AND SUNSET HOURS AND MINUTES
    # =====================================================================================================================
    sunset_rise_response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LATITUDE}"
                                       f"&lng={MY_LONGITUDE}"
                                       f"&formatted=0")
    sunset_rise_response.raise_for_status()

    sunset_time_utc = sunset_rise_response.json()["results"]["sunset"].split("T")[1].split("+")[0]
    sunset_time = sunset_time_utc.replace(sunset_time_utc[0:2], str((int(sunset_time_utc[0:2]) - 5) % 24)).split(":")
    sunset_hour = int(sunset_time[0])
    sunset_minute = int(sunset_time[1])

    sunrise_time_utc = sunset_rise_response.json()["results"]["sunrise"].split("T")[1].split("+")[0]
    sunrise_time = sunrise_time_utc.replace(sunrise_time_utc[0:2], str((int(sunrise_time_utc[0:2]) - 5) % 24)).split(":")
    sunrise_hour = int(sunrise_time[0])
    sunrise_minute = int(sunrise_time[1])


    # =====================================================================================================================
    #                                       SEND AN EMAIL IF THE ISS IS NEAR
    # =====================================================================================================================

    if (MY_LONGITUDE - 2) < iss_longitude < (MY_LONGITUDE + 2) \
            and (MY_LATITUDE - 2) < iss_latitude < (MY_LATITUDE + 2):
        if (sunset_hour < now_hour < sunrise_hour) \
                or (now_hour == sunset_hour and now_minute >= sunset_minute) \
                or (now_hour == sunrise_hour and now_minute <= sunrise_minute):
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=EMAIL,
                                    msg="Subject:Look at the sky\n\nThe ISS is near you. You could see it.")




