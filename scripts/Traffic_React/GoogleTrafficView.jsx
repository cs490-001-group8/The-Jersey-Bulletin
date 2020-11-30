import React, { useEffect, useState } from 'react';
import GoogleMapReact from 'google-map-react';
import { Socket } from '../Socket';

const createMapOptions = () => ({
    panControl: false,
    mapTypeControl: false,
    scrollwheel: false,
    styles: [
        {
            stylers: [{ saturation: -100 }, { gamma: 0.8 },
                { lightness: 4 },
                { visibility: 'on' }],
        },
    ],
});

const getAPIkey = () => (
    process.env.GOOGLE_MAP_API_KEY
);

export default function GoogleTrafficView() {
    const [currCoordinates, setCurrCoordinates] = useState(() => (
        { lat: 40.560806, lng: -74.465591 }));
    const [zoom, setZoom] = useState(() => 9);

    useEffect(() => {
        Socket.on('location_update', (data) => {
            setCurrCoordinates(data);
            setZoom(12);
        });
    }, []);

    return (
        <div className="traffic-map">
            <GoogleMapReact
              bootstrapURLKeys={{
                    key: getAPIkey(),
                    language: 'en',
                    region: 'us',
                }}
              center={currCoordinates}
              zoom={zoom}
              layerTypes={['TrafficLayer']}
              options={createMapOptions}
            />
        </div>
    );
}
