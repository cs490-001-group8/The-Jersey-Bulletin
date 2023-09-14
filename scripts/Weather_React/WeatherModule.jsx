import React, { useState, useEffect } from 'react';
import WidgetTitle from '../WidgetTitle';
import WeatherHourly from './WeatherHourly';
import { Socket } from '../Socket';

export default function WeatherModule() {
    const [currWeather, setCurrWeather] = useState(() => []);
    const [currCity, setCurrCity] = useState(() => 'Hourly');
    useEffect(() => {
        Socket.emit('get last weather input', {
            localStorage: localStorage.getItem('weatherInput'),
        });
        Socket.on('here last weather input', (data) => {
            const weatherInput = data.last_weather_input;
            localStorage.setItem('weatherInput', weatherInput);
        });
        Socket.on('send weather', (data) => {
            setCurrCity(data.city_name);
            setCurrWeather([]);
            const iterWeather = [];
            for (let i = 0; i < data.hourly.length; i += 1) {
                const temp = (
                    <WeatherHourly
                      key={i}
                      time={data.hourly[i].time}
                      icon={data.hourly[i].icon}
                      description={data.hourly[i].description}
                      temp={`${Math.round(data.hourly[i].temp)} °F`}
                    />
                );
                iterWeather.push(temp);
            }
            // eslint-disable-next-line no-shadow
            setCurrWeather((currWeather) => [...currWeather, iterWeather]);
        });

        Socket.on('weather error', () => {
            setCurrCity('Hourly');
            setCurrWeather([]);
            setCurrWeather((currWeather) => [...currWeather, 'Please enter a valid NJ zipcode or city name!']);
        });
        return () => {
            Socket.off('here last weather input');
        };
    }, []);

    function handleSubmit(event) {
        const currCityEvent = document.getElementById('inputCity');
        const currCityValue = currCityEvent.value;
        Socket.emit('weather request', {
            city_name: currCityValue,
        });
        Socket.emit('last weather input', {
            last_weather_input: currCityValue,
        });
        localStorage.setItem('weatherInput', currCityValue);
        currCityEvent.value = '';
        event.preventDefault();
        setCurrWeather([]);
    }
    return (
        <div className="widget weather_widget">
            <WidgetTitle title={`${currCity} Forecast`} />
            <form onSubmit={handleSubmit}>
                <input className="commuter-input" id="inputCity" placeholder="Search your city" type="text" />
            </form>
            <hr />
            {currWeather.length !== 0 || !localStorage.getItem("weatherInput") ? currWeather : <div className="loader" />}
        </div>
    );
}
