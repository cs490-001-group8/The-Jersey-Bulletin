/* eslint react/prop-types: 0 */
/* eslint jsx-a11y/no-static-element-interactions: 0 */
/* eslint jsx-a11y/click-events-have-key-events: 0 */
/* eslint no-alert: 0 */
/* eslint no-restricted-syntax: */
// Proptype enforcement breaks the module.
// There is interaction with the module
// There is interaction with the mouse, no key event necessary.
// Alert is used to display to the user an error, necessary.
// Didn't like for loop syntax but for loop is legal.
import React, { useEffect } from 'react';
import { Socket } from './Socket';

let widgetCount = 1;
let absoluteClass = true;
const selectedDict = {
    News: false,
    Weather: false,
    Traffic: false,
    Bills: false,
    Politician_Twitter: false,
    Hiking_Destinations: false,
    Sports: false,
};

function handleClick(data) {
    if (selectedDict[data]) {
        selectedDict[data] = false;
        widgetCount -= 1;
        Socket.emit('personal tab change', selectedDict);
    } else if (widgetCount <= 3) {
        selectedDict[data] = true;
        widgetCount += 1;
        Socket.emit('personal tab change', selectedDict);
    } else {
        alert('Only select three widgets!');
    }

    if (widgetCount <= 1) {
        absoluteClass = true;
    } else {
        absoluteClass = false;
    }
}

export default function TabChooser() {
    useEffect(() => {
        Socket.on('update existing personal', (data) => {
            for (const property in data) {
                if (data[property]) {
                    handleClick(property);
                }
            }
        });
    }, []);

    return (
        <div className={absoluteClass && 'absolute-class'}>
            <div className="icon-bar">
                <div className={selectedDict.News ? 'selected' : 'unselected'}>
                    <i
                      title="News"
                      className="far fa-newspaper fa-2x"
                      onClick={() => handleClick('News')}
                    />
                </div>
                <div className={selectedDict.Weather ? 'selected' : 'unselected'}>
                    <i
                      title="Weather"
                      className="fas fa-sun fa-2x"
                      onClick={() => handleClick('Weather')}
                    />
                </div>
                <div className={selectedDict.Traffic ? 'selected' : 'unselected'}>
                    <i
                      title="Traffic"
                      className="fas fa-traffic-light fa-2x"
                      onClick={() => handleClick('Traffic')}
                    />
                </div>
                <div className={selectedDict.Bills ? 'selected' : 'unselected'}>
                    <i
                      title="Bills"
                      className="fas fa-vote-yea fa-2x"
                      onClick={() => handleClick('Bills')}
                    />
                </div>
                <div className={selectedDict.Politician_Twitter ? 'selected' : 'unselected'}>
                    <i
                      title="Politican Twitter"
                      className="fab fa-twitter fa-2x"
                      onClick={() => handleClick('Politician_Twitter')}
                    />
                </div>
                <div className={selectedDict.Hiking_Destinations ? 'selected' : 'unselected'}>
                    <i
                      title="Hiking Destinations"
                      className="fas fa-mountain fa-2x"
                      onClick={() => handleClick('Hiking_Destinations')}
                    />
                </div>
                <div className={selectedDict.Sports ? 'selected' : 'unselected'}>
                    <i
                      title="Sports"
                      className="fas fa-football-ball fa-2x"
                      onClick={() => handleClick('Sports')}
                    />
                </div>
            </div>
        </div>
    );
}
