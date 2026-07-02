---
title: "Stream Mode: Concise vs Full"
source: https://docs.perplexity.ai/docs/sonar/pro-search/stream-mode
path: docs/sonar/pro-search/stream-mode
---

Learn how to use stream_mode to control streaming response formats and optimize your integration

## Overview

The `stream_mode` parameter gives you control over how streaming responses are formatted. Choose between two modes:

* **`full`** (default) - Traditional streaming format with complete message objects in each chunk
* **`concise`** - Optimized streaming format with reduced redundancy and enhanced reasoning visibility

<Info>
  The `concise` mode is designed to minimize bandwidth usage and provide better visibility into the model's reasoning process.
</Info>

## Quick Comparison

| Feature                 | Full Mode                                | Concise Mode                        |
| ----------------------- | ---------------------------------------- | ----------------------------------- |
| **Message aggregation** | Server-side (includes `choices.message`) | Client-side (delta only)            |
| **Chunk types**         | Single type (`chat.completion.chunk`)    | Multiple types for different stages |
| **Search results**      | Multiple times during stream             | Only in `done` chunks               |
| **Bandwidth**           | Higher (includes redundant data)         | Lower (optimized for efficiency)    |

## Using Concise Mode

Set `stream_mode: "concise"` when creating streaming completions:

<Tabs>
  <Tab title="Python SDK">
    ```python theme={null}
    from perplexity import Perplexity

    client = Perplexity()

    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "Current weather and 7-day forecast for Seattle, Washington"}],
        stream=True,
        stream_mode="concise"
    )

    for chunk in stream:
        print(f"Chunk type: {chunk.object}")
        if chunk.choices and chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
    ```
  </Tab>

  <Tab title="Typescript SDK">
    ```typescript theme={null}
    import Perplexity from '@perplexity-ai/perplexity_ai';

    const client = new Perplexity();

    const stream = await client.chat.completions.create({
      model: "sonar-pro",
      messages: [{ role: "user", content: "Current weather and 7-day forecast for Seattle, Washington" }],
      stream: true,
      stream_mode: "concise"
    });

    for await (const chunk of stream) {
      console.log(`Chunk type: ${chunk.object}`);
      if (chunk.choices[0]?.delta?.content) {
        process.stdout.write((chunk.choices[0]?.delta?.content ?? '') as string);
      }
    }
    ```
  </Tab>

  <Tab title="cURL">
    ```bash theme={null}
    curl -X POST "https://api.perplexity.ai/v1/sonar" \
      -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "model": "sonar-pro",
        "messages": [{"role": "user", "content": "What is the weather in Seattle?"}],
        "stream": true,
        "stream_mode": "concise"
      }'
    ```
  </Tab>
</Tabs>

<AccordionGroup>
  <Accordion title="Response — Current weather and 7-day forecast for Seattle, Washington">
    ```json theme={null}
    {
      "id": "300fab98-92a3-4a69-9e84-fe05c918f831",
      "results": [
        {
          "snippet": "**Current conditions at**\n## Boeing Field - King County International Airport (KBFI)\n**Lat: ** 47.54548°N**Lon: ** 122.3147°W**Elev: ** 20.0ft.\nMostly Cloudy\n61°F\n16°C\n|**Humidity**|63%|\n|--|--|\n|**Wind Speed**|N 0 MPH|\n|**Barometer**|29.95 in (1014.22 mb)|\n|**Dewpoint**|48°F (9°C)|\n|**Visibility**|10.00 mi|\n|**Last update**|26 May 03:00 PM PDT|\n...\n**Extended Forecast for**\n## Seattle WA\n- Tonight\nLow: 50 °F\nMostly Clear\n- Wednesday\nHigh: 71 °F\nSunny\n- Wednesday Night\nLow: 54 °F\nMostly Clear\n- Thursday\nHigh: 77 °F\nSunny\n- Thursday Night\nLow: 53 °F\nChance Rain\n- Friday\nHigh: 60 °F\nChance Rain\n- Friday Night\nLow: 49 °F\nMostly Cloudy\n- Saturday\nHigh: 62 °F\nPartly Sunny\n- Saturday Night\nLow: 48 °F\nPartly Cloudy\n## Detailed Forecast\n**Tonight**\nMostly clear, with a low around 50.\nNorth wind 5 to 8 mph becoming calm in the evening.\n**Wednesday**\nSunny, with a high near 71.\nLight and variable wind becoming north 5 to 10 mph in the morning.\n**Wednesday Night**\nMostly clear, with a low around 54.\nNorth wind 5 to 8 mph becoming calm in the evening.\n**Thursday**\nSunny, with a high near 77.\nCalm wind becoming north northwest around 5 mph in the afternoon.\n**Thursday Night**\nA 30 percent chance of rain, mainly after 11pm.\nMostly cloudy, with a low around 53.\nNorth northwest wind 5 to 9 mph becoming south after midnight.\n**Friday**\nA 50 percent chance of rain.\nMostly cloudy, with a high near 60.\n**Friday Night**\nMostly cloudy, with a low around 49.\n**Saturday**\nPartly sunny, with a high near 62.\n**Saturday Night**\nPartly cloudy, with a low around 48.\n**Sunday**\nMostly sunny, with a high near 64.\n**Sunday Night**\nMostly clear, with a low around 49.\n**Monday**\nSunny, with a high near 70.\n**Monday Night**\nPartly cloudy, with a low around 53.\n**Tuesday**\nMostly sunny, with a high near 78.\n...\nSeattle WA\n47.62°N 122.36°W (Elev. 105 ft)\nLast Update:\n11:26 am PDT May 26, 2026\nForecast Valid:\n3pm PDT May 26, 2026-6pm PDT Jun 2, 2026",
          "title": "7-Day Forecast 47.62N 122.36W",
          "url": "https://forecast.weather.gov/MapClick.php?lat=47.6218&lon=-122.3503",
          "date": "2026-05-26",
          "last_updated": "2026-05-26"
        },
        {
          "snippet": "Seattle, WA Weather Forecast | AccuWeather\n## Today's Weather\nTue, May 26\nMainly cloudy; brief morning showers followed by a shower in spots this afternoon\n**Hi: 62°**\nTonight: Partly cloudy\n**Lo: 51°**\n## Current Weather\n2:32 PM\n57°F\nRealFeel®\n60°\nCloudy More Details\nRealFeel Shade™ 56°\nWind NW 2 mph\nWind Gusts 5 mph\nAir Quality Fair\n## Looking Ahead\nWarming up, then noticeably cooler weather again Friday\n## Hourly Weather\n3 PM 59°\n40%\n4 PM 61°\n37%\n5 PM 62°\n32%\n6 PM 62°\n32%\n7 PM 61°\n21%\n8 PM 60°\n0%\n9 PM 59°\n0%\n10 PM 57°\n0%\n11 PM 56°\n0%\n12 AM 54°\n0%\n1 AM 53°\n0%\n2 AM 53°\n0%\n## 10-Day Weather Forecast\nToday\n5/26\n62° 51°\nA few showers this morning\nNight: Partly cloudy\n80%\nWed\n5/27\n73° 55°\nPartly sunny and pleasant\nPartly cloudy\n0%\nThu\n5/28\n77° 53°\nMostly sunny and pleasant\nPartly cloudy\n12%\nFri\n5/29\n59° 47°\nCooler\nLow clouds\n25%\nSat\n5/30\n62° 47°\nMostly cloudy\nMostly cloudy\n25%\nSun\n5/31\n70° 50°\nPleasant with clouds and sun\nMainly clear\n19%\nMon\n6/1\n76° 57°\nMostly sunny and pleasant\nMainly clear\n13%\nTue\n6/2\n93° 58°\nHot with high clouds\nCloudy\n2%\nWed\n6/3\n76° 55°\nMostly cloudy\nMostly cloudy\n6%\nThu\n6/4\n73° 53°\nSunshine and a few clouds\nMainly clear\n1%\n...\nAir Quality Fair\nThe air quality is generally acceptable for most individuals.\nHowever, sensitive groups may experience minor to moderate symptoms from long-term exposure.",
          "title": "Seattle, WA Weather Forecast",
          "url": "https://www.accuweather.com/en/us/seattle/98104/weather-forecast/351409",
          "date": null,
          "last_updated": "2026-05-26"
        },
        {
          "snippet": "Additional Conditions\nPressure\n29.93 °in\nVisibility\n10 °miles\nClouds\nPartly Cloudy\nDew Point\n47 °F\nHumidity\n60 °%\nRainfall\n0 °in\nSnow Depth\n0 °in\nTop Video Stories\n...\n5:20 AM\n8:55 PM",
          "title": "Seattle, WA 10-Day Weather Forecast",
          "url": "https://www.wunderground.com/forecast/us/wa/seattle",
          "date": "2026-05-26",
          "last_updated": "2026-05-27"
        },
        {
          "snippet": "**Current conditions at**\n## Boeing Field - King County International Airport (KBFI)\n**Lat: ** 47.54548°N**Lon: ** 122.3147°W**Elev: ** 20.0ft.\nMostly Cloudy\n52°F\n11°C\n|**Humidity**|66%|\n|--|--|\n|**Wind Speed**|WSW 6 MPH|\n|**Barometer**|30.15 in (1021.0 mb)|\n|**Dewpoint**|41°F (5°C)|\n|**Visibility**|10.00 mi|\n|**Last update**|16 May 06:20 PM PDT|\n...\n**Extended Forecast for**\n## Downtown Seattle WA\n- Tonight\nLow: 43 °F\nChance Rain\nthen Partly\nCloudy\n- Sunday\nHigh: 62 °F\nMostly Sunny\n- Sunday Night\nLow: 48 °F\nIncreasing\nClouds\n- Monday\nHigh: 66 °F\nDecreasing\nClouds\n- Monday Night\nLow: 50 °F\nPartly Cloudy\n- Tuesday\nHigh: 65 °F\nPartly Sunny\n- Tuesday Night\nLow: 50 °F\nMostly Cloudy\n- Wednesday\nHigh: 68 °F\nMostly Sunny\n- Wednesday Night\nLow: 51 °F\nPartly Cloudy\n## Detailed Forecast\n**Tonight**\nA 50 percent chance of rain, mainly before 8pm.\nMostly cloudy, with a low around 43.\nWest wind around 5 mph becoming calm in the evening.\n**Sunday**\nMostly sunny, with a high near 62.\nLight and variable wind.\n**Sunday Night**\nIncreasing clouds, with a low around 48.\nCalm wind.\n**Monday**\nCloudy, then gradually becoming mostly sunny, with a high near 66.\nLight and variable wind.\n**Monday Night**\nPartly cloudy, with a low around 50.\nNorth wind around 6 mph becoming calm in the evening.\n**Tuesday**\nPartly sunny, with a high near 65.\n**Tuesday Night**\nMostly cloudy, with a low around 50.\n**Wednesday**\nMostly sunny, with a high near 68.\n**Wednesday Night**\nPartly cloudy, with a low around 51.\n**Thursday**\nMostly sunny, with a high near 69.\n**Thursday Night**\nPartly cloudy, with a low around 52.\n**Friday**\nMostly sunny, with a high near 69.\n**Friday Night**\nMostly clear, with a low around 52.\n**Saturday**\nMostly sunny, with a high near 73.\n...\nDowntown Seattle WA\n47.61°N 122.32°W (Elev. 240 ft)\nLast Update:\n11:27 am PDT May 16, 2026\nForecast Valid:\n6pm PDT May 16, 2026-6pm PDT May 23, 2026\nForecast Discussion",
          "title": "7-Day Forecast 47.61N 122.32W - National Weather Service",
          "url": "https://forecast.weather.gov/MapClick.php?lat=47.6032&lon=-122.3303",
          "date": "2026-05-17",
          "last_updated": "2026-05-17"
        },
        {
          "snippet": "**Current conditions at**\n## SEATTLE WEATHER FORECAST OFFICE (SEAW1)\n**Lat: ** 47.68528°N**Lon: ** 122.25111°W**Elev: ** 29.0ft.\nNA\n45°F\n7°C\n|**Humidity**|75%|\n|--|--|\n|**Wind Speed**|SSW 5 MPH|\n|**Barometer**|30.45 in (1031.16 mb)|\n|**Dewpoint**|37°F (3°C)|\n|**Visibility**|NA|\n|**Wind Chill**|42°F (6°C)|\n|**Last update**|26 Mar 09:30 AM PDT|\n...\n**Extended Forecast for**\n## 2 Miles SSE Seattle-University WA\n- Today\nHigh: 53 °F\nSunny\n- Tonight\nLow: 35 °F\nIncreasing\nClouds\n- Friday\nHigh: 56 °F\nMostly Sunny\n- Friday Night\nLow: 38 °F\nMostly Cloudy\n- Saturday\nHigh: 54 °F\nPartly Sunny\n- Saturday Night\nLow: 39 °F\nMostly Cloudy\n- Sunday\nHigh: 54 °F\nSlight Chance\nRain\n- Sunday Night\nLow: 39 °F\nChance Rain\n- Monday\nHigh: 51 °F\nChance Rain\n## Detailed Forecast\n**Today**\nSunny, with a high near 53.\nSouth wind around 6 mph.\n**Tonight**\nIncreasing clouds, with a low around 35.\nCalm wind.\n**Friday**\nMostly sunny, with a high near 56.\nCalm wind becoming north 5 to 7 mph in the afternoon.\n**Friday Night**\nMostly cloudy, with a low around 38.\nNorth wind 5 to 8 mph becoming calm in the evening.\n**Saturday**\nPartly sunny, with a high near 54.\nCalm wind becoming north northwest around 5 mph in the afternoon.\n**Saturday Night**\nMostly cloudy, with a low around 39.\n**Sunday**\nA 20 percent chance of rain after 11am.\nMostly cloudy, with a high near 54.\n**Sunday Night**\nA chance of rain.\nMostly cloudy, with a low around 39.\n**Monday**\nA chance of rain.\nMostly cloudy, with a high near 51.\n**Monday Night**\nA chance of rain, mainly before 11pm.\nPartly cloudy, with a low around 36.\n**Tuesday**\nA slight chance of rain.\nMostly sunny, with a high near 53.\n**Tuesday Night**\nA chance of rain.\nMostly cloudy, with a low around 40.\n**Wednesday**\nA chance of rain.\nMostly cloudy, with a high near 53.\n...\n2 Miles SSE Seattle-University WA\n47.63°N 122.3°W (Elev. 190 ft)\nLast Update:\n11:27 pm PDT Mar 25, 2026\nForecast Valid:\n10am PDT Mar 26, 2026-6pm PDT Apr 1, 2026\nForecast Discussion",
          "title": "7-Day Forecast 47.63N 122.3W - National Weather Service",
          "url": "https://forecast.weather.gov/MapClick.php?lat=47.6329523&lon=-122.28918880000003&site=all&smap=1&searchresult=Seattle%2C+WA+98112%2C+USA",
          "date": "2026-03-26",
          "last_updated": "2026-03-26"
        },
        {
          "snippet": "Elevated to Critical fire weather conditions due to gusty winds and low humidity are expected through Tuesday across Oregon and Nevada.\nShowers and thunderstorms will develop over the Northwest.\n...\n**Current conditions at**\n## SEATTLE WEATHER FORECAST OFFICE (SEAW1)\n**Lat: ** 47.68528°N**Lon: ** 122.25111°W**Elev: ** 29.0ft.\nNA\n53°F\n12°C\n|**Humidity**|86%|\n|--|--|\n|**Wind Speed**|ESE 5 MPH|\n|**Barometer**|29.71 in (1006.1 mb)|\n|**Dewpoint**|49°F (9°C)|\n|**Visibility**|NA|\n|**Last update**|25 May 10:30 PM PDT|\n...\n**Extended Forecast for**\n## Seattle-University WA\n- Tonight\nLow: 48 °F\nSlight Chance\nRain\n- Tuesday\nHigh: 65 °F\nChance Rain\nthen Partly\nSunny\n- Tuesday Night\nLow: 49 °F\nPartly Cloudy\n- Wednesday\nHigh: 74 °F\nSunny\n- Wednesday Night\nLow: 53 °F\nMostly Clear\n- Thursday\nHigh: 78 °F\nSunny\n- Thursday Night\nLow: 53 °F\nPartly Cloudy\n- Friday\nHigh: 64 °F\nChance Rain\n- Friday Night\nLow: 48 °F\nChance Rain\nthen Mostly\nCloudy\n## Detailed Forecast\n**Tonight**\nA 10 percent chance of rain after 5am.\nPartly cloudy, with a low around 48.\nSouth wind around 6 mph becoming calm after midnight.\n**Tuesday**\nA 30 percent chance of rain, mainly before 9am.\nPartly sunny, with a high near 65.\nCalm wind becoming north northwest 5 to 7 mph in the afternoon.\n**Tuesday Night**\nPartly cloudy, with a low around 49.\nNorth wind around 6 mph becoming calm in the evening.\n**Wednesday**\nSunny, with a high near 74.\nCalm wind becoming north 5 to 8 mph in the afternoon.\n**Wednesday Night**\nMostly clear, with a low around 53.\nNorth wind 5 to 7 mph becoming calm in the evening.\n**Thursday**\nSunny, with a high near 78.\n**Thursday Night**\nPartly cloudy, with a low around 53.\n**Friday**\nA chance of rain.\nMostly cloudy, with a high near 64.\n**Friday Night**\nA chance of rain before 11pm.\nMostly cloudy, with a low around 48.\n**Saturday**\nPartly sunny, with a high near 65.\n**Saturday Night**\nPartly cloudy, with a low around 47.\n**Sunday**\nMostly sunny, with a high near 66.\n**Sunday Night**\nPartly cloudy, with a low around 48.\n**Monday**\nMostly sunny, with a high near 72.\n...\nSeattle-University WA\n47.65°N 122.3°W (Elev. 33 ft)\nLast Update:\n1:00 pm PDT May 25, 2026\nForecast Valid:\n11pm PDT May 25, 2026-6pm PDT Jun 1, 2026\nForecast Discussion",
          "title": "7-Day Forecast 47.65N 122.3W - National Weather Service",
          "url": "https://forecast.weather.gov/MapClick.php?CityName=Seattle&state=WA&site=SEW&lat=47.6606&lon=-122.292",
          "date": "2026-05-26",
          "last_updated": "2026-05-26"
        }
      ],
      "server_time": null
    }
    ```
  </Accordion>

  <Accordion title="Response — What is the weather in Seattle?">
    ```json theme={null}
    {
      "id": "3b076c08-870a-45e5-881d-ddaf39781638",
      "results": [
        {
          "snippet": "Seattle, WA Weather Forecast | AccuWeather\n## Today's Weather\nWed, May 20\nClouds breaking for some sun\n**Hi: 68°**\nTonight: Mainly clear\n**Lo: 51°**\n## Current Weather\n1:47 PM\n64°F\nRealFeel®\n77°\nMostly cloudy More Details\nRealFeel Shade™ 65°\nWind NNW 3 mph\nWind Gusts 6 mph\nAir Quality Fair\n## Looking Ahead\n...\n68° 51°\nClouds breaking for some sun\nNight: Mainly clear",
          "title": "Seattle, WA Weather Forecast - AccuWeather",
          "url": "https://www.accuweather.com/en/us/seattle/98104/weather-forecast/351409",
          "date": null,
          "last_updated": "2026-05-20"
        },
        {
          "snippet": "**Current conditions at**\n## Boeing Field - King County International Airport (KBFI)\n**Lat: ** 47.54548°N**Lon: ** 122.3147°W**Elev: ** 20.0ft.\nClear\n64°F\n18°C\n|**Humidity**|52%|\n|--|--|\n|**Wind Speed**|WNW 10 MPH|\n|**Barometer**|30.19 in (1022.35 mb)|\n|**Dewpoint**|46°F (8°C)|\n|**Visibility**|10.00 mi|\n|**Last update**|20 May 02:30 PM PDT|\n...\n## Seattle WA\n- This Afternoon\nHigh: 67 °F\nMostly Sunny\n- Tonight\nLow: 51 °F\nDecreasing\nClouds\n- Thursday\n...\n**This Afternoon**\nMostly sunny, with a high near 67.\nNorth northwest wind around 8 mph.\n**Tonight**\nMostly cloudy, then gradually becoming clear, with a low around 51.\nNorth wind 5 to 7 mph becoming calm after midnight.\n...\n2pm PDT May 20, 2026-6pm PDT May 26, 2026",
          "title": "7-Day Forecast 47.62N 122.36W - National Weather Service",
          "url": "https://forecast.weather.gov/MapClick.php?lat=47.6218&lon=-122.3503",
          "date": "2026-05-20",
          "last_updated": "2026-05-20"
        },
        {
          "snippet": "*access_time* ** 10:20 PM PDT on May 20, 2026** (GMT -7) | Updated 2 seconds ago\n--° | 50°\nlike 61°\nClear\nN\nGusts\nTomorrow's temperature is forecast to be WARMER than today.",
          "title": "Seattle, WA Weather Conditions | Weather Underground",
          "url": "https://www.wunderground.com/weather/us/wa/seattle",
          "date": "2026-05-20",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "Clear\n56°\n73°\n49°\nPrecipitation:0%\nWind:3 mphNNE\nHumidity:69%\nUV Index:Low\nSeattle, WA\nChange Location\nWednesday\n73\n49\n0%\nClear\nWind:3 mphNNE\nHumidity:69%\nUV Index:Low\nThursday\n73\n51\n...\nPartly Cloudy\nWind:9 mphN\nHumidity:56%\nUV Index:High\nFriday\n74\n...\nSunny\nWind:7 mphNNW\nHumidity:60%\nUV Index:High\nSaturday\n...\nAM Clouds/PM Sun\n...\nSunday\n...\nCloudy\n...\nMonday\n56\n48\n40%\nShowers\nWind:12 mphSSW\nHumidity:74%\nUV Index:Moderate\nTuesday\n61\n49\n30%\nAM Showers\nWind:8 mphW\nHumidity:71%\nUV Index:High",
          "title": "Weather - KOMO News",
          "url": "https://komonews.com/weather",
          "date": "2026-05-21",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "Wednesday, May 20\n# Current Weather\n2:37 PM\n65°F\nSunny\nRealFeel® 75°\nPleasant\nRealFeel Shade™ 64°\nPleasant\nRealFeel®\n75°\nRealFeel Shade™\n64°\nMax UV Index\n5.8 (High)\nWind\nNNW 4 mph\nWind Gusts\n7 mph\nHumidity\n65%\nIndoor Humidity\n59% (Ideal Humidity)\nDew Point\n53° F\nPressure\n↓ 30.21 in\nCloud Cover\n1%\nVisibility\n6 mi\nCloud Ceiling\n40000 ft\n## Day\n5/20\n68°Hi\nRealFeel®\n75°\nPleasant\nRealFeel Shade™\n65°\nPleasant\nClouds breaking for some sun\nMax UV Index8.0 (Very High)\nAccuLumen Brightness Index™6 (Medium)\nWindN 7 mph\nWind Gusts13 mph\nProbability of Precipitation0%\nProbability of Thunderstorms0%\nPrecipitation0.00 in\nCloud Cover59%\n...\n5/20\n51°Lo\nRealFeel®\n50°\nChilly\nMainly clear\nWindNNE 6 mph\nWind Gusts12 mph\nProbability of Precipitation0%\nProbability of Thunderstorms0%\nPrecipitation0.00 in\nCloud Cover22%\n...\n## Current Weather Conditions in Seattle\nSeattle, Washington is currently Sunny with a temperature of 65°.\nThe current RealFeel® Temperature is 75° (Pleasant) based on observed conditions including 65% humidity, 1% cloud cover, a UV index of 6, and winds of 4 mph.\nIn shade, the RealFeel Shade™ is 64°.",
          "title": "Current Weather - Seattle, WA - AccuWeather",
          "url": "https://www.accuweather.com/en/us/seattle/98104/current-weather/351409",
          "date": null,
          "last_updated": "2026-05-20"
        },
        {
          "snippet": "Additional Conditions\nPressure\n30.14 °in\nVisibility\n10 °miles\nClouds\nPartly Cloudy\nDew Point\n45 °F\nHumidity\n44 °%\nRainfall\n0 °in\nSnow Depth\n0 °in\nTop Video Stories",
          "title": "Seattle, WA 10-Day Weather Forecast",
          "url": "https://www.wunderground.com/forecast/us/wa/seattle",
          "date": "2026-05-20",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "Seattle, WA\n57°\nFeels like **57°**\nH: ° L: 49° as of 1:48 AM PDT\n2AM\n...\nLive\nSeattle\n, WA\n57°\nLive\nSeattle\n, WA\n57°\nLive\nSeattle\n, WA\n57°\nLive\n...\nSeattle weather: sunny and 70's return to end the work week",
          "title": "FOX 13 Weather for Seattle & Western Washington",
          "url": "https://www.fox13seattle.com/weather",
          "date": "2026-05-20",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "18\n°C\nClear\nFeels 18\nH: 18°   L: 10°\n## Hourly\n...\nPartly cloudy.\n...\n## Weather FAQ for Seattle, WA\nWhat is the current temperature in Seattle?\n18°\nWhat is the “feels like” temperature in Seattle?\n18°\nWhat is the high and low temperature today in Seattle?\n18°\n10°\nWhat is the probability of rain or snow today in Seattle?\n20% P.O.P.\nHow much will it rain or snow today in Seattle?\nNone expected\nWhat is the current wind speed and direction in Seattle?\n9 km/h NW\nWhat is the current humidity level in Seattle?\n52%\nAre there any active weather alerts in Seattle?\nNo\nWhat is the UV index right now in Seattle?\nLow\nWhat time is sunrise and sunset today in Seattle?\nSunrise 5:25am\nSunset 8:45pm",
          "title": "Seattle, WA Current Weather",
          "url": "https://www.theweathernetwork.com/en/city/us/washington/seattle/current?_guid_iss_=1",
          "date": "2026-05-20",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "# Seattle, WA Weather\nAs of\n- **Current Temperature**\n52\nFeels like:52°\n- **Today's high temperature**\n72°\n- **Today's low temperature**\n52°\nCurrent Weather ConditionSunny\n## Live Weather Radar\n...\n## Current Weather Details\n- **Windchill**\n52°\n- **Daily Rain**\n0\"\n- **Dew point**\n46°\n- **Monthly Rain**\n0.35\"\n- **Humidity**\n81%\n- **Avg.\nWind**\nW 2 mph\n- **Pressure**\n30.19\" →\n- **Wind Gust**\nW 3 mph\n- **Sunrise**\n5:25 AM\n- **Moon**\nWaxing Crescent\n- **Sunset**\n8:47 PM\n- **UV Index**\n7 (High)\n## Weather Forecast\n- ### Today\nHi\nSunny.\nHighs in the upper 60s to mid 70s.\nLight wind becoming northwest around 10 mph in the afternoon.\n- ### Tonight\nLo\nMostly clear.\nLows in the lower 50s.\nNorth wind to 10 mph in the evening becoming light.",
          "title": "Seattle, WA Weather Today & Tomorrow - Local Forecast & Live ...",
          "url": "https://www.weatherbug.com/weather-forecast/now/seattle-wa-98104",
          "date": "2026-05-21",
          "last_updated": "2026-05-21"
        },
        {
          "snippet": "Seattle, WA Hourly Weather | AccuWeather\n## 11 PM\n56°\nRealFeel®\n53°\nCool\n0%\nMostly clear\nWindNNE 7 mph\nAir QualityPoor\nWind Gusts9 mph\nHumidity68%\nIndoor Humidity44% (Ideal Humidity)\nDew Point45° F\nAccuLumen Brightness Index™0 (Dark)\nCloud Cover13%\nVisibility10 mi\nCloud Ceiling34000 ft\n...\nAccuWeather's hourly forecast for Seattle provides hour-by-hour temperatures, RealFeel® Temperature, and precipitation probability through the next 10 days.\nThe current hour shows 56° with a RealFeel® of 53°, mostly clear with a 0% chance of precipitation.",
          "title": "Seattle, WA Hourly Weather - AccuWeather",
          "url": "https://www.accuweather.com/en/us/seattle/98104/hourly-weather-forecast/351409",
          "date": null,
          "last_updated": "2026-05-21"
        }
      ],
      "server_time": null
    }
    ```
  </Accordion>
</AccordionGroup>

## Understanding Chunk Types

In concise mode, you'll receive four different types of chunks during the stream:

### 1. `chat.reasoning`

Streamed during the reasoning stage, containing real-time reasoning steps and search operations.

<Tabs>
  <Tab title="Structure">
    ```json theme={null}
    {
      "id": "cfa38f9d-fdbc-4ac6-a5d2-a3010b6a33a6",
      "model": "sonar-pro",
      "created": 1759441590,
      "object": "chat.reasoning",
      "choices": [{
        "index": 0,
        "finish_reason": null,
        "message": {
          "role": "assistant",
          "content": ""
        },
        "delta": {
          "role": "assistant",
          "content": "",
          "reasoning_steps": [{
            "thought": "Searching the web for Seattle's current weather...",
            "type": "web_search",
            "web_search": {
              "search_results": [...],
              "search_keywords": ["Seattle current weather"]
            }
          }]
        }
      }],
      "type": "message"
    }
    ```
  </Tab>

  <Tab title="Python Handler">
    ```python theme={null}
    def handle_reasoning_chunk(chunk):
        """Process reasoning stage updates"""
        if chunk.object == "chat.reasoning":
            delta = chunk.choices[0].delta

            if hasattr(delta, 'reasoning_steps'):
                for step in delta.reasoning_steps:
                    print(f"\n[Reasoning] {step.thought}")

                    if step.type == "web_search":
                        keywords = step.web_search.search_keywords
                        print(f"[Search] Keywords: {', '.join(keywords)}")
    ```
  </Tab>

  <Tab title="Typescript Handler">
    ```typescript theme={null}
    function handleReasoningChunk(chunk: any) {
      if (chunk.object === "chat.reasoning") {
        const delta = chunk.choices[0].delta;

        if (delta.reasoning_steps) {
          for (const step of delta.reasoning_steps) {
            console.log(`\n[Reasoning] ${step.thought}`);

            if (step.type === "web_search") {
              const keywords = step.web_search.search_keywords;
              console.log(`[Search] Keywords: ${keywords.join(', ')}`);
            }
          }
        }
      }
    }
    ```
  </Tab>
</Tabs>

### 2. `chat.reasoning.done`

Marks the end of the reasoning stage and includes all search results (web, images, videos) and reasoning steps.

<Tabs>
  <Tab title="Structure">
    ```json theme={null}
    {
      "id": "3dd9d463-0fef-47e3-af70-92f9fcc4db1f",
      "model": "sonar-pro",
      "created": 1759459505,
      "object": "chat.reasoning.done",
      "usage": {
        "prompt_tokens": 6,
        "completion_tokens": 0,
        "total_tokens": 6,
        "search_context_size": "low"
      },
      "search_results": [...],
      "images": [...],
      "choices": [{
        "index": 0,
        "finish_reason": null,
        "message": {
          "role": "assistant",
          "content": "",
          "reasoning_steps": [...]
        },
        "delta": {
          "role": "assistant",
          "content": ""
        }
      }]
    }
    ```
  </Tab>

  <Tab title="Python Handler">
    ```python theme={null}
    def handle_reasoning_done(chunk):
        """Process end of reasoning stage"""
        if chunk.object == "chat.reasoning.done":
            print("\n[Reasoning Complete]")

            # Access all search results
            if hasattr(chunk, 'search_results'):
                print(f"Found {len(chunk.search_results)} sources")
                for result in chunk.search_results[:3]:
                    print(f"  • {result['title']}")

            # Access image results
            if hasattr(chunk, 'images'):
                print(f"Found {len(chunk.images)} images")

            # Partial usage stats available
            if hasattr(chunk, 'usage'):
                print(f"Tokens used so far: {chunk.usage.total_tokens}")
    ```
  </Tab>

  <Tab title="Typescript Handler">
    ```typescript theme={null}
    function handleReasoningDone(chunk: any) {
      if (chunk.object === "chat.reasoning.done") {
        console.log("\n[Reasoning Complete]");

        // Access all search results
        if (chunk.search_results) {
          console.log(`Found ${chunk.search_results.length} sources`);
          chunk.search_results.slice(0, 3).forEach((result: any) => {
            console.log(`  • ${result.title}`);
          });
        }

        // Access image results
        if (chunk.images) {
          console.log(`Found ${chunk.images.length} images`);
        }

        // Partial usage stats available
        if (chunk.usage) {
          console.log(`Tokens used so far: ${chunk.usage.total_tokens}`);
        }
      }
    }
    ```
  </Tab>
</Tabs>

### 3. `chat.completion.chunk`

Streamed during the response generation stage, containing the actual content being generated.

<Tabs>
  <Tab title="Structure">
    ```json theme={null}
    {
      "id": "cfa38f9d-fdbc-4ac6-a5d2-a3010b6a33a6",
      "model": "sonar-pro",
      "created": 1759441592,
      "object": "chat.completion.chunk",
      "choices": [{
        "index": 0,
        "finish_reason": null,
        "message": {
          "role": "assistant",
          "content": ""
        },
        "delta": {
          "role": "assistant",
          "content": " tonight"
        }
      }]
    }
    ```
  </Tab>

  <Tab title="Python Handler">
    ```python theme={null}
    def handle_completion_chunk(chunk):
        """Process content generation updates"""
        if chunk.object == "chat.completion.chunk":
            delta = chunk.choices[0].delta

            if hasattr(delta, 'content') and delta.content:
                # Stream content to user
                print(delta.content, end='', flush=True)
                return delta.content

        return ""
    ```
  </Tab>

  <Tab title="Typescript Handler">
    ```typescript theme={null}
    function handleCompletionChunk(chunk: any): string {
      if (chunk.object === "chat.completion.chunk") {
        const delta = chunk.choices[0]?.delta;

        if (delta?.content) {
          // Stream content to user
          process.stdout.write(delta.content);
          return delta.content;
        }
      }

      return "";
    }
    ```
  </Tab>
</Tabs>

### 4. `chat.completion.done`

Final chunk indicating the stream is complete, including final search results, usage statistics, and cost information.

<Tabs>
  <Tab title="Structure">
    ```json theme={null}
    {
      "id": "cfa38f9d-fdbc-4ac6-a5d2-a3010b6a33a6",
      "model": "sonar-pro",
      "created": 1759441595,
      "object": "chat.completion.done",
      "usage": {
        "prompt_tokens": 6,
        "completion_tokens": 238,
        "total_tokens": 244,
        "search_context_size": "low",
        "cost": {
          "input_tokens_cost": 0.0,
          "output_tokens_cost": 0.004,
          "request_cost": 0.006,
          "total_cost": 0.01
        }
      },
      "search_results": [...],
      "images": [...],
      "choices": [{
        "index": 0,
        "finish_reason": "stop",
        "message": {
          "role": "assistant",
          "content": "## Seattle Weather Forecast\n\nSeattle is experiencing...",
          "reasoning_steps": [...]
        },
        "delta": {
          "role": "assistant",
          "content": ""
        }
      }]
    }
    ```
  </Tab>

  <Tab title="Python Handler">
    ```python theme={null}
    def handle_completion_done(chunk):
        """Process stream completion"""
        if chunk.object == "chat.completion.done":
            print("\n\n[Stream Complete]")

            # Final aggregated message
            full_message = chunk.choices[0].message.content

            # Final search results
            if hasattr(chunk, 'search_results'):
                print(f"\nFinal sources: {len(chunk.search_results)}")

            # Complete usage and cost information
            if hasattr(chunk, 'usage'):
                usage = chunk.usage
                print(f"\nTokens: {usage.total_tokens}")

                if hasattr(usage, 'cost'):
                    print(f"Cost: ${usage.cost.total_cost:.4f}")

            return {
                'content': full_message,
                'search_results': getattr(chunk, 'search_results', []),
                'images': getattr(chunk, 'images', []),
                'usage': getattr(chunk, 'usage', None)
            }
    ```
  </Tab>

  <Tab title="Typescript Handler">
    ```typescript theme={null}
    function handleCompletionDone(chunk: any) {
      if (chunk.object === "chat.completion.done") {
        console.log("\n\n[Stream Complete]");

        // Final aggregated message
        const fullMessage = chunk.choices[0].message.content;

        // Final search results
        if (chunk.search_results) {
          console.log(`\nFinal sources: ${chunk.search_results.length}`);
        }

        // Complete usage and cost information
        if (chunk.usage) {
          console.log(`\nTokens: ${chunk.usage.total_tokens}`);

          if (chunk.usage.cost) {
            console.log(`Cost: $${chunk.usage.cost.total_cost.toFixed(4)}`);
          }
        }

        return {
          content: fullMessage,
          search_results: chunk.search_results || [],
          images: chunk.images || [],
          usage: chunk.usage || null
        };
      }
    }
    ```
  </Tab>
</Tabs>

## Complete Implementation Examples

### Full Concise Mode Handler

<Tabs>
  <Tab title="Python SDK">
    ```python theme={null}
    from perplexity import Perplexity

    class ConciseStreamHandler:
        def __init__(self):
            self.content = ""
            self.reasoning_steps = []
            self.search_results = []
            self.images = []
            self.usage = None

        def stream_query(self, query: str, model: str = "sonar-pro"):
            """Handle a complete concise streaming request"""
            client = Perplexity()

            stream = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": query}],
                stream=True,
                stream_mode="concise"
            )

            for chunk in stream:
                self.process_chunk(chunk)

            return self.get_result()

        def process_chunk(self, chunk):
            """Route chunk to appropriate handler"""
            chunk_type = chunk.object

            if chunk_type == "chat.reasoning":
                self.handle_reasoning(chunk)
            elif chunk_type == "chat.reasoning.done":
                self.handle_reasoning_done(chunk)
            elif chunk_type == "chat.completion.chunk":
                self.handle_content(chunk)
            elif chunk_type == "chat.completion.done":
                self.handle_done(chunk)

        def handle_reasoning(self, chunk):
            """Process reasoning updates"""
            delta = chunk.choices[0].delta

            if hasattr(delta, 'reasoning_steps'):
                for step in delta.reasoning_steps:
                    self.reasoning_steps.append(step)
                    print(f"💭 {step.thought}")

        def handle_reasoning_done(self, chunk):
            """Process end of reasoning"""
            if hasattr(chunk, 'search_results'):
                self.search_results = chunk.search_results
                print(f"\n🔍 Found {len(self.search_results)} sources")

            if hasattr(chunk, 'images'):
                self.images = chunk.images
                print(f"🖼️  Found {len(self.images)} images")

            print("\n📝 Generating response...\n")

        def handle_content(self, chunk):
            """Process content chunks"""
            delta = chunk.choices[0].delta

            if hasattr(delta, 'content') and delta.content:
                self.content += delta.content
                print(delta.content, end='', flush=True)

        def handle_done(self, chunk):
            """Process completion"""
            if hasattr(chunk, 'usage'):
                self.usage = chunk.usage
                print(f"\n\n✅ Complete | Tokens: {self.usage.total_tokens}")

                if hasattr(self.usage, 'cost'):
                    print(f"💰 Cost: ${self.usage.cost.total_cost:.4f}")

        def get_result(self):
            """Return complete result"""
            return {
                'content': self.content,
                'reasoning_steps': self.reasoning_steps,
                'search_results': self.search_results,
                'images': self.images,
                'usage': self.usage
            }

    # Usage
    handler = ConciseStreamHandler()
    result = handler.stream_query("What's the latest news in AI?")

    print(f"\n\nFinal content length: {len(result['content'])} characters")
    print(f"Sources used: {len(result['search_results'])}")
    ```
  </Tab>

  <Tab title="Typescript SDK">
    ```typescript theme={null}
    import Perplexity from '@perplexity-ai/perplexity_ai';

    interface StreamResult {
      content: string;
      reasoning_steps: any[];
      search_results: any[];
      images: any[];
      usage: any;
    }

    class ConciseStreamHandler {
      private content: string = "";
      private reasoning_steps: any[] = [];
      private search_results: any[] = [];
      private images: any[] = [];
      private usage: any = null;

      async streamQuery(query: string, model: string = "sonar-pro"): Promise<StreamResult> {
        const client = new Perplexity();

        const stream = await client.chat.completions.create({
          model,
          messages: [{ role: "user", content: query }],
          stream: true,
          stream_mode: "concise"
        });

        for await (const chunk of stream) {
          this.processChunk(chunk);
        }

        return this.getResult();
      }

      private processChunk(chunk: any) {
        const chunkType = chunk.object;

        switch (chunkType) {
          case "chat.reasoning":
            this.handleReasoning(chunk);
            break;
          case "chat.reasoning.done":
            this.handleReasoningDone(chunk);
            break;
          case "chat.completion.chunk":
            this.handleContent(chunk);
            break;
          case "chat.completion.done":
            this.handleDone(chunk);
            break;
        }
      }

      private handleReasoning(chunk: any) {
        const delta = chunk.choices[0].delta;

        if (delta.reasoning_steps) {
          for (const step of delta.reasoning_steps) {
            this.reasoning_steps.push(step);
            console.log(`💭 ${step.thought}`);
          }
        }
      }

      private handleReasoningDone(chunk: any) {
        if (chunk.search_results) {
          this.search_results = chunk.search_results;
          console.log(`\n🔍 Found ${this.search_results.length} sources`);
        }

        if (chunk.images) {
          this.images = chunk.images;
          console.log(`🖼️  Found ${this.images.length} images`);
        }

        console.log("\n📝 Generating response...\n");
      }

      private handleContent(chunk: any) {
        const delta = chunk.choices[0]?.delta;

        if (delta?.content) {
          this.content += delta.content;
          process.stdout.write(delta.content);
        }
      }

      private handleDone(chunk: any) {
        if (chunk.usage) {
          this.usage = chunk.usage;
          console.log(`\n\n✅ Complete | Tokens: ${this.usage.total_tokens}`);

          if (this.usage.cost) {
            console.log(`💰 Cost: $${this.usage.cost.total_cost.toFixed(4)}`);
          }
        }
      }

      private getResult(): StreamResult {
        return {
          content: this.content,
          reasoning_steps: this.reasoning_steps,
          search_results: this.search_results,
          images: this.images,
          usage: this.usage
        };
      }
    }

    // Usage
    const handler = new ConciseStreamHandler();
    const result = await handler.streamQuery("What's the latest news in AI?");

    console.log(`\n\nFinal content length: ${result.content.length} characters`);
    console.log(`Sources used: ${result.search_results.length}`);
    ```
  </Tab>

  <Tab title="Raw HTTP">
    ```python theme={null}
    import os
    import requests
    import json

    def stream_concise_mode(query: str):
        """Handle concise streaming with raw HTTP"""
        url = "https://api.perplexity.ai/v1/sonar"
        headers = {
            "Authorization": f"Bearer {os.environ.get('PERPLEXITY_API_KEY')}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "sonar-pro",
            "messages": [{"role": "user", "content": query}],
            "stream": True,
            "stream_mode": "concise"
        }

        response = requests.post(url, headers=headers, json=payload, stream=True)

        content = ""
        search_results = []
        usage = None

        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    data_str = line[6:]
                    if data_str == '[DONE]':
                        break

                    try:
                        chunk = json.loads(data_str)
                        chunk_type = chunk.get('object')

                        if chunk_type == 'chat.reasoning':
                            # Handle reasoning
                            delta = chunk['choices'][0]['delta']
                            if 'reasoning_steps' in delta:
                                for step in delta['reasoning_steps']:
                                    print(f"💭 {step['thought']}")

                        elif chunk_type == 'chat.reasoning.done':
                            # Handle reasoning completion
                            if 'search_results' in chunk:
                                search_results = chunk['search_results']
                                print(f"\n🔍 Found {len(search_results)} sources\n")

                        elif chunk_type == 'chat.completion.chunk':
                            # Handle content
                            delta = chunk['choices'][0]['delta']
                            if 'content' in delta and delta['content']:
                                content += delta['content']
                                print(delta['content'], end='', flush=True)

                        elif chunk_type == 'chat.completion.done':
                            # Handle completion
                            if 'usage' in chunk:
                                usage = chunk['usage']
                                print(f"\n\n✅ Tokens: {usage['total_tokens']}")

                    except json.JSONDecodeError:
                        continue

        return {
            'content': content,
            'search_results': search_results,
            'usage': usage
        }

    # Usage
    result = stream_concise_mode("What's the latest news in AI?")
    ```
  </Tab>
</Tabs>

## Best Practices

<Steps>
  <Step title="Aggregate content on the client side">
    In concise mode, `choices.message` is not incrementally updated. You must aggregate chunks yourself.

    ```python theme={null}
    # Track content yourself
    content = ""
    for chunk in stream:
        if chunk.object == "chat.completion.chunk":
            if chunk.choices[0].delta.content:
                content += chunk.choices[0].delta.content
    ```
  </Step>

  <Step title="Use reasoning steps for transparency">
    Display reasoning steps to users for better transparency and trust.

    ```python theme={null}
    def display_reasoning(step):
        """Show reasoning to users"""
        print(f"🔍 Searching for: {step.web_search.search_keywords}")
        print(f"💭 {step.thought}")
    ```
  </Step>

  <Step title="Handle search results from done chunks only">
    Search results and usage information only appear in `chat.reasoning.done` and `chat.completion.done` chunks.

    ```python theme={null}
    # Don't check for search_results in other chunk types
    if chunk.object in ["chat.reasoning.done", "chat.completion.done"]:
        if hasattr(chunk, 'search_results'):
            process_search_results(chunk.search_results)
    ```
  </Step>

  <Step title="Implement proper type checking">
    Use the `object` field to route chunks to appropriate handlers.

    ```python theme={null}
    chunk_handlers = {
        "chat.reasoning": handle_reasoning,
        "chat.reasoning.done": handle_reasoning_done,
        "chat.completion.chunk": handle_content,
        "chat.completion.done": handle_done
    }

    handler = chunk_handlers.get(chunk.object)
    if handler:
        handler(chunk)
    ```
  </Step>

  <Step title="Track cost from the final chunk">
    Cost information is only available in the `chat.completion.done` chunk.

    ```python theme={null}
    if chunk.object == "chat.completion.done":
        if hasattr(chunk.usage, 'cost'):
            total_cost = chunk.usage.cost.total_cost
            print(f"Request cost: ${total_cost:.4f}")
    ```
  </Step>
</Steps>

## Migration from Full Mode

If you're migrating from full mode to concise mode, here are the key changes:

<Tabs>
  <Tab title="Before (Full Mode)">
    ```python theme={null}
    from perplexity import Perplexity

    client = Perplexity()

    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "What's the weather?"}],
        stream=True
        # stream_mode defaults to "full"
    )

    for chunk in stream:
        # All chunks are chat.completion.chunk
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")

        # Search results may appear in multiple chunks
        if hasattr(chunk, 'search_results'):
            print(f"Sources: {len(chunk.search_results)}")
    ```
  </Tab>

  <Tab title="After (Concise Mode)">
    ```python theme={null}
    from perplexity import Perplexity

    client = Perplexity()

    stream = client.chat.completions.create(
        model="sonar-pro",
        messages=[{"role": "user", "content": "What's the weather?"}],
        stream=True,
        stream_mode="concise"  # Enable concise mode
    )

    for chunk in stream:
        # Multiple chunk types - route appropriately
        if chunk.object == "chat.reasoning":
            # New: Handle reasoning steps
            if chunk.choices[0].delta.reasoning_steps:
                print("Reasoning in progress...")

        elif chunk.object == "chat.reasoning.done":
            # New: Reasoning complete, search results available
            if hasattr(chunk, 'search_results'):
                print(f"Sources: {len(chunk.search_results)}")

        elif chunk.object == "chat.completion.chunk":
            # Content chunks (similar to full mode)
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="")

        elif chunk.object == "chat.completion.done":
            # Final chunk with complete metadata
            print(f"\nTotal tokens: {chunk.usage.total_tokens}")
    ```
  </Tab>
</Tabs>

## When to Use Each Mode

<CardGroup>
  <Card title="Use Full Mode" icon="clipboard-list">
    * Simple integrations where you want the SDK to handle aggregation
    * Backward compatibility with existing implementations
    * When you don't need reasoning visibility
  </Card>

  <Card title="Use Concise Mode" icon="bolt">
    * Production applications optimizing for bandwidth
    * Applications that need reasoning transparency
    * Real-time chat interfaces with reasoning display
    * Cost-sensitive applications
  </Card>
</CardGroup>

## Resources

* [Streaming Responses Guide](/docs/agent-api/output-control#streaming-responses) - General streaming documentation
* [Sonar API Guide](/docs/sonar/quickstart) - Complete Sonar API guide
* [API Reference - Sonar API](/api-reference/sonar-post) - API documentation
