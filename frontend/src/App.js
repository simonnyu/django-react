import React from 'react';
import './App.css';
import {FormattedMessage} from 'react-intl';
function App({setLocale}) {
  return (
    <div className="App">
      <header className="App-header">
      <button onClick={() => setLocale('en')}>English</button>
          <button onClick={() => setLocale('zh-Hant')}>中文</button>
 
        <p><FormattedMessage id="home.welcome"/></p>
      </header>
    </div>
  );
}

export default App;
